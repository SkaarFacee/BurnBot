# Basic imports 
import time
import discord # For discord
from discord.ext import commands # For discord
import logging # For logging
from pathlib import Path # For paths
from secret  import DISCORD_TOKEN

# Defining a few things
bot = commands.Bot(command_prefix='$', case_insensitive=True,owner_id=692754016186138726)
bot.config_token = DISCORD_TOKEN
logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: -\n-----")
    # Another way to use variables in strings
    print("-----\nLogged in as: {} : {}\n-----\nMy current prefix is: -\n-----".format(bot.user.name, bot.user.id))
    await bot.change_presence(activity=discord.Game(name=f"Hi, my names {bot.user.name}.\nUse $ to interact with me!")) # This changes the bots 'activity'

@bot.command(name="ping")
async def some_crazy_function_name(ctx):
	await ctx.channel.send("pong")

""" SUPPOSED TO GET ALL REACTIONS
@commands.command()
async def ga(self, ctx):
    channel = self.bot.get_channel(channel_id)
    message = await channel.fetch_message(message_id)
    users = set()
    for reaction in message.reactions:
        async for user in reaction.users():
            users.add(user)
    await ctx.send(f"users: {', '.join(user.name for user in users)}")
"""





@bot.command(name="remind")
async def print(ctx,*args):
    #print(discord.ext.commands.Bot.get_all_members())
    response=""
    for arg in args:
        response=response+" "+arg
    
    #make the embed
    embed=discord.Embed(
        title = "{} has made a reminder:".format(ctx.message.author.name),
        description = response,
        colour=discord.Colour.dark_blue()
    )
    panel =await ctx.channel.send(embed=embed)
    await panel.add_reaction('\U0001F44D')
    time.sleep(5)
    message_id = panel.id
    message_react=panel.reactions
    await ctx.channel.send(f"Reactions are {message_react}")
    #await panel.add_reaction('\U0001F44E')

bot.run(bot.config_token )
"""
     def check(reaction, user):
            return str(reaction.emoji) == '👍' and user != bot.user
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=30, check=check)
        
        await ctx.send(f"Congratulations {user.name} you won!")
    except asyncio.TimeoutError:
        await ctx.send("You ran out of time!")
"""