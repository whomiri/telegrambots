#The bot searches from anywhere based on your question and sends a screenshot of the call or send only screenshot
#Produced by github.com/whomiri, we are against copying and not giving credit when sharing.

from telethon.sync import TelegramClient, events
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time

api_id = 'API-ID'
api_hash = 'API-HASH'
bot_token = 'BOT-TOKEN'

# Starting the Chrome browser driver for Selenium
driver = webdriver.Chrome()

# Starting the Telegram client
client = TelegramClient('session_name', api_id, api_hash)
client.start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond("Hi! I'm a search bot. Example for use;\n'/google/yahoo/bing/duck/yandex query'\n\nor '/screenshot https://yourrequest.com'..")
    raise events.StopPropagation

@client.on(events.NewMessage(pattern='/yahoo'))
async def search(event):
    query = ' '.join(event.raw_text.split()[1:])
    await event.respond("Please wait...")

    # Search yahoo
    driver.get(f'https://search.yahoo.com/search?q={query}')
    
    # Take screenshot
    screenshot_path = f'screenshot_{int(time.time())}.png'
    driver.save_screenshot(screenshot_path)
    
    # send screenshot via telegram
    await client.send_file(event.chat_id, screenshot_path, caption="Yahoo:\n" + query)
    
    raise events.StopPropagation

@client.on(events.NewMessage(pattern='/google'))
async def search(event):
    query = ' '.join(event.raw_text.split()[1:])
    await event.respond("Please wait...")
    
    driver.get(f'https://www.google.com/search?q={query}')
    
    screenshot_path = f'screenshot_{int(time.time())}.png'
    driver.save_screenshot(screenshot_path)

    await client.send_file(event.chat_id, screenshot_path, caption="Google:\n" + query)
    
    raise events.StopPropagation

@client.on(events.NewMessage(pattern='/bing'))
async def search(event):
    query = ' '.join(event.raw_text.split()[1:])
    await event.respond("Please wait...")

    driver.get(f'https://www.bing.com/search?q={query}')
    
    screenshot_path = f'screenshot_{int(time.time())}.png'
    driver.save_screenshot(screenshot_path)
    
    await client.send_file(event.chat_id, screenshot_path, caption="Bing:\n" + query)
    
    raise events.StopPropagation

@client.on(events.NewMessage(pattern='/duck'))
async def search(event):
    query = ' '.join(event.raw_text.split()[1:])
    await event.respond("Please wait...")
    
    driver.get(f'https://duckduckgo.com/?q={query}&ia=web')
    
    screenshot_path = f'screenshot_{int(time.time())}.png'
    driver.save_screenshot(screenshot_path)
    
    await client.send_file(event.chat_id, screenshot_path, caption="Duck:\n" + query)
    
    raise events.StopPropagation

#I do not recommend it because there is robot verification on yandex
@client.on(events.NewMessage(pattern='/youtube'))
async def search(event):
    query = ' '.join(event.raw_text.split()[1:])
    await event.respond("Please wait...")
    
    time.sleep(2)

    driver.get(f'https://www.youtube.com/results?search_query={query}')
    
    screenshot_path = f'screenshot_{int(time.time())}.png'
    driver.save_screenshot(screenshot_path)
    
    await client.send_file(event.chat_id, screenshot_path, caption="Youtube:\n" + query)
    
    raise events.StopPropagation

@client.on(events.NewMessage(pattern='/screenshot'))
async def search(event):
    query = ' '.join(event.raw_text.split()[1:])
    await event.respond("Please wait...")

    time.sleep(4)

    driver.get(query)
    
    screenshot_path = f'screenshot_{int(time.time())}.png'
    driver.save_screenshot(screenshot_path)
    
    await client.send_file(event.chat_id, screenshot_path, caption="Screenshot:\n" + query)
    
    raise events.StopPropagation

# Starting and running the client
client.run_until_disconnected()

# Close Selenium browser driver
driver.quit()
