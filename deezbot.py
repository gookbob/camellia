import discord
import os
import requests
import asyncio
from json import loads
import random


client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("메콩")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("집합"):
        channel = client.get_channel(437679614370906122)
        await client.get_channel(int(437679614370906122)).send("```@everyone 집합!!!```")
       
    if message.content.startswith("악마야"):
        await message.channel.send("네")
    if message.content.startswith("메콩인벤"):
        await message.channel.send("http://inven.co.kr/maple2/")
    if message.content.startswith("메콩공홈"):
        await message.channel.send("http://maplestory2.nexon.com/Main/Index")
        

@client.event
async def on_reaction_add(reaction, user):
    if str(reaction.emoji) == "👍":
        await reaction.message.channel.send("```"+user .name + "님이"+message.author.name+"에게 좋아요를 누르셨습니다.```")
    if str(reaction.emoji) == "💩":
        await reaction.message.channel.send("```"+user .name + "님이"+message.author.name+"에게 응가를 했습니다.```")
    if str(reaction.emoji) == "💓":
        await reaction.message.channel.send("```"+user .name + "님이"+message.author.name+"에게 하트를 달았습니다.```")
    if str(reaction.emoji) == "💔":
        await reaction.message.channel.send("```"+user .name + "님이"+message.author.name+"의 하트를 찢었습니다.```")
        
        
       


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
