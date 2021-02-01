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


@client.event
async def on_member_join(member):
    fmt = '{0.mention}님 {1.name}에 오신 것을 환영합니다. 왼쪽 메뉴 #🔪│입대신청을 눌러주세요.'.format(member, member.guild)
    channel = client.get_channel(696579283547848734)
    await channel.send(fmt)
    fmt = '@everyone 새로운 전학생 {0.mention}님이 {1.name}에 입학하셨습니다. 환영해주세요.'.format(member, member.guild)
    channel = client.get_channel(782259746257633350)
    await client.send(fmt)

tierScore = {
    'default': 0,
    'iron': 1,
    'bronze': 2,
    'silver': 3,
    'gold': 4,
    'platinum': 5,
    'diamond': 6,
    'master': 7,
    'grandmaster': 8,
    'challenger': 9
}


def tierCompare(solorank, flexrank):
    if tierScore[solorank] > tierScore[flexrank]:
        return 0
    elif tierScore[solorank] < tierScore[flexrank]:
        return 1
    else:
        return 2


warnings.filterwarnings(action='ignore')
bot = commands.Bot(command_prefix='!')

opggsummonersearch = 'https://www.op.gg/summoner/userName='

'''
Simple Introduction about asyncio
asyncio : Asynchronous I/O. It is a module for asynchronous programming and allows CPU operations to be handled in parallel with I/O.
async def (func name)(parameters): -> This type of asynchronous function or method is called Native Co-Rutine.
- await : you can use await keyword only in Native Co-Rutine
async def add(a,b):
    print("add {0} + {1}".format(a,b))
    await asyncio.sleep(1.0)
    return a + b
async def print_add(a,b):
    result = await add(a,b)
    print("print_add : {0} + {1} = {2}".format(a,b,result))
loop = asyncio.get_event_loop()
loop.run_until_complete(print_add(1,2))
loop.close()
'''


