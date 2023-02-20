from telethon import TelegramClient, events, sync
import time

api_id = 21669282
api_hash = '296682a49e5d8a71a7e30a69cbffc78b'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

f = open("chats.txt", "r")
text = "#SegaGameClub - это игровое сообщество на основе P2E игр.\nНаш SegaToken децентрализован и уже торгуется на DEX PancakeSwap\nРаботает в собственной экосистеме на смартконтрактах и генерит до 210% прибыли в месяц, при помощи Стейкинга и P2E\nПереходи в наш Телеграм чат за подробностями: https://t.me/segagameclubchat"
chats= f.read().split('https://t.me/')
for chat in chats:
    if "@" not in chat:
        chat = "@"+chat.replace('\n','')
    try:
        client.send_file(chat, 'image.jpg',caption=text)
    except:
        print("invalid string")
    print(chat)
    time.sleep(60)
