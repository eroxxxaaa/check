  // Function to send message
        function sendMessageToBot(chatId) {
            // Telegram Bot API endpoint for sending messages
            const apiUrl = 'https://api.telegram.org/bot7120814679:AAE_8z31_ZovejVsIsNp8S_MCyE2ppvZYlU/sendMessage';
            // Replace 'YOUR_BOT_TOKEN' with your actual bot token

            // Message payload with text and button
            const message = {
                chat_id: chatId,
                text: 'Hello from your JavaScript bot!',
                reply_markup: JSON.stringify({
                    inline_keyboard: [
                        [{ text: 'Open Another Bot', url: 'https://t.me/am_vbucks_bot/VBUCKSarm' }]
                    ]
                })
            };

            // Send message to the Telegram bot
            fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(message)
            })
            .then(response => {
                if (response.ok) {
                    console.log('Message sent successfully!');
                } else {
                    console.error('Failed to send message!');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }

        // Function to send message when the page loads
        function sendMessageOnLoad() {
            // Telegram Bot API endpoint for getting updates
            const apiUrl = 'https://api.telegram.org/bot7120814679:AAE_8z31_ZovejVsIsNp8S_MCyE2ppvZYlU/getUpdates';
            // Replace 'YOUR_BOT_TOKEN' with your actual bot token

            // Send request to get updates
            fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                // Check if there are any messages with "/start" command
                const messages = data.result.filter(msg => msg.message && msg.message.text && msg.message.text.trim() === '/start');

                // If there are messages with "/start" command
                if (messages.length > 0) {
                    // Extract chat ID from the first message
                    const chatId = messages[0].message.chat.id;
                    
                    // Send message to the Telegram bot
                    sendMessageToBot(chatId);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }

        // Call the function when the page loads
        window.onload = function() {
            // Send message when the page loads
            sendMessageOnLoad();
        };
