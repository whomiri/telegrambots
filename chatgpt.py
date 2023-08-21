#This bot uses the openai api to pull the responses from chatgpt and send them to you via tg
#current openai 3.5 gpt
from telethon.sync import TelegramClient, events
import openai

# Telethon
API_ID = 'API_ID'
API_HASH = 'API_HASH'
SESSION_NAME = 'SESSION_NAME'  # You can specify the session name as you wish.

# OpenAI API settings
OPENAI_API_KEY = 'OPENAI_API'

# Telethon client
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# OpenAI API
openai.api_key = OPENAI_API_KEY

# Function of sending messages with Telethon
@client.on(events.NewMessage)
async def handle_message(event):
    user_message = event.raw_text
    
    # Make API call to ask OpenAI questions
    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT-3.5 engine
        prompt=user_message,
        max_tokens=50  # Maximum length of response
    )
    
    # OpenAI incoming response
    ai_reply = response.choices[0].text.strip()
    
    # Send user OpenAI's response
    await event.reply(ai_reply)

def main():
    with client:
        client.run_until_disconnected()

if __name__ == '__main__':
    main()
