from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

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

@app.route('/')
def index():
    # Get chat ID from query parameter
    chat_id = request.args.get('chat_id')
    if chat_id:
        send_message_to_bot(chat_id)
        return 'Message sent successfully!'
    else:
        return 'Please provide a chat_id parameter.'

if __name__ == '__main__':
    app.run(debug=True)
