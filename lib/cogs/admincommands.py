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

    embed.add_field(name='Kicked User:', value=f"'{member.name}#{member.discriminator}\nID:{member.id}'", inline=False)
    embed.add_field(name='Punisher:', value=f"'{ctx.message.author.name}#{ctx.message.author.discriminator}\nID:{ctx.message.author.id}'", inline=False)
    embed.add_field(name='Reason:', value=f"'{reason}'")
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGR1aWkzdmFocmljc2tpenN6YjRqNjl0c2d4cmpxd3FqZjIzaHlkaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LICtqQ1K8ClIQ/giphy.gif')
    embed.set_author(name=f"{member.name}#{member.discriminator}", icon_url=member.avatar_url)
    embed.set_footer(text=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
    await ctx.send(embed=embed)
    await member.send(embed=embed)

@commands.command()
@commands.guild_only()
@commands.has_permissions(ban_members=True)
@commands.cooldown(1, 8, commands.BucketType.user)
async def ban(self, ctx, member: discord.Member, *, reason=None):
    """Bans a member from the server."""

    embed = discord.Embed(
        title='🔨 Ban Users.',
        description='QOTD Bot will ban a specific member of the server.',
        colour=ctx.author.colour,
        timestamp=ctx.message.created_at
    )

    embed.add_field(name='Banned User:', value=f"'{member.name}#{member.discriminator}\nID:{member.id}'" inline=False)
    embed.add_field(name='Punisher:', value=f"'{ctx.message.author.name}#{ctx.message.author.discriminator}\nID:{ctx.message.author.id}'", inline=False)
    embed.add_field(name='Reason:', value=f"'{reason}'")
    embed.set_thumbnail(url='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnUxcTJnMWlrbjZjYmUyeWJqcDRpaG40dGJ4bTI1c2EzbHo3NDNxbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qPD4yGsrc0pdm/giphy.gif')
    embed.set_author(name=f"{member.name}#{member.discriminator}", icon_url=member.avatar_url)
    embed.set_footer(text=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
    await ctx.send(embed=embed)
    await member.send(embed=embed)

@commands.command()
@commands.guild_only()
@commands.has_permissions(ban_members=True)
@commands.cooldown(1, 8, commands.BucketType.user)
async def unban(self, ctx, member: discord.Member, *, reason=None):
    """Unbans a member from the server."""

    embed = discord.Embed(
        title='',
        description='QOTD Bot will unban a specific member of the server.'
        colour=ctx.author.colour,
        timestamp=ctx.message.created_at
    )

    embed.add_field(name='Unbanned User:', value=f"'{member.user}\nID:{member.user.id}'" inline=False)
    embed.add_field(name='Unbanned By:', value=f"'{ctx.message.author.name}#{ctx.message.author.discriminator}\nID:{ctx.message.author.id}'", inline=False)
    embed.add_field(name='Reason:', value=f"'{reason}'", inline=False)
    embed.set_thumbnail(url='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2s5YmVhcWQ2dTVzcjJzeWwwNzUweTJuOWRtZDhkZDJlaTVtM3BpNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l1J9urAfGd3grKV6E/giphy.gif')
    embed.set_author(name=f"{member.user}")
    embed.set_footer(text=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
    await ctx.send(embed=embed)
    await member.send(embed=embed)