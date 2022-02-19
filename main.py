import discord
from discord.ext import commands
import csv
from os import getenv

csv_file = open("./VLL2021.csv", "r", encoding="utf_8", errors="", newline="")
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
        embed.add_field(name="サービス名", value=i[0])
        embed.add_field(name="ID", value=i[1])
        embed.add_field(name="管理者", value=i[2])
        embed.add_field(name="リンク", value=i[3])
        embed.add_field(name="説明", value=i[4])
        embed.add_field(name="連携先サービス", value=i[5])
        embed.set_footer(text="made by P4sTela",
                         icon_url="https://pbs.twimg.com/profile_images/1387009460581801991/OKa0sdnY_400x400.jpg")

    else:
        embed = discord.Embed(title=word, description="Not found!", color=discord.Colour.red())
    
    await ctx.send(embed=embed)



# botの機動
bot.run(TOKEN)
