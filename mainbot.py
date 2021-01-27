# Basic imports 

import discord 
import os
from discord.ext import commands 
from secret  import DISCORD_TOKEN


bot = commands.Bot(command_prefix="$")
@bot.command(name="ping")
async def some_crazy_function_name(ctx):
	await ctx.channel.send("pong")


@bot.command(name="echo")
async def print(ctx,*args):
    response=""
    for arg in args:
        response=response+" "+arg
    await ctx.channel.send(response)

bot.run(DISCORD_TOKEN)
