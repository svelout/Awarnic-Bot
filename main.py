import discord
from discord.ext import commands
from discord.ext.commands import Bot

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='=', intents = intents)

colours = {
    "✅": 832332996253319188
}

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=f"на участников"))
    print("Бот начал работать")

@bot.command(name='test')
@commands.has_permissions(manage_roles=True)
async def on_message(ctx):
    embed = discord.Embed(title="┌────▻ПЛАТФОРМА◅────┐", description="Здесь вы можете выбрать платформу", color=0xFF5733)
    embed.add_field(name="PC", value='🇦', inline=False)
    embed.add_field(name="Xbox", value='🇧', inline=False)
    embed.add_field(name="VReality", value='🇨', inline=False)
    embed.add_field(name="Mobile", value='🇩', inline=False)
    embed.add_field(name="Nintendo", value='🇪', inline=False)
    embed.add_field(name="PlayStation", value='🇫', inline=False)
    #Channel = discord.utils.get(ctx.guild.channels, id=831949714236244069)
    #Text = "YOUR_MESSAGE_HERE"
    Moji = await ctx.send(embed=embed)
    Moj = bot.get_emoji(767357702837764116)
    Moj2 = "🇧"#
    Moj3 = "🇨"#
    Moj4 = "🇩"#
    Moj5 = "🇪"#
    Moj6 = "🇫"
    Moj7 = "🇬"
    Moj8 = "🇭"
    Moj9 = "🇮"
    Moj10 = "🇯"
    Moj11 = "🇰"
    Moj12 = "🇱"

    await Moji.add_reaction(Moj)
    await Moji.add_reaction(Moj2)
    await Moji.add_reaction(Moj3)
    await Moji.add_reaction(Moj4)
    await Moji.add_reaction(Moj5)
    await Moji.add_reaction(Moj6)

    embed1 = discord.Embed(title="┌──────▻ВОЗРАСТ◅─────┐", description='Выберите роль со своим возрастом', color=0xFF5733)
    embed1.add_field(name='5-10', value='🇦', inline=False)
    embed1.add_field(name='10-15', value='🇧', inline=False)
    embed1.add_field(name='15-18', value='🇨', inline=False)
    embed1.add_field(name='18-25', value='🇩', inline=False)
    embed1.add_field(name='25-60', value='🇪', inline=False)

    Moji2 = await ctx.send(embed=embed1)
    await Moji2.add_reaction(Moj)
    await Moji2.add_reaction(Moj2)
    await Moji2.add_reaction(Moj3)
    await Moji2.add_reaction(Moj4)
    await Moji2.add_reaction(Moj5)

    embed2 = discord.Embed(title='┌───────▻ИГРЫ◅───────┐', description='Выберите роли с играми\n в которые вы играите',  color=0xFF5733)
    embed2.add_field(name='Roblox', value='🇦', inline=False)
    embed2.add_field(name='Among Us', value='🇧', inline=False)
    embed2.add_field(name='Minecraft', value='🇨', inline=False)
    embed2.add_field(name='Dota 2', value='🇩', inline=False)
    embed2.add_field(name='GTA V', value='🇪', inline=False)
    embed2.add_field(name='Fortnite', value='🇫', inline=False)
    embed2.add_field(name='CS:GO', value='🇬', inline=False)
    embed2.add_field(name='Overwatch', value='🇭', inline=False)
    embed2.add_field(name='NEXTRP', value='🇮', inline=False)
    embed2.add_field(name='Другие игры', value='🇯', inline=False)

    Moji3 = await ctx.send(embed=embed2)
    await Moji3.add_reaction(Moj)
    await Moji3.add_reaction(Moj2)
    await Moji3.add_reaction(Moj3)
    await Moji3.add_reaction(Moj4)
    await Moji3.add_reaction(Moj5)
    await Moji3.add_reaction(Moj6)
    await Moji3.add_reaction(Moj7)
    await Moji3.add_reaction(Moj8)
    await Moji3.add_reaction(Moj9)
    await Moji3.add_reaction(Moj10)

    embed3 = discord.Embed(title='┌───────▻ЗОДИАК◅──────┐', description='Выберите роль со своим знаком зодиаком',  color=0xFF5733)
    embed3.add_field(name='Овен', value='🇦', inline=False)
    embed3.add_field(name='Телец', value='🇧', inline=False)
    embed3.add_field(name='Близнецы', value='🇨', inline=False)
    embed3.add_field(name='Рак', value='🇩', inline=False)
    embed3.add_field(name='Дева', value='🇪', inline=False)
    embed3.add_field(name='Лев', value='🇫', inline=False)
    embed3.add_field(name='Весы', value='🇬', inline=False)
    embed3.add_field(name='Скорпион', value='🇭', inline=False)
    embed3.add_field(name='Стрелец', value='🇮', inline=False)
    embed3.add_field(name='Козерог', value='🇯', inline=False)
    embed3.add_field(name='Водолей', value='🇰', inline=False)
    embed3.add_field(name='Рыбы', value='🇱', inline=False)

    Moji4 = await ctx.send(embed=embed3)
    await Moji4.add_reaction(Moj)
    await Moji4.add_reaction(Moj2)
    await Moji4.add_reaction(Moj3)
    await Moji4.add_reaction(Moj4)
    await Moji4.add_reaction(Moj5)
    await Moji4.add_reaction(Moj6)
    await Moji4.add_reaction(Moj7)
    await Moji4.add_reaction(Moj8)
    await Moji4.add_reaction(Moj9)
    await Moji4.add_reaction(Moj10)
    await Moji4.add_reaction(Moj11)
    await Moji4.add_reaction(Moj12)

    embed4 = discord.Embed(title='┌───────▻ПОЛ◅───────┐', description='Выберите роли с вашим полом', color=0xFF5733)
    embed4.add_field(name='Девочка', value='🇦', inline=False)
    embed4.add_field(name='Мальчик', value='🇧', inline=False)

    Moji5 = await ctx.send(embed=embed4)
    await Moji5.add_reaction(Moj)
    await Moji5.add_reaction(Moj2)




