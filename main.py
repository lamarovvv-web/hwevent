import discord
import asyncio
from aiogram import Bot, Dispatcher, types

# ТВОИ ДАННЫЕ
DS_TOKEN = 'MTQ4NjczNTgxNTAzMDg3MDE4Nw.GiEvOB.2doZprTi6TDcd2qmF91gvU0KmpiVxa_dWKPnVg'
DS_CHANNEL_ID = 1484544347172245635 
TG_TOKEN = '8169376952:AAF4wO3HM3MyqEeog_5qVKVubpNChlMiy-I'

bot = Bot(token=TG_TOKEN)
dp = Dispatcher()
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@dp.message()
async def handle(message: types.Message):
    ch = client.get_channel(DS_CHANNEL_ID)
    if ch:
        await ch.send(f"📢 **Ивент:**\n{message.text or message.caption}")
        print("✅ Улетело в ДС!")

async def main():
    # Запускаем Дискорд
    asyncio.create_task(client.start(DS_TOKEN))
    print("📡 Дискорд запущен...")
    # Запускаем Телеграм
    print("🤖 Телеграм запущен... Жду сообщений!")
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print("🧨 Ошибка связи. Попробуй включить GoodbyeDPI или раздать 4G.")
