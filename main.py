import discord
from discord.ext import commands
import csv
from os import getenv

csv_file = open("./pokemon_status.csv", "r", encoding="utf_8", errors="", newline="")
r = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
rlist = list(r)

# おまじない(Botの用意)
bot = commands.Bot(command_prefix="!")
TOKEN = getenv('DISCORD_BOT_TOKEN')

#本体
@bot.event
async def on_ready():
    print('Done Login')
    ch_id = 858346308616454167
    chennel = bot.get_channel(ch_id)
    await chennel.send('botがログインしました')

@bot.command()
async def search(ctx, arg):
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
        embed = discord.Embed(title=word, description="I got a special color!", color=discord.Colour.orange())
        embed.add_field(name="図鑑番号", value=i[0])
        embed.add_field(name="ポケモン名", value=i[1])
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
        embed.set_footer(text="made by P4sTela",
                         icon_url="https://pbs.twimg.com/profile_images/1387009460581801991/OKa0sdnY_400x400.jpg")

    else:
        embed = discord.Embed(title=word, description="Not found!", color=discord.Colour.red())
    
    await ctx.send(embed=embed)



# botの機動
bot.run(TOKEN)
