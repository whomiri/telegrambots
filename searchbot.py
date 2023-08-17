#The bot searches from anywhere based on your question and sends a screenshot of the call
#Produced by github.com/whomiri, we are against copying and not giving credit when sharing.

from telethon.sync import TelegramClient, events
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time

api_id = 'API_ID'
api_hash = 'API_HASH'
bot_token = 'BOT_TOKEN'

# Starting the Chrome browser driver for Selenium
driver = webdriver.Chrome()

# Starting the Telegram client
client = TelegramClient('session_name', api_id, api_hash)
client.start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond("Hi! I'm a search bot. Example for use;\n'/google/yahoo/bing/duck/yandex query'...")
    raise events.StopPropagation

@client.on(events.NewMessage(pattern='/yahoo'))
async def search(event):
    query = ' '.join(event.raw_text.split()[1:])
    
    # Search yahoo
    driver.get(f'https://search.yahoo.com/search;_ylt=AwrhekUaAt5kjg8GmHpDDWVH;_ylc=X1MDMTE5NzgwNDg2NwRfcgMyBGZyAwRmcjIDcDpzLHY6c2ZwLG06c2ItdG9wBGdwcmlkAwRuX3JzbHQDMARuX3N1Z2cDMARvcmlnaW4Dc2VhcmNoLnlhaG9vLmNvbQRwb3MDMARwcXN0cgMEcHFzdHJsAzAEcXN0cmwDNQRxdWVyeQNzYWxhbQR0X3N0bXADMTY5MjI3MTE0MQ--?q={query}&fr=sfp&fr2=p%3As%2Cv%3Asfp%2Cm%3Asb-top&iscqry=')
    
    # Take screenshot
    screenshot_path = f'screenshot_{int(time.time())}.png'
    driver.save_screenshot(screenshot_path)
    
    # send screenshot via telegram
    await client.send_file(event.chat_id, screenshot_path, caption="Yahoo:\n" + query)
    
    raise events.StopPropagation

@client.on(events.NewMessage(pattern='/google'))
async def search(event):
    query = ' '.join(event.raw_text.split()[1:])
    
    driver.get(f'https://www.google.com/search?q={query}')
    
    screenshot_path = f'screenshot_{int(time.time())}.png'
    driver.save_screenshot(screenshot_path)

    await client.send_file(event.chat_id, screenshot_path, caption="Google:\n" + query)
    
    raise events.StopPropagation

@client.on(events.NewMessage(pattern='/bing'))
async def search(event):
    query = ' '.join(event.raw_text.split()[1:])

    driver.get(f'https://www.bing.com/search?q={query}&form=QBLH&sp=-1&ghc=1&lq=0&pq={query}&sc=10-7&qs=n&sk=&cvid=E711DCF7C6CF46F38CEB85C9282D5236&ghsh=0&ghacc=0&ghpl=')
    
    screenshot_path = f'screenshot_{int(time.time())}.png'
    driver.save_screenshot(screenshot_path)
    
    await client.send_file(event.chat_id, screenshot_path, caption="Bing:\n" + query)
    
    raise events.StopPropagation

@client.on(events.NewMessage(pattern='/duck'))
async def search(event):
    query = ' '.join(event.raw_text.split()[1:])
    
    driver.get(f'https://duckduckgo.com/?q={query}&ia=web')
    
    screenshot_path = f'screenshot_{int(time.time())}.png'
    driver.save_screenshot(screenshot_path)
    
    await client.send_file(event.chat_id, screenshot_path, caption="Duck:\n" + query)
    
    raise events.StopPropagation

#I do not recommend it because there is robot verification on yandex
@client.on(events.NewMessage(pattern='/yandex'))
async def search(event):
    query = ' '.join(event.raw_text.split()[1:])
    
    #Yandex not getting stuck on robot verification
    time.sleep(6)

    driver.get(f'https://yandex.com/search/?text={query}&lr=10253&search_source=yacom_desktop_common')
    
    screenshot_path = f'screenshot_{int(time.time())}.png'
    driver.save_screenshot(screenshot_path)
    
    await client.send_file(event.chat_id, screenshot_path, caption="Yandex:\n" + query)
    
    raise events.StopPropagation

# Starting and running the client
client.run_until_disconnected()

# Close Selenium browser driver
driver.quit()