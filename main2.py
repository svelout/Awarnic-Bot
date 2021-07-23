import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='-', intents = intents)

@bot.event
async def on_ready():
    print("O")
  
@bot.event
async def on_member_join(member):
    owner = bot.get_user(417714443884167177)
    owner2 = bot.get_user(414457409269137408)
    if member.bot:
          await member.ban()
          await owner.send(f"\aВнимание на сервер был добавлен бот по имени `{member.name}`!\n Из-за этого сработала система bramerto_Anti-Crash\n Продолжайте следить за сервером, а в случае опасности я вас спасу:)\n 🤟 ")
          await owner2.send(
              f"\aВнимание на сервер был добавлен бот по имени `{member.name}`!\n Из-за этого сработала система bramerto_Anti-Crash\n Продолжайте следить за сервером, а в случае опасности я вас спасу:)\n 🤟 ")
    else:
          print("New member has joined!")

bot.run("Nzc2NTMxOTc4OTcxMTE5NjQ2.X62Pww.DjzozDijWdnr_-56NMSY9h8lbeY")
