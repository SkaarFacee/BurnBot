# Basic imports 

import discord 
import os
from discord.ext import commands 
from secret  import DISCORD_TOKEN



intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='$', description="description", intents=intents)
channel = discord.utils.get(ctx.guild.channels, name=)
channel_id = channel.id

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

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
    #await panel.add_reaction('\U0001F44E')

bot.run(DISCORD_TOKEN)
"""
     def check(reaction, user):
            return str(reaction.emoji) == '👍' and user != bot.user
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=30, check=check)
        
        await ctx.send(f"Congratulations {user.name} you won!")
    except asyncio.TimeoutError:
        await ctx.send("You ran out of time!")
"""