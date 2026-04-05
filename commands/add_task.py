from telegram import Update
from telegram.ext import ContextTypes
from services.task_service import add_task

async def add_task_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    task_text = " ".join(context.args)
    if task_text:
        add_task(update.message.from_user.id, task_text)
        await update.message.reply_text(f"Задача добавлена: {task_text}")
    else:
        await update.message.reply_text("Пожалуйста, укажи текст задачи.")
