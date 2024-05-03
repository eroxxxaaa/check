import requests
import json

# Function to send message
def send_message_to_bot(chat_id):
    # Telegram Bot API endpoint for sending messages
    api_url = 'https://api.telegram.org/bot7120814679:AAE_8z31_ZovejVsIsNp8S_MCyE2ppvZYlU/sendMessage'
    # Replace '<YOUR_BOT_TOKEN>' with your actual bot token

    # Message payload with text and button
    message = {
        'chat_id': chat_id,
        'text': 'Hello from your Python bot!',
        'reply_markup': json.dumps({
            'inline_keyboard': [
                [{'text': 'Open Another Bot', 'url': 'https://t.me/am_vbucks_bot/VBUCKSarm'}]
            ]
        })
    }

    # Send message to the Telegram bot
    response = requests.post(api_url, json=message)
    if response.ok:
        print('Message sent successfully!')
    else:
        print('Failed to send message!')
        print('Response:', response.text)

# Function to send message when the script runs
def send_message_on_run():
    # Telegram Bot API endpoint for getting updates
    api_url = 'https://api.telegram.org/bot7120814679:AAE_8z31_ZovejVsIsNp8S_MCyE2ppvZYlU/getUpdates'
    # Replace '<YOUR_BOT_TOKEN>' with your actual bot token

    # Send request to get updates
    response = requests.get(api_url)
    if response.ok:
        data = response.json()

        # Check if there are any messages with "/start" command
        messages = [msg for msg in data.get('result', []) if msg.get('message') and msg['message'].get('text') and msg['message']['text'].strip() == '/start']

        # If there are messages with "/start" command
        if messages:
            # Extract chat ID from the first message
            chat_id = messages[0]['message']['chat']['id']
            
            # Send message to the Telegram bot
            send_message_to_bot(chat_id)
    else:
        print('Failed to fetch updates!')
        print('Response:', response.text)

# Call the function when the script runs
if __name__ == "__main__":
    # Send message when the script runs
    send_message_on_run()
