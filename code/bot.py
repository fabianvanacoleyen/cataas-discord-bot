import discord
from discord.ext import commands
import requests
import image

intents = discord.Intents.default()
intents.message_content = True								
bot = commands.Bot(command_prefix="$", intents=intents)    

@bot.event
async def on_ready():
    print(f'we succesfully logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:  	
        return  						

    if message.content.lower() == '!catimg':
        cat_file = image.save_image()
        await message.channel.send(file=discord.File(cat_file))

with open('token.txt', 'r') as file:
    discord_token = file.read()
bot.run(discord_token)
