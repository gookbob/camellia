import discord
import os
from discord.ext import commands
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote
import requests
import asyncio
from json import loads
import random
import re
import warnings

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("카멜리아")
    await client.change_presence(status=discord.Status.online, activity=game)
    
@client.event
async def on_message(message):
    if message.content.startswith("테스트"):
        await message.channel.send("ㅇㅇ")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
