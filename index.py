import discord
from discord import embeds
from discord.ext import commands
from discord.ext.commands.core import command
import datetime

robot = commands.Bot(command_prefix=">")


@robot.command()
async def ping(ctx):
    await ctx.send("pong")

@robot.command()
async def sum(ctx, numOne: int,  numTwo: int):
    await ctx.send(numOne + numTwo)
    
@robot.command()
async def info(ctx):
    embed = discord.Embed(Title=f"{ctx.guild.name}", description="svsvsss", timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed)

#events=
@robot.event
async def on_ready():
    print("Bot Encendido !")
    











robot.run("ODgwMTk2Mjk1MjI1MTI2OTYy.YSawrg.r06T-YLfEupvcaVlDrw6VNCsj8Y")

