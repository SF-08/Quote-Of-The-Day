import discord
import os
from discord.ext import commands

botToken = input("What is the bot token?\n")

#Command Prefix
client = commands.Bot(command_prefix= 'quote')

#Function to check if it is SF
def sf(ctx):
    return ctx.author.id == '609330636611780629'

#Cog Loader, loads extension.

@client.command()
@commands.check(sf)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} loaded successfully.')

#Cog Reloader, reloads the extension.

@client.command(aliases=['refesh', 'Refresh', 'Reload'])
@commands.check(sf)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} reloaded successfuly.')    

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(botToken)