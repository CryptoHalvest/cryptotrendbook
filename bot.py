import logging
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Telegram Bot Token
TOKEN = "7678922849:AAHd2USbACN4UBsxC3y4j9Gn5oGRKn0KOyxsPKLy8To"
# Replace this with your actual token

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Example fake data (later connect with real APIs if needed)
def get_crypto_trends():
    return {
        "country": "Bangladesh",
        "ebooks": ["Beginner’s Guide to Crypto", "Crypto Investing 2025"],
        "websites": ["Udemy", "Gumroad", "Amazon Kindle"],
        "interest_age": "18-35 years"
    }

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to Cryptotrendbook bot! Use /courses to get trending crypto courses.")

def courses(update: Update, context: CallbackContext) -> None:
    data = get_crypto_trends()
    message = (
        f"Trending in {data['country']}:\n"
        f"Popular eBooks/Courses: {', '.join(data['ebooks'])}\n"
        f"Websites: {', '.join(data['websites'])}\n"
        f"Age Group Interested: {data['interest_age']}\n\n"
        f"(This is sample data. Real data integration coming soon.)"
    )
    update.message.reply_text(message)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("courses", courses))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
