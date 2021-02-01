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
    game = discord.Game("UDT 훈련")
    await client.change_presence(status=discord.Status.online, activity=game)
    

@client.event
async def on_member_join(member):
    fmt = '{0.mention}님 {1.name}에 오신 것을 환영합니다. 왼쪽 메뉴 #🔪│입대신청을 눌러주세요.'.format(member, member.guild)
    channel = client.get_channel(696579283547848734)
    await channel.send(fmt)


@client.event
async def on_reaction_add(reaction, user):
    if str(reaction.emoji) == "👍":
        await reaction.message.channel.send(
            "```" + user.name + "님이 " + reaction.message.author.name + "에게 좋아요를 누르셨습니다.```")
    if str(reaction.emoji) == "💩":
        await reaction.message.channel.send(
            "```" + user.name + "님이 " + reaction.message.author.name + "에게 응가를 했습니다.```")
    if str(reaction.emoji) == "💓":
        await reaction.message.channel.send(
            "```" + user.name + "님이 " + reaction.message.author.name + "에게 하트를 달았습니다.```")
    if str(reaction.emoji) == "💔":
        await reaction.message.channel.send(
            "```" + user.name + "님이 " + reaction.message.author.name + "의 하트를 찢었습니다.```")
    if str(reaction.emoji) == "💨":
        await reaction.message.channel.send(
            "```" + user.name + "님이 " + reaction.message.author.name + "을(를) 보고 한숨을 쉽니다.```")
    if str(reaction.emoji) == "😡":
        await reaction.message.channel.send("```" + user.name + "님이 " + reaction.message.author.name + "에게 화를 냅니다.```")
    if str(reaction.emoji) == "💋":
        await reaction.message.channel.send(
            "```" + user.name + "님이 " + reaction.message.author.name + "에게 키스를 갈깁니다.```")
    if str(reaction.emoji) == "📐":
        await reaction.message.channel.send(
            "```" + user.name + "님이 " + reaction.message.author.name + "의 머리를 삼각자로 찍었습니다.```")
    if str(reaction.emoji) == "🔑":
        await reaction.message.channel.send(
            "```" + user.name + "님이 " + reaction.message.author.name + "에게 집열쇠를 건넵니다.```")
    if str(reaction.emoji) == "🔇":
        await reaction.message.channel.send(
            "```" + user.name + "님이 " + reaction.message.author.name + "에게 닥치라고 합니다.```")
    if str(reaction.emoji) == "👅":
        await reaction.message.channel.send(
            "```" + user.name + "님이 " + reaction.message.author.name + "을(를) 혀로 햝습니다.```")
    if str(reaction.emoji) == "👌":
        await reaction.message.channel.send(
            "```" + user.name + "님이 " + reaction.message.author.name + "에게 알겠다고 합니다. ```")
    if str(reaction.emoji) == "🔨":
        await reaction.message.channel.send("```" + user.name + "이 " + reaction.message.author.name + "의 뚝배기를 깹니다. ```")



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
