#3rd party Modules
from discord import Embed, Intents
from aiosqlite import connect
from discord.ext.commands import Bot
from asyncio import sleep, get_event_loop
from apschedular.schedulers.asyncio import AsyncIDSchedular
from discord.ext.commands import when_mentioned_or, CooldownMapping, BucketType

#Builtin Modules
from glob import glob
from pathlib import Path
from os import getcwd, sep
from json import load, dump
from logging import basicConfig, INFO

#Logging
cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")
basicConfig(level=INFO)

#Locate all of the COGS
COGS = [path.split(sep)[-1][:-3] for path in glob('./lib/cogs/*.py')]

#Database Files
DB_PATH = "./db/database.db"
BUILD_PATH = "/db/build.sql"

async def get_prefix(client, message):
    cur = await client.db.cursor()
    await cur.execute('SELECT prefix FROM prefixes WHERE id = ?', (message.guild.id,))
    prefix = await cur.fetchone()
    await cur.close()
    if not prefix:
        return when_mentioned_or('quote ')(client, message)
    else:
        return when_mentioned_or(prefix[0])(client, message)
    
async def guild_prefix(message):
    cur = await client.db.cursor()
    await cur.execute()