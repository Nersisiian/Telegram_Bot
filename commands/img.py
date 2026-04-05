from telegram import Update
from telegram.ext import ContextTypes
from services.ai_service import generate_image

async def img_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("Напиши описание картинки.")
        return
    url = await generate_image(prompt)
    await update.message.reply_photo(url)
