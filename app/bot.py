from urllib import response
import discord
from discord.ext import commands
import requests
import key
bot = commands.Bot(command_prefix='$')

@bot.event 
async def on_ready():
    print("Fire bot is ready!")

@bot.command()
async def helpme(ctx):
    await ctx.reply("""Hi there! I am the Fire Bot! I help predict areas were there might be forest fires using the power of machine learning. 
                    To use me, type $getPrediction followed by the X position, y position, temperatuer, RH, wind, and rain separated by spaces.
                    I will reply to you the area of the forest fire!
                    That's all you have to do! 
                    If you want to take a look at the sample data I was trained on, type $getdata. 
    """)
@bot.command()
async def getdata(ctx):
    response = requests.get("http://127.0.0.1:5000/getdataset")
    data = response.json()
    await ctx.reply(data["data"])

@bot.command()
async def getPrediction(ctx, X, y, temp, RH, wind, rain):
    response = requests.get("http://127.0.0.1:5000/predict/{}/{}/{}/{}/{}/{}".format(X, y, temp, RH, wind, rain))
    data = response.json()
    await ctx.reply(data["prediction"])

bot.run(key.key)