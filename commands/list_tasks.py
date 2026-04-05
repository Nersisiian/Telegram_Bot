from telegram import Update
from telegram.ext import ContextTypes
from services.task_service import list_tasks

async def list_tasks_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tasks = list_tasks(update.message.from_user.id)
    if tasks:
        msg = "\n".join([f"{i+1}. {t}" for i, t in enumerate(tasks)])
    else:
        msg = "У тебя нет задач."
    await update.message.reply_text(msg)
