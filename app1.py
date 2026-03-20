from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers import ask, image, help_cmd

TOKEN = "8701891106:AAEA_fDg9h2yjpDB-lXbE8ocN2DucH_Qj2Y"

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("ask", ask))
app.add_handler(CommandHandler("help", help_cmd))
app.add_handler(MessageHandler(filters.PHOTO, image))

app.run_polling()