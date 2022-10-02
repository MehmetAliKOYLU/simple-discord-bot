import discord
from discord.ext import commands
from Bot_commands import *
intents=discord.Intents(messages=True,guilds=True,reactions=True,members=True,presences=True,message_content = True)

token="TOKEN"#if you don't know where the token is located, follow the steps in the readme section

Bot=commands.Bot(command_prefix='',intents=intents)#in the command prefix section(''), it determines how the commands will work

@Bot.event
async def on_ready():
    print("I'm ready!!") #if you see this message, our bot has worked
@Bot.event
async def on_message(message):
    if message.author == Bot.user:
        return
    message.content=message.content.lower()
    if message.content == 'hi':  #write the word you want to be answered
        await message.channel.send('hello ^^')


Bot.run(token)
