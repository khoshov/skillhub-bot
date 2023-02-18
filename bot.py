from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from loguru import logger


logger.add("bot.log")

TOKEN = "6108514561:AAGvBLqtk00H6ISbHngwVo4R1qPokP9iQp8"


def greet_user(update, context):
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')


def talk_to_me(update, context):
    user_text = update.message.text
    logger.info(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(TOKEN, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logger.info("Бот стартовал")

    mybot.start_polling()
    mybot.idle()


main()