@bot.event
async def on_member_join(ctx):
    guild = ctx.guild
    role1 = discord.utils.get(ctx.guild.roles, id=767454985390391306)
    role2 = discord.utils.get(ctx.guild.roles, id=767457027546939393)
    role3 = discord.utils.get(ctx.guild.roles, id=767457057619443762)
    role4 = discord.utils.get(ctx.guild.roles, id=767457174657695776)
    role5 = discord.utils.get(ctx.guild.roles, id=767456824520605767)
    await ctx.add_roles(role1)
    await ctx.add_roles(role2)
    await ctx.add_roles(role3)
    await ctx.add_roles(role4)
    await ctx.add_roles(role5)
    await ctx.send(f"Привет! Добро пожаловать на сервер {guild.name}\n Здесь ты можешь найти новых друзей и просто приятно провести время\n Не забудь прочитать правила!\n **Удачи!**")

@bot.event
async def on_raw_reaction_add(payload):
    message1 = 832700075662114907
    message2 = 832700087322148895
    message3 = 832700097669890090
    message4 = 832700118964633691
    message5 = 832700143404056606

    if message1 == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == '🇦':
            role = discord.utils.get(guild.roles, id=767457369675530240)
        elif emoji == '🇧':
            role = discord.utils.get(guild.roles, id=767457389150470144)
        elif emoji == '🇨':
            role = discord.utils.get(guild.roles, id=767457390877474847)
        elif emoji == '🇩':
            role = discord.utils.get(guild.roles, id=767457374591909908)
        elif emoji == '🇪':
            role = discord.utils.get(guild.roles, id=767457385353838622)
        elif emoji == '🇫':
            role = discord.utils.get(guild.roles, id=767457382959153192)
        await member.add_roles(role)

    if message2 == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == '🇦':
            role = discord.utils.get(guild.roles, id=767457913294946355)
        elif emoji == '🇧':
            role = discord.utils.get(guild.roles, id=767457916445130772)
        elif emoji == '🇨':
            role = discord.utils.get(guild.roles, id=767457918965907646)
        elif emoji == '🇩':
            role = discord.utils.get(guild.roles, id=767457921029242910)
        elif emoji == '🇪':
            role = discord.utils.get(guild.roles, id=767457922195390496)
        await member.add_roles(role)

    if message3 == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == '🇦':
            role = discord.utils.get(guild.roles, id=767458116446322689)
        elif emoji == '🇧':
            role = discord.utils.get(guild.roles, id=767458115029303317)
        elif emoji == '🇨':
            role = discord.utils.get(guild.roles, id=767458113976533012)
        elif emoji == '🇩':
            role = discord.utils.get(guild.roles, id=767458118091014166)
        elif emoji == '🇪':
            role = discord.utils.get(guild.roles, id=767458119239729153)
        elif emoji == '🇫':
            role = discord.utils.get(guild.roles, id=767458121777807371)
        elif emoji == '🇬':
            role = discord.utils.get(guild.roles, id=767458121969827870)
        elif emoji == '🇭':
            role = discord.utils.get(guild.roles, id=767458123749130250)
        elif emoji == '🇮':
            role = discord.utils.get(guild.roles, id=767458125044645898)
        elif emoji == '🇯':
            role = discord.utils.get(guild.roles, id=767458126500331550)
        await member.add_roles(role)

    if message4 == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == '🇦':
            role = discord.utils.get(guild.roles, id=767458830430109696)
        elif emoji == '🇧':
            role = discord.utils.get(guild.roles, id=767458832221339718)
        elif emoji == '🇨':
            role = discord.utils.get(guild.roles, id=767458833538613278)
        elif emoji == '🇩':
            role = discord.utils.get(guild.roles, id=767458834822201417)
        elif emoji == '🇪':
            role = discord.utils.get(guild.roles, id=767458835945619486)
        elif emoji == '🇫':
            role = discord.utils.get(guild.roles, id=767458837295923230)
        elif emoji == '🇬':
            role = discord.utils.get(guild.roles, id=767458838608871454)
        elif emoji == '🇭':
            role = discord.utils.get(guild.roles, id=767458839985258538)
        elif emoji == '🇮':
            role = discord.utils.get(guild.roles, id=767458840781914183)
        elif emoji == '🇯':
            role = discord.utils.get(guild.roles, id=767458841704923147)
        elif emoji == '🇰':
            role = discord.utils.get(guild.roles, id=767458843230732319)
        elif emoji == '🇱':
            role = discord.utils.get(guild.roles, id=767458844702933022)
        await member.add_roles(role)

    if message5 == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == '🇦':
            role = discord.utils.get(guild.roles, id=767459216323117077)
        elif emoji == '🇧':
            role = discord.utils.get(guild.roles, id=767459217920622692)
        await member.add_roles(role)


