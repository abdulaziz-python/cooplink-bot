# -*- coding: utf-8 -*-
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database.db import add_user, update_language, get_user_listings_count
from keyboards.reply import language_keyboard, main_menu_keyboard
from utils.localization import get_string
from utils.helpers import to_html, format_html
from constants import Button, ButtonText, Language, Config
from utils.filters import text_contains_button

router = Router()

class LanguageSelection(StatesGroup):
    waiting_for_language = State()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await add_user(
        user_id=message.from_user.id,
        username=message.from_user.username or "Unknown"
    )
    
    welcome_text = to_html("🇺🇿 *Xush kelibsiz!* / 🇷🇺 *Добро пожаловать!*\n\nTilni tanlang / Выберите язык:")
    
    await message.answer(
        text=welcome_text,
        reply_markup=language_keyboard(),
        parse_mode="HTML"
    )
    await state.set_state(LanguageSelection.waiting_for_language)

@router.message(LanguageSelection.waiting_for_language, F.text.contains("\u0420\u0443\u0441\u0441\u043a\u0438\u0439"))
async def language_selected_ru(message: Message, state: FSMContext):
    await update_language(message.from_user.id, 'ru')
    
    language_selected_text = to_html(get_string('language_selected', 'ru'))
    main_menu_text = to_html(get_string('main_menu', 'ru'))
    
    await message.answer(
        text=language_selected_text,
        parse_mode="HTML"
    )
    
    await message.answer(
        text=main_menu_text,
        reply_markup=main_menu_keyboard('ru'),
        parse_mode="HTML"
    )
    
    await state.clear()

@router.message(LanguageSelection.waiting_for_language, F.text.contains("O'zbek"))
async def language_selected_uz(message: Message, state: FSMContext):
    await update_language(message.from_user.id, 'uz')
    
    language_selected_text = to_html(get_string('language_selected', 'uz'))
    main_menu_text = to_html(get_string('main_menu', 'uz'))
    
    await message.answer(
        text=language_selected_text,
        parse_mode="HTML"
    )
    
    await message.answer(
        text=main_menu_text,
        reply_markup=main_menu_keyboard('uz'),
        parse_mode="HTML"
    )
    
    await state.clear()

@router.message(text_contains_button(Button.PROFILE))
async def show_profile(message: Message, **kwargs):
    user_data = kwargs.get('user_data', {})
    language = user_data.get('language', Config.DEFAULT_LANGUAGE)
    
    listings_count = await get_user_listings_count(message.from_user.id)
    username = message.from_user.username or "Unknown"
    
    profile_template = get_string('profile', language)
    profile_text = format_html(
        profile_template,
        user_id=message.from_user.id,
        username=username,
        listings_count=listings_count
    )
    
    await message.answer(
        text=profile_text,
        parse_mode="HTML"
    )

@router.message(text_contains_button(Button.HELP))
async def show_help(message: Message, **kwargs):
    user_data = kwargs.get('user_data', {})
    language = user_data.get('language', Config.DEFAULT_LANGUAGE)
    
    help_text = to_html(get_string('help', language))
    
    await message.answer(
        text=help_text,
        parse_mode="HTML"
    )

