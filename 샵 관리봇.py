import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print("MADE BY 수한 (NO 24HOURS)")

cid = 881106855882010730
tid = 881106855882010730
gid = 881106855412252717
dii = 881106855882010730
aid = 687160850644992030, 750224361755115531
gtid = 881108475747401738
lid = 881106855882010730
token = "ODgxMTE3NTc1MjQ3OTc0NDMw.YSoKsA.sncK2cLp52DD8DJKZydtasTPUr4"

@client.event
async def on_message(message):
    if message.content.startswith("!출근"):
        if message.author.id == aid:
            if message.channel.id == dii:
                embed = discord.Embed(title=f"{message.author.name}님이 출근하셨습니다.", color=0x00ff00)
                await client.get_channel(int(cid)).send (embed=embed)

    if message.content.startswith("!퇴근"):
        if message.author.id == aid:
            if message.channel.id == dii:
                embed = discord.Embed(title=f"{message.author.name}님이 퇴근하셨습니다.", color=0x00ff00)
                await client.get_channel(int(tid)).send (embed=embed)


    if message.content.startswith("!공지"):
        if message.author.id == aid:
            if message.channel.id == dii:
                msg = message.content[4:]
                embed = discord.Embed(title="공지사항", color=0x000000)
                embed.set_footer(text=msg)
                await client.get_channel(int(gid)).send (embed=embed)

    if message.content.startswith('!블랙리스트'):
        if message.author.guild_permissions.ban_members:
            try:
                target = message.mentions[0]
            except:
                await message.channel.send('유저가 지정되지 않았습니다')
                return

            j = message.content.split(" ")
            try:
                reason = j[2]
            except IndexError:
                reason = 'None'
            embed = discord.Embed(title='블랙리스트',
                                  description=f'{target}님이 {message.guild.name} 블랙리스트에 추가되었습니다.\n사유: {reason}',
                                  colour=discord.Colour.red())
            try:
                await target.send(embed=embed)
            except:
                pass
            embed = discord.Embed(title="블랙리스트 추가", color=0x000000)
            embed.add_field(name="닉네임", value=str(target), inline=False)
            embed.add_field(name="아이디", value=str(target.id), inline=False)
            embed.add_field(name="사유", value=str(reason), inline=False)
            await client.get_channel(int(gtid)).send(embed=embed)
            await target.ban(reason=reason)

client.run(token)