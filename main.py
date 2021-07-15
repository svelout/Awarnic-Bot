import random
from random import choice
import sqlite3
from typing import Optional
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from random import seed
from random import random
from random import randint

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='=', intents = intents)
status =

colours = {
    "✅": 832332996253319188
}

@bot.event
async def on_ready():
    db = sqlite3.connect('db.sqlite')
    cursor = db.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS main(
        admin1 TEXT,
        banned_count_members TEXT,
        message_id TEXT
        )
        ''')
    guild = discord.Guild
    servers = len(bot.guilds)
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1

    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=str(f"на {members} участников")))
    print("Бот начал работать")

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

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx,member,message, *,reason=None):
    if message.content.startswith("=ban"):
        db = sqlite3.connect('db.sqlite')
        cursor = db.cursor()
        banned_member_count = cursor.execute(f"SELECT banned_member_count FROM main WHERE admin1 = {ctx.message.author.id}")
        if banned_member_count < 2:
            await member.ban(reason=reason)
            await ctx.send("Успешно!")
        elif banned_member_count == 2:
            return await ctx.send("У вас ограничение по бану")

@bot.command(name='invite')
async def on_message(ctx):
    one = randint(1, 9)
    two = randint(1, 9)
    three = randint(1, 9)
    four = randint(1, 9)
    five = randint(1, 9)
    six = randint(1, 9)
    seven = randint(1, 9)
    eight = randint(1, 9)
    nine = randint(1, 9)
    ten = randint(1, 9)
    eleven = randint(1, 9)
    twelve = randint(1, 9)
    thirteen = randint(1, 9)
    fourteen = randint(1, 9)
    fifteen = randint(1, 9)
    sixteen = randint(1, 9)
    seventeen = randint(1, 9)
    eightteen = randint(1, 9)
    id = f"{one}{two}{three}{four}{five}{six}{seven}{eight}{nine}{ten}{eleven}{twelve}{thirteen}{fourteen}{fifteen}{sixteen}{seventeen}{eightteen}"
    dm = bot.get_user(id)
    member = ctx.author
    owner = bot.get_user(417714443884167177)
    try:
        await dm.send(
    '''
    ˚˳⊹・✦✗⋆ Приветствую на :fire:AWARNIC:fire:  ✦・˚˳⊹
꒦꒷︶˚︶˚︶˚꒷꒦꒷꒷꒦꒷꒦꒷︶˚︶꒦꒷꒷˚꒷︶˚︶˚︶˚꒷꒦꒷꒷꒦꒷꒷
                      ❃๑ ════════════════ ๑❃
       ˚˳⊹・●:heart:           Тут ты можешь:             :heart:●˚˳⊹・
⁣                      ❃๑ ════════════════ ๑❃
╭────────────────────────────
╰─► ・˚˳⊹ Заводить новых друзей!
⁣⁣             ⁣・˚˳⊹ Общаться с новыми друзьями!
⁣⁣             ⁣・˚˳⊹ Играть в разные крутые игры!
⁣⁣             ⁣・˚˳⊹ Подать заявку на Модераторов!
⁣⁣             ⁣・˚˳⊹ Слушать крутую музыку!
⁣⁣             ⁣・˚˳⊹ Побеждай в конкурсах!
⁣⁣             ⁣・˚˳⊹ Выйгрывай призы!
⁣⁣             ⁣・˚˳⊹ Поспамить!
⁣⁣             ⁣・˚˳⊹ Отдохнуть за просмотром видео!
⁣⁣             ⁣・˚˳⊹ Стать партнёром сервера!
╭─►・˚˳⊹ Поделиться своими мемами!
╰────────────────────────────
                      ❃๑ ════════════════ ๑❃
     ˚˳⊹・●:heart:        ОСТАЛЬНОЕ О СЕРВЕРЕ     :heart:●˚˳⊹・
