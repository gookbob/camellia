import discord
import os


client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("윤모와 영어공부")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("/deezsvon"):
        channel = client.get_channel(630432867683401824)
        await client.get_channel(int(630432867683401824)).send("")
       
    if message.content.startswith("국밥아"):
        await message.channel.send("왜 ㅅㅂ럼아")
    if message.content.startswith("검사인벤"):
        await message.channel.send("http://black.inven.co.kr/")
    if message.content.startswith("검사"):
        await message.channel.send("https://www.kr.playblackdesert.com/main/index")
       


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
