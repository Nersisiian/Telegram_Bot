from telegram import Update
from telegram.ext import ContextTypes
from services.task_service import delete_task

async def del_task_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Укажи номер задачи для удаления.")
        return
    index = int(context.args[0]) - 1
    if delete_task(update.message.from_user.id, index):
        await update.message.reply_text("Задача удалена ✅")
    else:
        await update.message.reply_text("Не удалось удалить задачу.")
