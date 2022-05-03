import hashlib
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle

from config import settings

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.inline_handler()
async def inline_handler(inline_query: types.InlineQuery):
    text = inline_query.query or 'echo'
    input_content = InputTextMessageContent(text)
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    item = InlineQueryResultArticle(
        id=result_id,
        title=f'Result {text!r}',
        input_message_content=input_content,
    )
    await bot.answer_inline_query(inline_query.id,
                                  results=[item],
                                  cache_time=1)


def main():
    # dp.register_inline_handler(inline_handler, lambda inline_query: True)
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
