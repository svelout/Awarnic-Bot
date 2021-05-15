import sqlite3

import discord
from discord.ext import commands
import main


class WelcomeCog(commands.Cog, name='Moderation'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def ban(self, ctx, *, reason=None):
        member = discord.Member
        if ctx.message.startwith("=ban"):
            await member.ban(reason=reason)
            db = sqlite3.connect('main.sqlite')
            cursor = main.cursor()
            cursor.execute(f"SELECT banned_member_id FROM main WHERE message_id = {ctx.message.id}")
            result = cursor.fetchone()







