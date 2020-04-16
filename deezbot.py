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
    game = discord.Game("메1콩")
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
    if message.content.startswith("연장챙겨"):
        await message.channel.send("넵🔧🔨🔪")
    if message.content.startswith("멭갤"):
        await message.channel.send("https://gall.dcinside.com/board/lists/?id=maplestory2")     
    if message.content.startswith("모갤"):
        await message.channel.send("https://gall.dcinside.com/mgallery/board/lists/?id=ms2") 
    if message.content == "/임베드":
        embed = discord.Embed(title="지옥 학교에 오신걸 환영합니다.", description="입학을 원한다면 🔪을 누르세요", color=0x000000)
        embed.set_image(url="https://i.imgur.com/nvrWwoj.png")
        embed.set_thumbnail(url="https://i.imgur.com/1YsasKB.png")
        embed.set_footer(text="발신자 : 양치맨#4518", icon_url="https://i.imgur.com/3OpkEyM.png")
        await message.channel.send("", embed=embed)
    if message.content == "/임베드2":
        embed = discord.Embed(title="이곳은 학교 뒷골목입니다.", description="🏃모범학생 이상만 채팅칠 수 있습니다.", color=0x00FF00)
        embed.set_footer(text="발신자 : 양치맨#4518", icon_url="https://i.imgur.com/3OpkEyM.png")
        await message.channel.send("", embed=embed)
    if message.content == "/마이쮸":
        embed = discord.Embed(title="마이쮸 학교에 오신걸 환영합니다.", description="입학을 원한다면 🔪을 누르세요", color=0x000000)
        embed.set_image(url="https://https://i.imgur.com/VBZ4Ps5.png")
        embed.set_thumbnail(url="https://i.imgur.com/1YsasKB.png")
        embed.set_footer(text="발신자 : 양치맨#4518", icon_url="https://i.imgur.com/3OpkEyM.png")
        await message.channel.send("", embed=embed)   
        

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
    if str(reaction.emoji) == "💋":
        await reaction.message.channel.send("```"+user .name +"님이 "+reaction.message.author.name+"에게 키스를 갈깁니다.```")
    if str(reaction.emoji) == "📐":
        await reaction.message.channel.send("```"+user .name +"님이 "+reaction.message.author.name+"의 머리를 삼각자로 찍었습니다.```")
    if str(reaction.emoji) == "🔑":
        await reaction.message.channel.send("```"+user .name +"님이 "+reaction.message.author.name+"에게 집열쇠를 건넵니다.```")
    if str(reaction.emoji) == "🔇":
        await reaction.message.channel.send("```"+user .name +"님이 "+reaction.message.author.name+"에게 닥치라고 합니다.```")
    if str(reaction.emoji) == "👅":
        await reaction.message.channel.send("```"+user .name +"님이 "+reaction.message.author.name+"을(를) 혀로 햝습니다.```")
    if str(reaction.emoji) == "👌":
        await reaction.message.channel.send("```"+user .name +"님이 "+reaction.message.author.name+"에게 알겠다고 합니다. ```")
    if str(reaction.emoji) == "🔨":
        await reaction.message.channel.send("```"+user .name +"이 "+reaction.message.author.name+"의 뚝배기를 깹니다. ```")

                                   
@client.event
async def on_member_join(member):
    fmt = '{0.mention}님 {1.name}에 입학하신 것을 환영합니다. 왼쪽 메뉴에서 칼을 누르세요.'.format(member, member.guild)
    channel = member.guild.get_channel(696579283547848734)
    await channel.send(fmt)
    fmt = '@everyone 새로운 전학생 {0.mention}님이 {1.name}에 입학하셨습니다. 환영해주세요.'.format(member, member.guild)
    channel = member.guild.get_channel(547980454398132252)
    await channel.send(fmt)        
       


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
