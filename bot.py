import requests
from pyrogram import Client, filters
from pyrogram.types import Message

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
TOKEN = '6138768761:AAFYcz3WSRYloDvHPaTVNEiPX2nRjYsJ-sU'
API_BASE_URL = 'https://dalink.in/'  # Replace with your AdLinkFly website URL

# Helper function to make API requests to AdLinkFly
def adlinkfly_api_request(endpoint, params=None):
    url = API_BASE_URL + endpoint
    headers = {
        'Content-Type': 'application/json',
        'Authorization': '906573ff95ebd1c697ffd472ff9eadcd2e90f479',  # Replace with your AdLinkFly API token
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# Start command handler
@Client.on_message(filters.command(["start"]))
def start(_, message: Message):
    message.reply_text(
        "Welcome! I am your AdLinkFly account balance bot. "
        "Use /check_balance to see your account balance."
    )

# /check_balance command handler
@Client.on_message(filters.command(["check_balance"]))
def check_balance(_, message: Message):
    user_id = message.from_user.id

    # Here you can implement logic to retrieve the account balance from AdLinkFly API.
    # For this example, let's assume the balance is 100.
    balance = 100

    message.reply_text(f"Your account balance: {balance} credits.")

# Handler to handle unrecognized commands
@Client.on_message(~filters.command)
def unknown(_, message: Message):
    message.reply_text("Sorry, I didn't understand that command.")

def main():
    # Create and run the Pyrogram client
    app = Client("my_bot", bot_token=TOKEN)
    app.add_handler(start)
    app.add_handler(check_balance)
    app.add_handler(unknown)
    app.run()

if __name__ == '__main__':
    main()
    
