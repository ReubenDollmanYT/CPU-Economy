from discord.ext.commands import Cog, BucketType
from discord.ext.commands import command, cooldown
from discord.utils import get
from discord import Embed
from datetime import datetime
from random import randint
import pybelieva
from typing import Optional

class unb(Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_ready(self):
        self.unb_client = pybelieva.Client('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBfaWQiOiI4MDM5NjUxMjcwMzU1ODUwOTEiLCJpYXQiOjE2MTE3NTA2MjN9.e5LjMTWzvT3b6OWjHOHDKTclMLozjZTw1P93oK3R9vo')
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up('unb')
        print('unb loaded')
        await self.bot.stdout.send('unb Cog loaded!')
    
    @command()
    @cooldown(1, 60, BucketType.user)
    async def books(self, ctx):
        '''Gives money for reading books'''
        cash = randint(100, 500)
        await self.unb_client.patch_user_balance(ctx.guild.id, ctx.author.id, cash=cash, reason="Read some Books")
        #emoji = get(ctx.message.server.emojis, name="Beachball")
        embed = Embed(
            title="Book Command",
            description=f'You just got {cash} money for reading books!', #{emoji}
            colour=0xd6ff00,
            timestamp=datetime.utcnow())
        await ctx.send(embed=embed)
    
    @command()
    @cooldown(1, 3600, BucketType.user)
    async def hourly(self, ctx):
        cash = randint(1000, 2000)
        await self.unb_client.patch_user_balance(ctx.guild.id, ctx.author.id, cash=cash, reason="Waited 1 Hour")
        #emoji = get(ctx.message.server.emojis, name="Beachball")
        embed = Embed(
            title="Hourly",
            description=f"You just got {cash} for waiting 1 hour. I wonder who gave it to you",
            colour=0xfd00ff,
            timestamp=datetime.utcnow())
        await ctx.send(embed=embed)

    @command()
    @cooldown(1, 600, BucketType.user)
    async def Code(self, ctx):
        '''Gives money for codeing things'''
        cash = randint(100, 500)
        await self.unb_client.patch_user_balance(ctx.guild.id, ctx.author.id, cash=cash, reason="Did Some Codeing")
        #emoji = get(ctx.message.server.emojis, name="Beachball")
        embed = Embed(
            title="Code Command",
            description=f'You just got {cash} money for codeing!',
            colour=0x00ffab,
            timestamp=datetime.utcnow())
        embed.set_thumbnail(url="https://reubendollmanyt.is-inside.me/KLkj4dVp.gif")
        await ctx.send(embed=embed)

    @command()
    @cooldown(1, 86400, BucketType.user)
    async def daily(self, ctx):
        cash = randint(5000, 6000)
        await self.unb_client.patch_user_balance(ctx.guild.id, ctx.author.id, cash=cash, reason="Waited 1 Day")
        embed = Embed(
            title="Daily",
            description=f"You just got {cash} for waiting 24 hours.~~now go spend it~~",
            colour=0xfd00ff,
            timestamp=datetime.utcnow())
        await ctx.send(embed=embed)    

def setup(bot):
    bot.add_cog(unb(bot))