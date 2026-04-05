import asyncio

LOG_FILE = "data/logs.txt"

async def log_message(user_id, message):
    async with asyncio.Lock():
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"{user_id}: {message}\n")
