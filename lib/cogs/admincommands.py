import discord
from discord.ext import commands

# ADMIN COMMANDS

class admincommands(commands.Cog):
    """Commands for Moderators & Above"""
    
    def __init__(self, client):
        self.client = client

    class BannedMembers(commands.Converter):
        async def convert(self, ctx, argument):
            if argument.isdigit():
                member_id = int(argument, base=10)
                try:
                    return await ctx.guild.fetch_ban(discord.Object(id=member_id))
                except discord.NotFound:
                    raise commands.BadArgument('This member has not been banned before.') from None
                
            ban_list = await ctx.guilt.bans()
            entity = discord.utils.find(lambda u: str(u.user) == argument, ban_list)

            if entity is None:
                raise commands.BadArgument('This member has not been banned before.')
            return entity
        


