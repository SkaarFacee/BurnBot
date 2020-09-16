import os

import discord,random
from secret  import DISCORD_TOKEN
TOKEN = os.getenv(DISCORD_TOKEN)
client = discord.Client()

Indict={"Theres is derpression in your words": " ",
"You were assumed to be straight, why haven't you come out yet": "? Oh yeah you dont have a dick",
"Looks like sugar mama kicked":"out cause he did not do the only thing he was supposed to",
"Only chance of":"getting laid is if he crawls up a chickens butt",
"Listening to what" :"said, I would happily listen to manjusha instead",
" ":"needs to figure out if he has a dick or a pussy first",
"Where is your mom":"Oh yeah seeing you the second you were born, she ran away",
"If people search trans in pornhub":"they get you",
"Stop being anji !":" ",
}

list1,list2=[],[]
for i,j in zip(Indict.keys(),Indict.values()):
    list1.append(i)
    list2.append(j)
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the super secret server, Stay happy till you get kicked ;)'
    )
@client.event
async def on_message(message):
    if(message.author.bot == False):
        if 'happy birthday' in message.content.lower():
            await message.channel.send('Happy Birthday!🎈🎉')
        if message.content == 'ping':
            panel = await message.channel.send('pong')
            await panel.add_reaction('\U0001F3D3')
        if(message.author.bot):
         return
        if message.content == '!ins':
            user = random.choice(message.channel.guild.members)
            author=message.author
            print(user==message.author)
            num =random.randint(0,len(list1))
            for i in range(1000):
                if not user.bot and not user==message.author:
                    response = str(list1[num]) + " {0.mention} ".format(user)+str(list2[num])
                    break
                else:
                    user = random.choice(message.channel.guild.members)
            panel = await message.channel.send(response)
            await panel.add_reaction('\U0001F44D')
            await panel.add_reaction('\U0001F44E')
        elif message.content == 'raise-exception':
            raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise
    
client.run(DISCORD_TOKEN)