#3rd party Modules
from discord import Embed, Intents
from aiosqlite import connect
from discord.ext.commands import Bot
from asyncio import sleep, get_event_loop
from apschedular.schedulers.asyncio import AsyncIDSchedular
from discord.ext.commands import when_mentioned_or, CooldownMapping, BucketType
import Pylance

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
    cur = await Bot.db.cursor()
    await cur.execute('SELECT prefix FROM prefixes WHERE id = ?', (message.guild.id,))
    prefix = await cur.fetchone()
    await cur.close()
    if not prefix:
        return 'quote'
    else:
        return prefix[0]
class Ready(object):
    """COG Console loading on startup"""

    def __init__(self):
        print(COGS)
        for cog in COGS:
            # commands.cog = false love.cog = false
            setattr(self, cog, False)
    
    def ready_up(self, cog):
        """Singular COG ready"""

        setattr(self, cog, True)
        print(f"{cog} COG ready")
    
    def all_ready(self):
        """All COGS are ready."""
    
        return all([getattr(self, cog) for cog in COGS])

intents = Intents.default()
client = Bot(command_prefix=get_prefix, intents=intents, case_insensitive=True, help_command=None)

client.prefix = guild_prefix
client.ready = False
client.cogs_ready = Ready()
client.support_url = 'ADD URL'
client.official_url = 'ADD URL'
client.invite_url = 'ADD URL'
client.scheduler = AsyncIDSchedular()
client.cooldown = CooldownMapping.from_cooldown(1, 5, BucketType.user) 
client.colours = {'WHITE': 0xFFFFF,
                  'RED': 0xE74C3C,
                  'NAVY': 0x34495E,
                  'GREEN': 0x2ECC71,
                  }
client.colour_list = [c for c in client.colours.values()]

def setup():
    """Initial COG loader"""

    for cog in COGS:
        client.load_extension(f"lib.cogs.{cog}")
        print(f"Initial setup for {cog}.py")

    print('COG setup complete')

def launch(version):
    """Run the bot using the API token"""

    client.version = version
    print('Running setup...')
    setup()
    with open('./lib/bot/token.txt', 'r', encoding='utf-8') as tf:
        client.TOKEN = tf.read()

    print(f"Running your bot on version {client.version}...")
    client.run(client.TOKEN, reconnect=True)

async def connect_db():
    client.db = await connect(DB_PATH)

get_event_loop().run_until_complete(connect_db())

@client.event
async def on_ready():
    cur = await client.db.cursor()
    with open(BUILD_PATH, 'r', encoding='utf-8') as script:
	    await cur.executescript(script.read())
    
client.scheduler.start()


status_channel = client.get_channel()
await status_channel.send(':wave: Boop Boop I\'m` back online!')

while not client.cogs_ready.all_ready():
    await sleep(0.5)