⁣                      ❃๑ ════════════════ ๑❃
●▬▬▬▬▬▬▬▬▬▬▬▬▢▬▬▬▬▬▬▬▬▬▬▬▬●
│ ✓ Адекватная администрация
│ ✓ Красивое оформление
│ ✓ Понятное правило
│ ✓ Общительное комьюнити 
│ ✓ Хорошие боты
●▬▬▬▬▬▬▬▬▬▬▬▬▢▬▬▬▬▬▬▬▬▬▬▬▬●
                      ❃๑ ════════════════ ๑❃
       ˚˳⊹・●:heart:             ПОЛЕЗНОЕ             :heart:●˚˳⊹・
⁣                      ❃๑ ════════════════ ๑❃
|▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬|
⁣⁣             ⁣・˚˳⊹ Ютуб - AWARNIC YT
|▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬|
┍──────────────────────────────────
 │︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾
 │────────────────────────────────── 
┣・。〔Дискорд〕・。 - https://discord.gg/C94Kb7ygR7
 │──────────────────────────────────
┣・。〔Ютуб〕・。 - https://www.youtube.com/channel/UCxwdrF0iLwTyAwvZkmljc0w?view_as=subscriber
 │──────────────────────────────────
┣・。〔Пинг〕・。 - @everyone  @here
    '''
)
        await ctx.send("Приглашение было успешно отправлено!")
        await owner.send("Приглашение отправлено!")
    except:
        await ctx.send(f"Походу айди пользователя сгенерировался неверно, кстати вот он {id}\nПоэтому не удалось отправить сообщение\nПопробуйте еще раз")





@bot.command(name='test')
@commands.has_permissions(manage_roles=True)
async def on_message(ctx):
    Moj1p =  '🖥️'
    Moj2p = '📼'
    Moj3p = '🥽'
    Moj4p = '📱'
    Moj5p = '🕹️'
    Moj6p = '🎥'
    Mojg = '🧯'
    Moj2g = '🔦'
    Moj3g = '⛏️'
    Moj4g = '🧰'
    Moj5g = '💰'
    Moj6g = '🧱'
    Moj7g = '🔫'
    Moj8g = '🧲'
    Moj9g = '💣'
    Moj10g = '🔋'
    Mojz = '♈'
    Mojz2 = '♉'
    Mojz3 = '♊'
    Mojz4 = '♋'
    Mojz5 = '♍'
    Mojz6 = '♌'
    Mojz7 = '♎'
    Mojz8 = '♏'
    Mojz9 = '♐'
    Mojz10 = '♑'
    Mojz11 = '♒'
    Mojz12 = '♓'
    Moja = '🔵'
    Moja2 = '🔴'
    Moja3 = '🟢'
    Moja4 = '🟡'
    Moja5 = '🟠'
    Mojp = '🧍‍♀️'
    Mojp2 = '🧍‍♂️'
    embed = discord.Embed(title="┌────▻ПЛАТФОРМА◅────┐", description="Здесь вы можете выбрать платформу", color=0xFF5733)
    embed.add_field(name="PC", value=Moj1p, inline=False)
    embed.add_field(name="Xbox", value=Moj2p, inline=False)
    embed.add_field(name="VReality", value=Moj3p, inline=False)
    embed.add_field(name="Mobile", value=Moj4p, inline=False)
    embed.add_field(name="Nintendo", value=Moj5p, inline=False)
    embed.add_field(name="PlayStation", value=Moj6p, inline=False)
    #Channel = discord.utils.get(ctx.guild.channels, id=831949714236244069)
    #Text = "YOUR_MESSAGE_HERE"
    Moji = await ctx.send(embed=embed)

    await Moji.add_reaction(Moj1p)
    await Moji.add_reaction(Moj2p)
    await Moji.add_reaction(Moj3p)
    await Moji.add_reaction(Moj4p)
    await Moji.add_reaction(Moj5p)
    await Moji.add_reaction(Moj6p)

    embed1 = discord.Embed(title="┌──────▻ВОЗРАСТ◅─────┐", description='Выберите роль со своим возрастом', color=0xFF5733)
    embed1.add_field(name='5-10', value=Moja, inline=False)
    embed1.add_field(name='10-15', value=Moja2, inline=False)
    embed1.add_field(name='15-18', value=Moja3, inline=False)
    embed1.add_field(name='18-25', value=Moja4, inline=False)
    embed1.add_field(name='25-60', value=Moja5, inline=False)

    Moji2 = await ctx.send(embed=embed1)
    await Moji2.add_reaction(Moja)
    await Moji2.add_reaction(Moja2)
    await Moji2.add_reaction(Moja3)
    await Moji2.add_reaction(Moja4)
    await Moji2.add_reaction(Moja5)

    embed2 = discord.Embed(title='┌───────▻ИГРЫ◅───────┐', description='Выберите роли с играми\n в которые вы играите',  color=0xFF5733)
    embed2.add_field(name='Roblox', value=Mojg, inline=False)
    embed2.add_field(name='Among Us', value=Moj2g, inline=False)
    embed2.add_field(name='Minecraft', value=Moj3g, inline=False)
    embed2.add_field(name='Dota 2', value=Moj4g, inline=False)
    embed2.add_field(name='GTA V', value=Moj5g, inline=False)
    embed2.add_field(name='Fortnite', value=Moj6g, inline=False)
    embed2.add_field(name='CS:GO', value=Moj7g, inline=False)
    embed2.add_field(name='Overwatch', value=Moj8g, inline=False)
    embed2.add_field(name='NEXTRP', value=Moj9g, inline=False)
    embed2.add_field(name='Другие игры', value=Moj10g, inline=False)

    Moji3 = await ctx.send(embed=embed2)
    await Moji3.add_reaction(Mojg)
    await Moji3.add_reaction(Moj2g)
    await Moji3.add_reaction(Moj3g)
    await Moji3.add_reaction(Moj4g)
    await Moji3.add_reaction(Moj5g)
    await Moji3.add_reaction(Moj6g)
    await Moji3.add_reaction(Moj7g)
    await Moji3.add_reaction(Moj8g)
    await Moji3.add_reaction(Moj9g)
    await Moji3.add_reaction(Moj10g)

    embed3 = discord.Embed(title='┌───────▻ЗОДИАК◅──────┐', description='Выберите роль со своим знаком зодиаком',  color=0xFF5733)
    embed3.add_field(name='Овен', value=Mojz, inline=False)
    embed3.add_field(name='Телец', value=Mojz2, inline=False)
    embed3.add_field(name='Близнецы', value=Mojz3, inline=False)
    embed3.add_field(name='Рак', value=Mojz4, inline=False)
    embed3.add_field(name='Дева', value=Mojz5, inline=False)
    embed3.add_field(name='Лев', value=Mojz6, inline=False)
    embed3.add_field(name='Весы', value=Mojz7, inline=False)
    embed3.add_field(name='Скорпион', value=Mojz8, inline=False)
    embed3.add_field(name='Стрелец', value=Mojz9, inline=False)
    embed3.add_field(name='Козерог', value=Mojz10, inline=False)
    embed3.add_field(name='Водолей', value=Mojz11, inline=False)
    embed3.add_field(name='Рыбы', value=Mojz12, inline=False)

    Moji4 = await ctx.send(embed=embed3)
    await Moji4.add_reaction(Mojz)
    await Moji4.add_reaction(Mojz2)
    await Moji4.add_reaction(Mojz3)
    await Moji4.add_reaction(Mojz4)
    await Moji4.add_reaction(Mojz5)
    await Moji4.add_reaction(Mojz6)
    await Moji4.add_reaction(Mojz7)
    await Moji4.add_reaction(Mojz8)
    await Moji4.add_reaction(Mojz9)
    await Moji4.add_reaction(Mojz10)
    await Moji4.add_reaction(Mojz11)
    await Moji4.add_reaction(Mojz12)


@bot.command(name='test2')
async def on_message(ctx):
    Mojp = '🧍‍♀️'
    Mojp2 = '🧍‍♂️'
    embed4 = discord.Embed(title='┌───────▻ПОЛ◅───────┐', description='Выберите роли с вашим полом', color=0xFF5733)
    embed4.add_field(name='Девочка', value=Mojp, inline=False)
    embed4.add_field(name='Мальчик', value=Mojp2, inline=False)

    Moji5 = await ctx.send(embed=embed4)
    await Moji5.add_reaction(Mojp)
    await Moji5.add_reaction(Mojp2)

@bot.event
async def on_raw_reaction_add(payload):
    Moj1p = '🖥️'
    Moj2p = '📼'
    Moj3p = '🥽'
    Moj4p = '📱'
    Moj5p = '🕹️'
    Moj6p = '🎥'
    Mojg = '🧯'
    Moj2g = '🔦'
    Moj3g = '⛏️'
    Moj4g = '🧰'
    Moj5g = '💰'
    Moj6g = '🧱'
    Moj7g = '🔫'
    Moj8g = '🧲'
    Moj9g = '💣'
    Moj10g = '🔋'
    Mojz = '♈'
    Mojz2 = '♉'
    Mojz3 = '♊'
    Mojz4 = '♋'
    Mojz5 = '♍'
    Mojz6 = '♌'
    Mojz7 = '♎'
    Mojz8 = '♏'
    Mojz9 = '♐'
    Mojz10 = '♑'
    Mojz11 = '♒'
    Mojz12 = '♓'
    Moja = '🔵'
    Moja2 = '🔴'
    Moja3 = '🟢'
    Moja4 = '🟡'
    Moja5 = '🟠'
    Mojp = '🧍‍♀️'
    Mojp2 = '🧍‍♂️'
    message1 = 835234956929531955
    message2 = 835234967940104232
    message3 = 835234976979091476
    message4 = 835234998142369802
    message5 = 835235026643582977

    if message1 == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == Moj1p:
            role = discord.utils.get(guild.roles, id=767457369675530240)
        elif emoji == Moj2p:
            role = discord.utils.get(guild.roles, id=767457389150470144)
        elif emoji == Moj3p:
            role = discord.utils.get(guild.roles, id=767457390877474847)
        elif emoji == Moj4p:
            role = discord.utils.get(guild.roles, id=767457374591909908)
        elif emoji == Moj5p:
            role = discord.utils.get(guild.roles, id=767457385353838622)
        elif emoji == Moj6p:
            role = discord.utils.get(guild.roles, id=767457382959153192)
        await member.add_roles(role)

    if message2 == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == Moja:
            role = discord.utils.get(guild.roles, id=767457913294946355)
        elif emoji == Moja2:
            role = discord.utils.get(guild.roles, id=767457916445130772)
        elif emoji == Moja3:
            role = discord.utils.get(guild.roles, id=767457918965907646)
        elif emoji == Moja4:
            role = discord.utils.get(guild.roles, id=767457921029242910)
        elif emoji == Moja5:
            role = discord.utils.get(guild.roles, id=767457922195390496)
        await member.add_roles(role)

    if message3 == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == Mojg:
            role = discord.utils.get(guild.roles, id=767458116446322689)
        elif emoji == Moj2g:
            role = discord.utils.get(guild.roles, id=767458115029303317)
        elif emoji == Moj3g:
            role = discord.utils.get(guild.roles, id=767458113976533012)
        elif emoji == Moj4g:
            role = discord.utils.get(guild.roles, id=767458118091014166)
        elif emoji == Moj5g:
            role = discord.utils.get(guild.roles, id=767458119239729153)
        elif emoji == Moj6g:
            role = discord.utils.get(guild.roles, id=767458121777807371)
        elif emoji == Moj7g:
            role = discord.utils.get(guild.roles, id=767458121969827870)
        elif emoji == Moj8g:
            role = discord.utils.get(guild.roles, id=767458123749130250)
        elif emoji == Moj9g:
            role = discord.utils.get(guild.roles, id=767458125044645898)
        elif emoji == Moj10g:
            role = discord.utils.get(guild.roles, id=767458126500331550)
        await member.add_roles(role)

    if message4 == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == Mojz:
            role = discord.utils.get(guild.roles, id=767458830430109696)
        elif emoji == Mojz2:
            role = discord.utils.get(guild.roles, id=767458832221339718)
        elif emoji == Mojz3:
            role = discord.utils.get(guild.roles, id=767458833538613278)
        elif emoji == Mojz4:
            role = discord.utils.get(guild.roles, id=767458834822201417)
        elif emoji == Mojz5:
            role = discord.utils.get(guild.roles, id=767458835945619486)
        elif emoji == Mojz6:
            role = discord.utils.get(guild.roles, id=767458837295923230)
        elif emoji == Mojz7:
            role = discord.utils.get(guild.roles, id=767458838608871454)
        elif emoji == Mojz8:
            role = discord.utils.get(guild.roles, id=767458839985258538)
        elif emoji == Mojz9:
            role = discord.utils.get(guild.roles, id=767458840781914183)
        elif emoji == Mojz10:
            role = discord.utils.get(guild.roles, id=767458841704923147)
        elif emoji == Mojz11:
            role = discord.utils.get(guild.roles, id=767458843230732319)
        elif emoji == Mojz12:
            role = discord.utils.get(guild.roles, id=767458844702933022)
        await member.add_roles(role)

    if message5 == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == Mojp:
            role = discord.utils.get(guild.roles, id=767459216323117077)
        elif emoji == Mojp2:
            role = discord.utils.get(guild.roles, id=767459217920622692)
        await member.add_roles(role)


@bot.event
async def on_raw_reaction_remove(payload):
    Moj1p = '🖥️'
    Moj2p = '📼'
    Moj3p = '🥽'
    Moj4p = '📱'
    Moj5p = '🕹️'
    Moj6p = '🎥'
    Mojg = '🧯'
    Moj2g = '🔦'
    Moj3g = '⛏️'
    Moj4g = '🧰'
    Moj5g = '💰'
    Moj6g = '🧱'
    Moj7g = '🔫'
    Moj8g = '🧲'
    Moj9g = '💣'
    Moj10g = '🔋'
    Mojz = '♈'
    Mojz2 = '♉'
    Mojz3 = '♊'
    Mojz4 = '♋'
    Mojz5 = '♍'
    Mojz6 = '♌'
    Mojz7 = '♎'
    Mojz8 = '♏'
    Mojz9 = '♐'
    Mojz10 = '♑'
    Mojz11 = '♒'
    Mojz12 = '♓'
    Moja = '🔵'
    Moja2 = '🔴'
    Moja3 = '🟢'
    Moja4 = '🟡'
    Moja5 = '🟠'
    Mojp = '🧍‍♀️'
    Mojp2 = '🧍‍♂️'
    message1 = 835234956929531955
    message2 = 835234967940104232
    message3 = 835234976979091476
    message4 = 835234998142369802
    message5 = 835235026643582977

    if message1 == payload.message_id:
        member = payload.member
        guild = bot.get_guild(765315456415432704)

        emoji = payload.emoji.name
        if emoji == Moj1p:
            role = discord.utils.get(guild.roles, id=767457369675530240)
        elif emoji == Moj2p:
            role = discord.utils.get(guild.roles, id=767457389150470144)
        elif emoji == Moj3p:
            role = discord.utils.get(guild.roles, id=767457390877474847)
        elif emoji == Moj4p:
            role = discord.utils.get(guild.roles, id=767457374591909908)
        elif emoji == Moj5p:
            role = discord.utils.get(guild.roles, id=767457385353838622)
        elif emoji == Moj6p:
            role = discord.utils.get(guild.roles, id=767457382959153192)
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
           await member.remove_roles(role)

    if message2 == payload.message_id:
        member = payload.member
        guild = bot.get_guild(765315456415432704)

        emoji = payload.emoji.name
        if emoji == Moja:
            role = discord.utils.get(guild.roles, id=767457913294946355)
        elif emoji == Moja2:
            role = discord.utils.get(guild.roles, id=767457916445130772)
        elif emoji == Moja3:
            role = discord.utils.get(guild.roles, id=767457918965907646)
        elif emoji == Moja4:
            role = discord.utils.get(guild.roles, id=767457921029242910)
        elif emoji == Moja5:
            role = discord.utils.get(guild.roles, id=767457922195390496)
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)

    if message3 == payload.message_id:
        member = payload.member
        guild = bot.get_guild(765315456415432704)

        emoji = payload.emoji.name
        if emoji == Mojg:
            role = discord.utils.get(guild.roles, id=767458116446322689)
        elif emoji == Moj2g:
            role = discord.utils.get(guild.roles, id=767458115029303317)
        elif emoji == Moj3g:
            role = discord.utils.get(guild.roles, id=767458113976533012)
        elif emoji == Moj4g:
            role = discord.utils.get(guild.roles, id=767458118091014166)
        elif emoji == Moj5g:
            role = discord.utils.get(guild.roles, id=767458119239729153)
        elif emoji == Moj6g:
            role = discord.utils.get(guild.roles, id=767458121777807371)
        elif emoji == Moj7g:
            role = discord.utils.get(guild.roles, id=767458121969827870)
        elif emoji == Moj8g:
            role = discord.utils.get(guild.roles, id=767458123749130250)
        elif emoji == Moj9g:
            role = discord.utils.get(guild.roles, id=767458125044645898)
        elif emoji == Moj10g:
            role = discord.utils.get(guild.roles, id=767458126500331550)
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)

    if message4 == payload.message_id:
        member = payload.member
        guild = bot.get_guild(765315456415432704)

        emoji = payload.emoji.name
        if emoji == Mojz:
            role = discord.utils.get(guild.roles, id=767458830430109696)
        elif emoji == Mojz2:
            role = discord.utils.get(guild.roles, id=767458832221339718)
        elif emoji == Mojz3:
            role = discord.utils.get(guild.roles, id=767458833538613278)
        elif emoji == Mojz4:
            role = discord.utils.get(guild.roles, id=767458834822201417)
        elif emoji == Mojz5:
            role = discord.utils.get(guild.roles, id=767458835945619486)
        elif emoji == Mojz6:
            role = discord.utils.get(guild.roles, id=767458837295923230)
        elif emoji == Mojz7:
            role = discord.utils.get(guild.roles, id=767458838608871454)
        elif emoji == Mojz8:
            role = discord.utils.get(guild.roles, id=767458839985258538)
        elif emoji == Mojz9:
            role = discord.utils.get(guild.roles, id=767458840781914183)
        elif emoji == Mojz10:
            role = discord.utils.get(guild.roles, id=767458841704923147)
        elif emoji == Mojz11:
            role = discord.utils.get(guild.roles, id=767458843230732319)
        elif emoji == Mojz12:
            role = discord.utils.get(guild.roles, id=767458844702933022)
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)

    if message5 == payload.message_id:
        member = payload.member
        guild = bot.get_guild(765315456415432704)

        emoji = payload.emoji.name
        if emoji == Mojp:
            role = discord.utils.get(guild.roles, id=767459216323117077)
        elif emoji == Mojp2:
            role = discord.utils.get(guild.roles, id=767459217920622692)
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)


#member = await(guild.fetch_member(payload.user_id))
        #if member is not None

bot.run("Nzc2NTMxOTc4OTcxMTE5NjQ2.X62Pww.DjzozDijWdnr_-56NMSY9h8lbeY")
