import discord
from discord.ext import commands
from pprint import pprint
import csv

csv_file = open("./pokemon_status.csv", "r", encoding="utf_8", errors="", newline="")
r = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
rlist = list(r)

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print('Done Login')
    ch_id = 856874019152461847
    chennel = bot.get_channel(ch_id)
    await chennel.send('botがログインしました')


@bot.command()
async def serch(ctx, arg):
    word = arg
    for i in rlist:
        if word in i:
            result = True
            break
        else:
            result = False

    for index, value in enumerate(i):
        if value == '':
            i[index] = '-'


    if result:
        data = i
        embed = discord.Embed(title=word, description=i, color=discord.Colour.green())
        embed.add_field(name="図鑑番号", value=i[0])
        embed.add_field(name="ポケモン名", value=i[1])
        embed.add_field(name=" ", value=" ")
        embed.add_field(name="タイプ１", value=i[2])
        embed.add_field(name="タイプ２", value=i[3])
        embed.add_field(name="通常特性１", value=i[4])
        embed.add_field(name="通常特性２", value=i[5])
        embed.add_field(name="夢特性", value=i[6])
        embed.add_field(name="HP", value=i[7])
        embed.add_field(name="こうげき", value=i[8])
        embed.add_field(name="ぼうぎょ", value=i[9])
        embed.add_field(name="とくこう", value=i[10])
        embed.add_field(name="とくぼう", value=i[11])
        embed.add_field(name="すばやさ", value=i[12])
        embed.add_field(name="合計", value=i[13])
        embed.set_footer(text="made by P4sTela",  # フッターには開発者の情報でも入れてみる
                         icon_url="https://pbs.twimg.com/profile_images/1387009460581801991/OKa0sdnY_400x400.jpg")
        await ctx.reply(i)

    else:
        embed = discord.Embed(title=word, description="Not found!", color=discord.Colour.red())
        await ctx.reply("not found!")

    # await ctx.send(embed=embed)
    # await ctx.reply(i)
token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
