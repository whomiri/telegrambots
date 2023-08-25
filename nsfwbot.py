# this is a nsfw detector adapted to telegram
#It will tell you how many 18+% a media or any sticker is, then you can write code and use it as a group saver
# +18 bot detector

import os
import requests
from pyrogram import Client, filters, types
import logging 

logging.basicConfig(level=logging.INFO)

app = Client("Checker", api_id="API_ID", api_hash="API_HASH",
             bot_token="BOT_TOKEN")

name = "__main__"

# ---------------------------------- #

# ------------------------------------------------------ #
#AI_DE = sb(os.environ.get("CYBER_AI_DE", "False"))#
AI_KEY = "YOUR_AI_KEY"
#TAKE THIS FROM https://api.deepai.org/api/nsfw-detector
# ------------------------------------------------------ #

@app.on_message(filters.sticker | filters.photo)
async def deleter(client, message: types.Message):
    _info = await message.reply_text("I'm analyzing...")
    
    media = await message.download()

    r = requests.post(
        "https://api.deepai.org/api/nsfw-detector",
        files={
            "image": open(media, "rb"),
        },
        headers={"api-key": AI_KEY},
    )
    os.remove(media)
    if "status" in r.json():
        return await _info.edit_text(r.json()["status"])
    r_json = r.json()["output"]
    pic_id = r.json()["id"]
    percentage = r_json["nsfw_score"] * 100
    detections = r_json["detections"]
    link = f"https://api.deepai.org/job-view-file/{pic_id}/inputs/image.jpg"
    netice = f"<b>The media was calculated to be +18:</b>\n<a href='{link}'>>>></a> <code>{percentage:.3f}%</code>\n\n"
    if (percentage > 40):
        await message.delete()
    else:
        await _info.edit_text(netice)
         
if name == '__main__':
    app.run()
