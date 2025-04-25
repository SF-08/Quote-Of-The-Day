import discord
import random
from discord.ext import commands

#QUOTES

class quotes(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def love(self, ctx):
        love_quotes = [
            'QUOTES'
            'QUOTES'
            'QUOTES'
            'QUOTES'
            'QUOTES'
            'QUOTES'
            'QUOTES'
            'QUOTES'
            'QUOTES'
            'QUOTES'
        ]

        await ctx.send(random.choice(love_quotes))





# Cog Setup


def setup(client):
    client.add_cog(quotes(client))