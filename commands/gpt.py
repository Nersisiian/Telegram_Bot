from telegram import Update
from telegram.ext import ContextTypes
from services.ai_service import gpt_chat

async def gpt_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("Напиши текст для ИИ.")
        return
    response = await gpt_chat(prompt)
    await update.message.reply_text(response)
