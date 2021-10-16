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

    if message.content == "임베드":
        embed = discord.Embed(title="카멜리아 스토리에 오신 것을 환영합니다.", description='''🌸 를 누르시면 멤버 권한이 들어옵니다.
                              ⚠️ 게임을 악용하거나 서버 내 갈등을 조장하러 
                                  오신 분은 돌아가 주세요.''', color=0xFFFFFF)
        embed.set_image(url="https://i.imgur.com/2iWFMkw.mp4")
        embed.set_thumbnail(url="https://i.imgur.com/SpIFEgs.png")
        await message.channel.send("", embed=embed)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
