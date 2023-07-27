import requests
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
TOKEN = '6138768761:AAFYcz3WSRYloDvHPaTVNEiPX2nRjYsJ-sU'
API_BASE_URL = 'https://dalink.in/'  # Replace with your AdLinkFly website URL

# Telegram bot conversation states
CHECK_BALANCE = 1

# Helper function to make API requests to AdLinkFly
def adlinkfly_api_request(endpoint, params=None):
    url = API_BASE_URL + endpoint
    headers = {
        'Content-Type': 'application/json',
        'Authorization': '906573ff95ebd1c697ffd472ff9eadcd2e90f479',  # Replace with your AdLinkFly API token
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# /start command handler
def start(update: Update, _: CallbackContext):
    update.message.reply_text(
        "Welcome! I am your AdLinkFly account balance bot. "
        "Use /check_balance to see your account balance."
    )

# /check_balance command handler
def check_balance(update: Update, _: CallbackContext):
    user_id = update.effective_user.id
    # Here you can implement logic to retrieve the account balance from AdLinkFly API.
    # For this example, let's assume the balance is 100.
    balance = 100

    update.message.reply_text(f"Your account balance: {balance} credits.")

# Handler to handle unrecognized commands
def unknown(update: Update, _: CallbackContext):
    update.message.reply_text("Sorry, I didn't understand that command.")

def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("check_balance", check_balance))

    # Handler for unrecognized commands
    dp.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
