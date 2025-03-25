# -*- coding: utf-8 -*-
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from config import channels
from utils.localization import get_string
from utils.helpers import format_html

class SubscriptionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        if isinstance(event, Message) and event.text and event.text.startswith('/start'):
            return await handler(event, data)
            
        user_id = event.from_user.id
        bot = data['bot']
        
        for channel in channels.REQUIRED:
            try:
                member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
                if member.status in ['left', 'kicked', 'banned']:
                    user_data = data.get('user_data', {})
                    language = user_data.get('language', 'uz')
                    
                    subscription_template = get_string('subscription_required', language)
                    subscription_text = format_html(
                        subscription_template,
                        channel=channel
                    )
                    
                    await event.answer(
                        subscription_text,
                        parse_mode="HTML"
                    )
                    return
            except Exception as e:
                print(f"Subscription check error: {e}")
                continue
                
        return await handler(event, data)

