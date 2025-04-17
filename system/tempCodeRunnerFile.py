import discord, asyncio, datetime, pytz
import yaml


with open('config.yaml', encoding='UTF-8') as f:
    _cfg = yaml.load(f, Loader=yaml.FullLoader)
DISCORD_BOT_TOKEN = _cfg["DISCORD_BOT_TOKEN"]


intents = discord.Intents.default()
client = discord.Client(intents=intents)


# 봇 온라인 접속
@client.event
async def on_ready():
    print("JARVIS on online")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("안녕하세요, 주인님"))

@client.event
async def on_message(message):

    if message.author.name == 'wontothree': # 메세지 감지

        # 작성된 채널에 메시지를 보낸다.
        await message.channel.send ("{} | {}, 반응 출력".format(message.author, message.author.mention))

        # 메시지 작성자에게 DM을 보낸다.
        # await message.author.send ("{} | {}, User, hello".format(message.author, message.author.mention))

    # 특정 채널에 출력
    if message.author.name == 'wontothree':
        channel = client.get_channel(1196505285691453572)
        await channel.send("{} | {}, 특정 채널에 출력".format(message.author, message.author.mention))
    
    # Imbedding
    if message.author.name == 'wontothree':
        embed = discord.Embed(title="Title", description="Subtitle", timestamp=datetime.datetime.now(pytz.timezone('UTC')), colour=10038562)

        embed.add_field(name="임베드 라인 1 - inline = false로 설정", value="라인 이름에 해당하는 값", inline=False)
        embed.add_field(name="임베드 라인 1 - inline = false로 설정", value="라인 이름에 해당하는 값", inline=False)

        embed.add_field(name="임베드 라인 1 - inline = false로 설정", value="라인 이름에 해당하는 값", inline=True)
        embed.add_field(name="임베드 라인 1 - inline = false로 설정", value="라인 이름에 해당하는 값", inline=True)

        embed.set_footer(text="JARVIS made by. wontothree", icon_url="")
        # embed.set_thumbnail(url-"")
        await message.channel.send(embed=embed)
                              

# Token of bot
client.run('DISCORD_BOT_TOKEN')

