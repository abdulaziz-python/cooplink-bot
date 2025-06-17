# -*- coding: utf-8 -*-
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database.db import get_listing, update_listing_status, get_total_users, get_total_listings, get_all_users
from keyboards.reply import main_menu_keyboard
from utils.localization import get_string
from utils.helpers import to_html, format_html
from config import config, ADMIN_IDS 
from constants import Button, ButtonText, Channel, Config
from utils.filters import text_contains_button

router = Router()

class Broadcast(StatesGroup):
    waiting_for_message = State()

@router.message(Command("admin"))
async def admin_panel(message: Message):
    if message.from_user.id not in config.ADMIN_IDS:
        return
    
    total_users = await get_total_users()
    total_listings = await get_total_listings()
    
    admin_panel_template = get_string('admin_panel', Config.DEFAULT_LANGUAGE)
    admin_panel_text = format_html(
        admin_panel_template,
        total_users=total_users,
        total_listings=total_listings
    )
    
    await message.answer(
        text=admin_panel_text,
        parse_mode="HTML"
    )

@router.message(Command("broadcast"))
async def broadcast_command(message: Message, state: FSMContext):
    if message.from_user.id not in ADMIN_IDS:
        return
    
    broadcast_text = to_html(get_string('broadcast', 'uz'))
    
    await message.answer(
        text=broadcast_text,
        parse_mode="HTML"
    )
    
    await state.set_state(Broadcast.waiting_for_message)

@router.message(Broadcast.waiting_for_message)
async def process_broadcast(message: Message, state: FSMContext):
    if message.from_user.id not in ADMIN_IDS:
        return
    
    users = await get_all_users()
    count = 0
    
    broadcast_message = message.text
    
    for user in users:
        try:
            await message.bot.send_message(
                chat_id=user['user_id'],
                text=broadcast_message
            )
            count += 1
        except Exception as e:
            print(f"Error sending broadcast to {user['user_id']}: {e}")
    
    broadcast_sent_template = get_string('broadcast_sent', 'uz')
    broadcast_sent_text = format_html(
        broadcast_sent_template,
        count=count
    )
    
    await message.answer(
        text=broadcast_sent_text,
        parse_mode="HTML"
    )
    
    await state.clear()

@router.callback_query(F.data.startswith("approve_"))
async def approve_listing(callback: CallbackQuery):
    if callback.from_user.id not in config.ADMIN_IDS:
        return
        
    listing_id = int(callback.data.split("_")[1])
    listing = await get_listing(listing_id)
    
    if not listing:
        await callback.answer("Listing not found!")
        return
    
    await update_listing_status(listing_id, "approved")
    
    try:
        chat = await callback.bot.get_chat(listing['user_id'])
        username = chat.username or f"User#{listing['user_id']}"
        
        announcement_template = get_string('announcement', Config.DEFAULT_LANGUAGE)
        announcement_data = {**listing, 'owner': f"@{username}"}
        announcement_text = format_html(
            announcement_template,
            **announcement_data
        )
        
        if listing['image_file_id']:
            await callback.bot.send_photo(
                chat_id=Channel.ANNOUNCEMENT,
                photo=listing['image_file_id'],
                caption=announcement_text,
                parse_mode="HTML"
            )
        else:
            await callback.bot.send_message(
                chat_id=Channel.ANNOUNCEMENT,
                text=announcement_text,
                parse_mode="HTML"
            )
        
        approved_text = to_html(
            get_string('listing_approved', Config.DEFAULT_LANGUAGE)
        )
        
        await callback.bot.send_message(
            chat_id=listing['user_id'],
            text=approved_text,
            parse_mode="HTML"
        )
        
        await callback.answer("Listing approved and published!")
        
        # For edit_text, we need to be careful with the original message
        updated_message = callback.message.text + "\n\n✅ Approved"
        await callback.message.edit_text(
            text=updated_message
        )
    except Exception as e:
        print(f"Error approving listing: {e}")
        await callback.answer("Error approving listing!")

@router.callback_query(F.data.startswith("reject_"))
async def reject_listing(callback: CallbackQuery):
    if callback.from_user.id not in ADMIN_IDS:
        return
    
    listing_id = int(callback.data.split("_")[1])
    
    listing = await get_listing(listing_id)
    
    if not listing:
        await callback.answer("Listing not found!")
        return
    
    await update_listing_status(listing_id, "rejected")
    
    user_id = listing['user_id']
    
    try:
        rejected_text = to_html(get_string('listing_rejected', 'uz'))
        
        await callback.bot.send_message(
            chat_id=user_id,
            text=rejected_text,
            parse_mode="HTML"
        )
        
        await callback.answer("Listing rejected!")
        
        updated_message = callback.message.text + "\n\n❌ Rejected"
        await callback.message.edit_text(
            text=updated_message
        )
    except Exception as e:
        print(f"Error rejecting listing: {e}")
        await callback.answer("Error rejecting listing!")

