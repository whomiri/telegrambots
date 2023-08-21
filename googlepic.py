from telethon.sync import TelegramClient, events
from google_images_search import GoogleImagesSearch

# Telegram API 
API_ID = 'API_ID'
API_HASH = 'API_HASH'
BOT_TOKEN = 'BOT_TOKEN'

# Google API
GCS_DEVELOPER_KEY = 'GOOGLE_API_KEY'
GCS_CX = 'GOOGLE_CX_NUM'

# Telegram client
client = TelegramClient('bot_session', API_ID, API_HASH)

# /start 
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply("Hi! Send me pic.")

# Pic func
@client.on(events.NewMessage(func=lambda e: e.photo))
async def photo_received(event):
    # download pic tg
    photo = await event.download_media()
    
    # Google Images Search
    gis = GoogleImagesSearch(GCS_DEVELOPER_KEY, GCS_CX)
    gis.search({'q': photo})  # search pic
    
    if gis.results():
        first_result = gis.results()[0]
        await event.reply("Search: {}".format(first_result.url))
    else:
        await event.reply("Üzgünüm, arama sonuçları bulunamadı.")

def main():
    with client:
        client.run_until_disconnected()

if __name__ == '__main__':
    main()
