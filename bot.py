from telegram.ext import ApplicationBuilder, CommandHandler
from config import BOT_TOKEN
from commands.start import start
from commands.help import help_command
from commands.add_task import add_task_command
from commands.list_tasks import list_tasks_command
from commands.del_task import del_task_command
from commands.gpt import gpt_command
from commands.img import img_command
import asyncio
from utils.logger import log_message
from telegram.ext import MessageHandler, filters

async def handle_message(update, context):
    await log_message(update.message.from_user.id, update.message.text)
    await update.message.reply_text("Я получил твоё сообщение!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("add_task", add_task_command))
    app.add_handler(CommandHandler("tasks", list_tasks_command))
    app.add_handler(CommandHandler("del_task", del_task_command))
    app.add_handler(CommandHandler("gpt", gpt_command))
    app.add_handler(CommandHandler("img", img_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен 🚀")
    asyncio.run(app.run_polling())