def deleteTags(htmls):
    for a in range(len(htmls)):
        htmls[a] = re.sub('<.+?>', '', str(htmls[a]), 0).strip()
    return htmls


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@client.event
async def on_message(message):
    if message.content.startswith("/전적"):
        try:
            if len(message.content.split(" ")) == 1:
                embed = discord.Embed(title="소환사 이름이 입력되지 않았습니다!", description="", color=0x0080FF)
                embed.add_field(name="Summoner name not entered",
                                value="명령어를 다시 확인해주세요. /전적 (소환사명)", inline=False)
                embed.set_footer(text='제작 : 양치맨#7777',
                                 icon_url='https://i.imgur.com/3OpkEyM.png')
                await message.channel.send("Error : Incorrect command usage ", embed=embed)
            else:
                playerNickname = ''.join((message.content).split(' ')[1:])
                # Open URL
                checkURLBool = urlopen(opggsummonersearch + quote(playerNickname))
                bs = BeautifulSoup(checkURLBool, 'html.parser')

                # 자유랭크 언랭은 뒤에 '?image=q_auto&v=1'표현이없다

                # Patch Note 20200503에서
                # Medal = bs.find('div', {'class': 'ContentWrap tabItems'}) 이렇게 바꾸었었습니다.
                # PC의 설정된 환경 혹은 OS플랫폼에 따라서 ContentWrap tabItems의 띄어쓰기가 인식이

                Medal = bs.find('div', {'class': 'SideContent'})
                RankMedal = Medal.findAll('img', {'src': re.compile(
                    '\/\/[a-z]*\-[A-Za-z]*\.[A-Za-z]*\.[A-Za-z]*\/[A-Za-z]*\/[A-Za-z]*\/[a-z0-9_]*\.png')})
                # Variable RankMedal's index 0 : Solo Rank
                # Variable RankMedal's index 1 : Flexible 5v5 rank

                # for mostUsedChampion
                mostUsedChampion = bs.find('div', {'class': 'ChampionName'})
                mostUsedChampionKDA = bs.find('span', {'class': 'KDA'})

                # 솔랭, 자랭 둘다 배치가 안되어있는경우 -> 사용된 챔피언 자체가 없다. 즉 모스트 챔피언 메뉴를 넣을 필요가 없다.

                # Scrape Summoner's Rank information
                # [Solorank,Solorank Tier]
                solorank_Types_and_Tier_Info = deleteTags(bs.findAll('div', {'class': {'RankType', 'TierRank'}}))
                # [Solorank LeaguePoint, Solorank W, Solorank L, Solorank Winratio]
                solorank_Point_and_winratio = deleteTags(
                    bs.findAll('span', {'class': {'LeaguePoints', 'wins', 'losses', 'winratio'}}))
                # [Flex 5:5 Rank,Flexrank Tier,Flextier leaguepoint + W/L,Flextier win ratio]
                flexrank_Types_and_Tier_Info = deleteTags(bs.findAll('div', {
                    'class': {'sub-tier__rank-type', 'sub-tier__rank-tier', 'sub-tier__league-point',
                              'sub-tier__gray-text'}}))
                # ['Flextier W/L]
                flexrank_Point_and_winratio = deleteTags(bs.findAll('span', {'class': {'sub-tier__gray-text'}}))

                # embed.set_imag()는 하나만 들어갈수 있다.

                # 솔랭, 자랭 둘다 배치 안되어있는 경우 -> 모스트 챔피언 출력 X
                if len(solorank_Point_and_winratio) == 0 and len(flexrank_Point_and_winratio) == 0:
                    embed = discord.Embed(title="📃 소환사 " + playerNickname + "님의 전적", description="", color=0x0080FF)
                    embed.add_field(name="op.gg 주소", value=opggsummonersearch + playerNickname,
                                    inline=False)
                    embed.add_field(name="솔로랭크 : Unranked", value="Unranked", inline=False)
                    embed.add_field(name="자유랭크 : Unranked", value="Unranked", inline=False)
                    embed.set_thumbnail(url='https:' + RankMedal[0]['src'])
                    embed.set_footer(text='제작 : 양치맨#7777',
                                     icon_url='https://i.imgur.com/3OpkEyM.png')
                    await message.channel.send("", embed=embed)

                # 솔로랭크 기록이 없는경우
                elif len(solorank_Point_and_winratio) == 0:

                    # most Used Champion Information : Champion Name, KDA, Win Rate
                    mostUsedChampion = bs.find('div', {'class': 'ChampionName'})
                    mostUsedChampion = mostUsedChampion.a.text.strip()
                    mostUsedChampionKDA = bs.find('span', {'class': 'KDA'})
                    mostUsedChampionKDA = mostUsedChampionKDA.text.split(':')[0]
                    mostUsedChampionWinRate = bs.find('div', {'class': "Played"})
                    mostUsedChampionWinRate = mostUsedChampionWinRate.div.text.strip()

                    FlexRankTier = flexrank_Types_and_Tier_Info[0] + ' : ' + flexrank_Types_and_Tier_Info[1]
                    FlexRankPointAndWinRatio = flexrank_Types_and_Tier_Info[2] + " /" + flexrank_Types_and_Tier_Info[-1]
                    embed = discord.Embed(title="소환사 전적검색", description="", color=0x5CD1E5)
                    embed.add_field(name="솔로랭크 : Unranked", value="Unranked", inline=False)
                    embed.add_field(name=FlexRankTier, value=FlexRankPointAndWinRatio, inline=False)
                    embed.add_field(name="Most Used Champion : " + mostUsedChampion,
                                    value="KDA : " + mostUsedChampionKDA + " / " + " WinRate : " + mostUsedChampionWinRate,
                                    inline=False)
                    embed.add_field(name="op.gg 주소", value=opggsummonersearch + playerNickname,
                                    inline=False)
                    embed.set_thumbnail(url='https:' + RankMedal[1]['src'])
                    embed.set_footer(text='제작 : 양치맨#7777',
                                     icon_url='https://i.imgur.com/3OpkEyM.png')
                    await message.channel.send("소환사 " + playerNickname + "님의 전적", embed=embed)

                # 자유랭크 기록이 없는경우
                elif len(flexrank_Point_and_winratio) == 0:

                    # most Used Champion Information : Champion Name, KDA, Win Rate
                    mostUsedChampion = bs.find('div', {'class': 'ChampionName'})
                    mostUsedChampion = mostUsedChampion.a.text.strip()
                    mostUsedChampionKDA = bs.find('span', {'class': 'KDA'})
                    mostUsedChampionKDA = mostUsedChampionKDA.text.split(':')[0]
                    mostUsedChampionWinRate = bs.find('div', {'class': "Played"})
                    mostUsedChampionWinRate = mostUsedChampionWinRate.div.text.strip()

                    SoloRankTier = ' : ' + solorank_Types_and_Tier_Info[1]
                    SoloRankPointAndWinRatio = solorank_Point_and_winratio[0] + " / " + solorank_Point_and_winratio[
                        1] + " " + solorank_Point_and_winratio[2] + " / " + solorank_Point_and_winratio[3]
                    embed = discord.Embed(title="소환사 " + playerNickname + "님의 전적", description="", color=0x0080FF)
                    embed.add_field(name='솔로랭크' + SoloRankTier, value=SoloRankPointAndWinRatio, inline=False)
                    embed.add_field(name="자유랭크 : Unranked", value="Unranked", inline=False)
                    embed.add_field(name="모스트 챔피언 : " + mostUsedChampion,
                                    value="KDA : " + mostUsedChampionKDA + " / " + "WinRate : " + mostUsedChampionWinRate,
                                    inline=False)
                    embed.add_field(name="op.gg 주소", value=opggsummonersearch + playerNickname,
                                    inline=False)
                    embed.set_thumbnail(url='https:' + RankMedal[0]['src'])
                    embed.set_footer(text='제작 : 양치맨#7777',
                                     icon_url='https://i.imgur.com/3OpkEyM.png')
                    await message.channel.send("", embed=embed)
                # 두가지 유형의 랭크 모두 완료된사람
                else:
                    # 더 높은 티어를 thumbnail에 안착
                    solorankmedal = RankMedal[0]['src'].split('/')[-1].split('?')[0].split('.')[0].split('_')
                    flexrankmedal = RankMedal[1]['src'].split('/')[-1].split('?')[0].split('.')[0].split('_')

                    # Make State
                    SoloRankTier = ' : ' + solorank_Types_and_Tier_Info[1]
                    SoloRankPointAndWinRatio = solorank_Point_and_winratio[0] + " / " + solorank_Point_and_winratio[
                        1] + " " + solorank_Point_and_winratio[2] + " / " + solorank_Point_and_winratio[3]
                    FlexRankTier = ' : ' + flexrank_Types_and_Tier_Info[1]
                    FlexRankPointAndWinRatio = flexrank_Types_and_Tier_Info[2] + " / " + flexrank_Types_and_Tier_Info[
                        -1]

                    # most Used Champion Information : Champion Name, KDA, Win Rate
                    mostUsedChampion = bs.find('div', {'class': 'ChampionName'})
                    mostUsedChampion = mostUsedChampion.a.text.strip()
                    mostUsedChampionKDA = bs.find('span', {'class': 'KDA'})
                    mostUsedChampionKDA = mostUsedChampionKDA.text.split(':')[0]
                    mostUsedChampionWinRate = bs.find('div', {'class': "Played"})
                    mostUsedChampionWinRate = mostUsedChampionWinRate.div.text.strip()

                    cmpTier = tierCompare(solorankmedal[0], flexrankmedal[0])
                    embed = discord.Embed(title="소환사 " + playerNickname + "님의 전적", description="", color=0x0080FF)
                    embed.add_field(name='솔로랭크' + SoloRankTier, value=SoloRankPointAndWinRatio, inline=False)
                    embed.add_field(name='자유랭크' + FlexRankTier, value=FlexRankPointAndWinRatio, inline=False)
                    embed.add_field(name="모스트 챔피언 : " + mostUsedChampion,
                                    value="KDA : " + mostUsedChampionKDA + " / " + " WinRate : " + mostUsedChampionWinRate,
                                    inline=False)
                    if cmpTier == 0:
                        embed.set_thumbnail(url='https:' + RankMedal[0]['src'])
                    elif cmpTier == 1:
                        embed.set_thumbnail(url='https:' + RankMedal[1]['src'])
                    else:
                        if solorankmedal[1] > flexrankmedal[1]:
                            embed.set_thumbnail(url='https:' + RankMedal[0]['src'])
                        elif solorankmedal[1] < flexrankmedal[1]:
                            embed.set_thumbnail(url='https:' + RankMedal[0]['src'])
                        else:
                            embed.set_thumbnail(url='https:' + RankMedal[0]['src'])

                    embed.add_field(name="op.gg 주소", value=opggsummonersearch + playerNickname,
                                    inline=False)
                    embed.set_footer(text='제작 : 양치맨#7777',
                                     icon_url='https://i.imgur.com/3OpkEyM.png')
                    await message.channel.send("", embed=embed)
        except HTTPError as e:
            embed = discord.Embed(title="소환사 전적검색 실패", description="", color=0x5CD1E5)
            embed.add_field(name="", value="올바르지 않은 소환사 이름입니다. 다시 확인해주세요!", inline=False)
            await message.channel.send("Wrong Summoner Nickname")

        except UnicodeEncodeError as e:
            embed = discord.Embed(title="소환사 전적검색 실패", description="", color=0x5CD1E5)
            embed.add_field(name="???", value="올바르지 않은 소환사 이름입니다. 다시 확인해주세요!", inline=False)
            await message.channel.send("Wrong Summoner Nickname", embed=embed)

        except AttributeError as e:
            embed = discord.Embed(title="존재하지 않는 소환사", description="", color=0x5CD1E5)
            embed.add_field(name="OP.GG에 등록되지 않은 소환사입니다.", value="오타를 확인 후 다시 검색해주세요.", inline=False)
            embed.set_footer(text='제작 : 양치맨#7777',
                             icon_url='https://i.imgur.com/3OpkEyM.png')
            await message.channel.send("Error : Non existing Summoner ", embed=embed)
    if message.content.startswith("집합"):
        channel = client.get_channel(437679614370906122)
        await client.get_channel(int(437679614370906122)).send("@everyone 집합!!!")
        await message.channel.send("", embed=embed)
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
    if message.content.startswith("/mute"):
        channel = client.get_channel(547980454398132252)
        await client.get_channel(int(547980454398132252)).send("```도배가 감지되어 자동 뮤트 되었습니다.```")
    if message.content == "/임베드":
        embed = discord.Embed(title="사이버 UDT에 오신걸 환영합니다.", description="입대를 하시려면 🔪을 누르세요", color=0x000000)
        embed.set_image(url="https://i.imgur.com/RKAV9GX.png")
        embed.set_thumbnail(url="https://i.imgur.com/nvrWwoj.png")
        embed.set_footer(text="발신자 : 윤모#7777", icon_url="https://i.imgur.com/3OpkEyM.png")
        await message.channel.send("", embed=embed)
    if message.content == "/임베드2":
        embed = discord.Embed(title="이곳은 학교 뒷골목입니다.", description="🏃모범학생 이상만 채팅칠 수 있습니다.", color=0x00FF00)
        embed.set_footer(text="발신자 : 양치맨#4518", icon_url="https://i.imgur.com/3OpkEyM.png")
        await message.channel.send("", embed=embed)
    if message.content.startswith("/숙제"):
        embed = discord.Embed(title="메콩숙제", description="", color=0x00FF00)
        embed.add_field(name="주간", value="""바베니 주간퀘스트, 라펜샤드 구매
        50, 60, 70카오스, 폐광 4층
        에네르코어 옵션변경권 구매""", inline=False)
        embed.add_field(name="일간", value="""바베니, 함선 일간퀘스트
        열쇠 10 + 3 뽑기
        생활기술
        폐광 1층 10판
        발록 10판
        펫합성
        부캐 피파
        길드출석 기부""", inline=False)
        embed.set_thumbnail(url="https://i.imgur.com/1YsasKB.png")
        embed.set_footer(text="발신자 : 양치맨#7777", icon_url="https://i.imgur.com/3OpkEyM.png")
        await message.channel.send("", embed=embed)
    if message.content.startswith("/로아숙제"):
        embed = discord.Embed(title="로아숙제", description="", color=0xFF0000)
        embed.add_field(name="주간", value="""주간 에포나, 주간 레이드
        어비스 던전, 어비스 레이드
        * 주간 레이드, 어비스 던전, 레이드는 주 1회씩 갈 수 있는데 모든 컨텐츠를 1회씩 가능""", inline=False)
        embed.add_field(name="일간", value="""레이드 수확 2회
        카오스 던전 2회
        에포나 3회
        * 레이드, 카던, 에포나는 휴식 보너스 활용하면 그날 쉬어도 50%는 돌려받을수있음
        + 생활의 기운 소모
        + 영지 활동력 소모 (파견)""", inline=False)
        embed.set_thumbnail(url="https://i.imgur.com/Z6owaEO.jpg")
        embed.set_footer(text="발신자 : 양치맨#7777", icon_url="https://i.imgur.com/3OpkEyM.png")
        await message.channel.send("", embed=embed)
    if message.content == "q":
        embed = discord.Embed(title="", description="", color=0x000000)
        embed.set_image(url="https://i.imgur.com/5cQ7UrP.gif")
        await message.channel.send("", embed=embed)
    if message.content == "w":
        embed = discord.Embed(title="", description="", color=0x000000)
        embed.set_image(url="https://i.imgur.com/atosL4N.gif")
        await message.channel.send("", embed=embed)
    if message.content == "e":
        embed = discord.Embed(title="", description="", color=0x000000)
        embed.set_image(url="https://i.imgur.com/ELnKGB4.gif")
        await message.channel.send("", embed=embed)
    if message.content == "r":
        embed = discord.Embed(title="", description="", color=0x000000)
        embed.set_image(url="https://i.imgur.com/M7v44FH.gif")
        await message.channel.send("", embed=embed)
    if message.content == "웃기":
        embed = discord.Embed(title="", description="", color=0x000000)
        embed.set_image(url="https://i.imgur.com/8EAWyLo.gif")
        await message.channel.send("", embed=embed)
    if message.content == "제드야":
        embed = discord.Embed(title="네", description="", color=0x000000)
        embed.set_image(url="https://i.imgur.com/oqZCMez.gif")
        await message.channel.send("", embed=embed)
    if message.content == "춤춰":
        embed = discord.Embed(title="", description="", color=0x000000)
        embed.set_image(url="https://i.imgur.com/89M4LRh.gif")
        await message.channel.send("", embed=embed)


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
