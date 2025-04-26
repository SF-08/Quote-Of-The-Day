import discord
from discord.ext import commands, tasks
from itertools import cycle

#Bot Status Cycle

bot_status = cycle(['Quoting Quotes.', 'Knowledge is power.', 'https://github.com/SF-08'])

class events(commands.Cog):
    """Events for the Bot"""
    
    def __init__(self, client):
        self.client = client

    #Status Loop

    @tasks.loop(seconds=20, count=None, reconnect=True)
    async def status_loop(self):
        """Bot Status Change"""
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game(next(bot_status)))
        