from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - запуск бота\n"
        "/help - помощь\n"
        "/tasks - список твоих задач\n"
        "/add_task <текст> - добавить задачу\n"
        "/del_task <номер> - удалить задачу\n"
        "/gpt <текст> - чат с ИИ\n"
        "/img <текст> - сгенерировать картинку"
    )
