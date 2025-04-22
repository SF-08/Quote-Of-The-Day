import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random
from aiohttp import requests

load_dotenv()
key = os.getenv('API_KEY')

class love(commands.Cog):
    api_url = 'https://api.api-ninjas.com/v1/quotes'
    response = requests.get(api_url, headers={'X-Api-Key': 'API_KEY'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Uh Oh! I have an error.", response.status_code, response.text)