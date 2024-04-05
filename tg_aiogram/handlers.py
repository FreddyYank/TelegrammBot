from aiogram import Router,types,F,Bot
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

router = Router()

chat_id = 1489684112

@router.message(Command('start'))
async def start_command(message:Message,bot:Bot):
    await message.answer(f"Пишите мне, как писали бы Паше:")
    @router.message()
    async def talk_command(message:Message,bot:Bot):
        if message.text == '/cancel':
            await message.answer(f'Вы вышли из режима прослушки. Нет')
        else:
            await message.answer(f'Сообщение от {message.from_user.full_name} chat_id:{message.chat.id}:')
            await bot.forward_message(chat_id,message.chat.id,message.message_id)
