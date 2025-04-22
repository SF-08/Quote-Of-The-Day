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
        


@commands.command(aliases=['delete', 'purge'])
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
@commands.cooldown(1, 8, commands.BucketType.user)
async def clear(self, ctx, amount=6):
    """Deletes messages in a channel."""

    embed = discord.Embed(
        description=f"Deleted {amount} messages.",
        colour=ctx.message.author.colour,
        timestamp=ctx.message.created_at
    )

    embed.set_author(
        name=f"{ctx.message.author.name} #{ctx.message.author.discriminator}",
        icon_url=ctx.message.author.avatar_url
    )

    await ctx.message.delete()
    await ctx.channel.purge(limit=amount)
    await ctx.send(embed=embed, delete_after=5.0)

@commands.command()
@commands.guild_only()
@commands.has_permissions(kick_members=True)
@commands.cooldown(1, 8, commands.BucketType.user)
async def kick(self, ctx, member: discord.Member, *, reason=None):
    """Kicks members from the server // However they can still join back."""

    embed = discord.Embed(
        title='👟 Kick users.',
        description='QOTD Bot will kick a specific member of the server.',
        colour=ctx.author.colour,
        timestamp=ctx.message.created_at
    )

    embed.add_field(name='Kicked User:', value=f"'{member.name}#{member.discriminator}\nID:{}'")