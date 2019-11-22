import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("DEEZ 서버")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("/deezsvon"):
        channel = client.get_channel(630432867683401824)
        await client.get_channel(int(630432867683401824)).send("@everyone                                                                                                                                                                                                                                                                                                                                                                                        DEEZ SERVER [ ON ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                   서버 주소 : deez.r-e.kr                                                                                                                                                                                                                                                                                                                                                                                                                                                               서버가 열린 후 바로 들어오시면 서버 렉의 원인이 됩니다.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 조금만 기다렸다가 접속해 주세요")




access_token = os.environ["BOT_TOKEN"]
client.run("access_token")
