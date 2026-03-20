import asyncio
import sys
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers import ask, image, help_cmd

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

TOKEN = "8701891106:AAEA_fDg9h2yjpDB-lXbE8ocN2DucH_Qj2Y"

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("ask", ask))
app.add_handler(CommandHandler("help", help_cmd))
app.add_handler(MessageHandler(filters.PHOTO, image))

app.run_polling(close_loop=False)