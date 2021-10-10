import discord
import os
import random
import asyncio
import datetime as dt
from itertools import cycle
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '+e ')


@client.event
async def on_ready():
    print('Bot is ready.')
#    channel = client.get_channel(785994190441021451)
#    await channel.send("miles")


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print("------")



# Message 1
@tasks.loop(hours=24)
async def mytask():
    print('working')
    channel = client.get_channel(805235058167513139)
    await channel.send('miles')

@client.event
async def on_ready():
    mytask.start()

@client.event
async def on_message(message):
    if message.content.find("evan") !=-1:
        await message.channel.send("miles")

""" 
  pokemon channel id: 776964589203095552
@client.event
async def on_message(msg1):
    msg1.content = msg1.content.lower()
    if msg1.content.find("hi") !=-1:
        await msg1.channel.send("hello")
        

@client.event
msg2.content = msg2.content.lower().replace(' ', '')
async def on_message(msg2):
    if msg2.content.find("Hi") !=-1:
        await msg2.channel.send("hello")
        

@client.event
async def on_message(msg3):
    if msg3.content.find("hiii") !=-1:
        await msg3.channel.send("hello")

@client.event
async def on_message(msg4):
    if msg4.content.find("Hi") !=-1:
        await msg4.channel.send("hello")


@client.event
async def on_message(msg5):
    if msg5.content.find("Hii") !=-1:
        await msg5.channel.send("hello")

@client.event
async def on_message(msg6):
    if msg6.content.find("Hiii") !=-1:
        await msg6.channel.send("hello")
 


@msg1.before_loop
async def before_msg1():
    for _ in range(60*60*24): # loop the whole day
        if dt.datetime.now().hour == 10+12: # 24 hour format
            print ('It is time')
            return
        await asyncio.sleep(1) # wait a second before looping again. You can make it more
 
# miles channel id: 761383453735387146

async def on_ready(self):
    if not self.ready:
        self.ready = True
        print("bot ready")

        channel = self.get_channel(761383453735387146)
        await channel.send("miles")

 target_channel_id = 785994190441021451

@tasks.loop(hours=0.08)
async def called_once_a_day():
    message_channel = bot.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    await message_channel.send("miles")

@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

called_once_a_day.start() 


 @client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['Yes.',
                 'No.',
                 'Maybe.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
 """
client.run('token')