@bot.event
async def on_raw_reaction_remove(payload):
    message1 = 832700075662114907
    message2 = 832700087322148895
    message3 = 832700097669890090
    message4 = 832700118964633691
    message5 = 832700143404056606

    if message1 == payload.message_id:
        guild = await(bot.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name
        if emoji == '🇦':
            role = discord.utils.get(guild.roles, id=767457369675530240)
        elif emoji == '🇧':
            role = discord.utils.get(guild.roles, id=767457389150470144)
        elif emoji == '🇨':
            role = discord.utils.get(guild.roles, id=767457390877474847)
        elif emoji == '🇩':
            role = discord.utils.get(guild.roles, id=767457374591909908)
        elif emoji == '🇪':
            role = discord.utils.get(guild.roles, id=767457385353838622)
        elif emoji == '🇫':
            role = discord.utils.get(guild.roles, id=767457382959153192)
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)

    if message2 == payload.message_id:
        guild = await(bot.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name
        if emoji == '🇦':
            role = discord.utils.get(guild.roles, id=767457913294946355)
        elif emoji == '🇧':
            role = discord.utils.get(guild.roles, id=767457916445130772)
        elif emoji == '🇨':
            role = discord.utils.get(guild.roles, id=767457918965907646)
        elif emoji == '🇩':
            role = discord.utils.get(guild.roles, id=767457921029242910)
        elif emoji == '🇪':
            role = discord.utils.get(guild.roles, id=767457922195390496)
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)

    if message3 == payload.message_id:
        guild = await(bot.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name
        if emoji == '🇦':
             role = discord.utils.get(guild.roles, id=767458116446322689)
        elif emoji == '🇧':
            role = discord.utils.get(guild.roles, id=767458115029303317)
        elif emoji == '🇨':
            role = discord.utils.get(guild.roles, id=767458113976533012)
        elif emoji == '🇩':
             role = discord.utils.get(guild.roles, id=767458118091014166)
        elif emoji == '🇪':
            role = discord.utils.get(guild.roles, id=767458119239729153)
        elif emoji == '🇫':
            role = discord.utils.get(guild.roles, id=767458121777807371)
        elif emoji == '🇬':
            role = discord.utils.get(guild.roles, id=767458121969827870)
        elif emoji == '🇭':
            role = discord.utils.get(guild.roles, id=767458123749130250)
        elif emoji == '🇮':
            role = discord.utils.get(guild.roles, id=767458125044645898)
        elif emoji == '🇯':
            role = discord.utils.get(guild.roles, id=767458126500331550)
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)

    if message4 == payload.message_id:
        guild = await(bot.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name
        if emoji == '🇦':
             role = discord.utils.get(guild.roles, id=767458830430109696)
        elif emoji == '🇧':
            role = discord.utils.get(guild.roles, id=767458832221339718)
        elif emoji == '🇨':
            role = discord.utils.get(guild.roles, id=767458833538613278)
        elif emoji == '🇩':
             role = discord.utils.get(guild.roles, id=767458834822201417)
        elif emoji == '🇪':
            role = discord.utils.get(guild.roles, id=767458835945619486)
        elif emoji == '🇫':
            role = discord.utils.get(guild.roles, id=767458837295923230)
        elif emoji == '🇬':
            role = discord.utils.get(guild.roles, id=767458838608871454)
        elif emoji == '🇭':
            role = discord.utils.get(guild.roles, id=767458839985258538)
        elif emoji == '🇮':
            role = discord.utils.get(guild.roles, id=767458840781914183)
        elif emoji == '🇯':
            role = discord.utils.get(guild.roles, id=767458841704923147)
        elif emoji == '🇰':
            role = discord.utils.get(guild.roles, id=767458843230732319)
        elif emoji == '🇱':
            role = discord.utils.get(guild.roles, id=767458844702933022)
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)

    if message5 == payload.message_id:
        guild = await(bot.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name
        if emoji == '🇦':
            role = discord.utils.get(guild.roles, id=767459216323117077)
        elif emoji == '🇧':
            role = discord.utils.get(guild.roles, id=767459217920622692)
        member = await(guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)



bot.run("Nzc2NTMxOTc4OTcxMTE5NjQ2.X62Pww.DjzozDijWdnr_-56NMSY9h8lbeY")