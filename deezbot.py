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
        await client.get_channel(int(437679614370906122)).send("@everyone 집합!!!")
    if message.content.startswith("/숙제"):
        await message.channel.send("```바베니일일퀘스트+함선```")
        await message.channel.send("```열쇠 10+3 뽑기```")
        await message.channel.send("```생활 폐광 1층 10판 (안해두댐)```")
        await message.channel.send("```바야르 10판```")
        await message.channel.send("```펫합성```")
        await message.channel.send("```부캐피파```")
        await message.channel.send("```길드출석 기부```")
    if message.content.startswith("악마야"):
        await message.channel.send("네")
    if message.content.startswith("무투"):
        await message.channel.send("귀요미")
    if message.content.startswith("메콩인벤"):
        await message.channel.send("http://inven.co.kr/maple2/")
    if message.content.startswith("메콩공홈"):
        await message.channel.send("http://maplestory2.nexon.com/Main/Index")
        

@client.event
async def on_reaction_add(reaction, user):
    if str(reaction.emoji) == "👍":
        await reaction.message.channel.send("```"+user .name +"님이 "+reaction.message.author.name+"에게 좋아요를 누르셨습니다.```")
    if str(reaction.emoji) == "💩":
        await reaction.message.channel.send("```"+user .name +"님이 "+reaction.message.author.name+"에게 응가를 했습니다.```")
    if str(reaction.emoji) == "💓":
        await reaction.message.channel.send("```"+user .name +"님이 "+reaction.message.author.name+"에게 하트를 달았습니다.```")
    if str(reaction.emoji) == "💔":
        await reaction.message.channel.send("```"+user .name +"님이 "+reaction.message.author.name+"의 하트를 찢었습니다.```")
    if str(reaction.emoji) == "💨":
        await reaction.message.channel.send("```"+user .name +"님이 "+reaction.message.author.name+"을(를) 보고 한숨을 쉽니다.```")
    if str(reaction.emoji) == "😡":
        await reaction.message.channel.send("```"+user .name +"님이 "+reaction.message.author.name+"에게 화를 냅니다.```")

        
        
       


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
