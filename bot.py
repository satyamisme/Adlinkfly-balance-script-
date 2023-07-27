import requests
from pyrogram import Client, filters
from pyrogram.types import Message

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
TOKEN = '6138768761:AAFYcz3WSRYloDvHPaTVNEiPX2nRjYsJ-sU'
API_BASE_URL = 'https://dalink.in/'  # Replace with your AdLinkFly website URL

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with the API ID and API hash obtained from Telegram API website
API_ID =14505719
API_HASH = '620f0a2aa2cd1474a4953619b3e3643d'

# Replace 'YOUR_API_TOKEN' with the API token obtained from your AdLinkFly account settings
API_TOKEN = '906573ff95ebd1c697ffd472ff9eadcd2e90f479'

# Helper function to make API requests to AdLinkFly
def adlinkfly_api_request(endpoint, params=None):
    url = API_BASE_URL + endpoint
    headers = {
        'Content-Type': 'application/json',
        'Authorization': API_TOKEN,
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# Create the Pyrogram client
app = Client("my_bot", bot_token=TOKEN, api_id=API_ID, api_hash=API_HASH)

# Start command handler
@app.on_message(filters.command("start"))
def start(_, message: Message):
    message.reply_text(
        "Welcome! I am your AdLinkFly account balance bot. "
        "Use /check_balance to see your account balance."
    )

# /check_balance command handler
@app.on_message(filters.command("check_balance"))
def check_balance(_, message: Message):
    user_id = message.from_user.id

    # Retrieve the account balance from AdLinkFly API
    account_balance = get_account_balance(API_TOKEN)
    if account_balance is not None:
        message.reply_text(f"Your account balance: {account_balance} credits.")
    else:
        message.reply_text("Failed to retrieve account balance. Please try again later.")

# Handler to handle unrecognized commands
@app.on_message(~filters.command("start") & ~filters.command("check_balance"))
def unknown(_, message: Message):
    message.reply_text("Sorry, I didn't understand that command.")

# Function to get the account balance from AdLinkFly API
def get_account_balance(api_token):
    endpoint = '/api/v1/account/balance'
    url = API_BASE_URL + endpoint
    headers = {
        'Content-Type': 'application/json',
        'Authorization': api_token,
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['balance']
    else:
        print(f"Failed to retrieve account balance. Status code: {response.status_code}")
        return None

def main():
    # Start the Pyrogram client
    app.run()

if __name__ == '__main__':
    main()
    
