import os
import time
import discord
import requests
import json
import hashlib
import pytz
from datetime import datetime as dt
from requests.adapters import HTTPAdapter
from discord.ext import commands, random
from itertools import cycle

GMT = pytz.timezone('London / United Kingdom')
client = discord.Client()

class qotd(commands.Cog):
    """QuoteOfTheDay command - Different Quote per Day!"""


    @commands.command
    async def daily_quote(self, ctx):
        s = requests.Session()
        url="https://www.brainyquote.com/quote_of_the_day"
        s.mount(url, HTTPAdapter(max_retries=5))
        page = requests.get(url)    
        content = page.content.decode("utf-8")
        new_content = json.loads(content)
        quote = new_content["contents"]["quotes"][0]["quote"]
        return quote

    @commands.command()
    async def time(self):
        naive_dt = dt.now(GMT)
        current_time = naive_dt.strftime("%H:%M:%S")
        if current_time == "00:00:00":
            message =  daily_quote()
            await client.send(message)
            time.sleep(1)
                


def setup(client):
    client.add_cog(qotd(client))