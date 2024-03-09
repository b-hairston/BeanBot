import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import requests
import random
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
from io import BytesIO
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
SEARCH_ENGINE_ID = os.getenv('SEARCH_ENGINE_ID')



intents = discord.Intents.default()
intents.message_content = True  # Enable intents for receiving message content

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()  # Use the bot.command() decorator to register a command
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.display_name}.')
@bot.command()
async def image(ctx, *, search_query):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "q": str(search_query),  # Ensuring the query is treated as a phrase
        "searchType": "image",
        "imgColorType": "color",  # Only fetch color image
        "num": 10   }
    
    response = requests.get(search_url, params=params).json()
    
    print(response)
    
    if 'items' in response:
        random_image_url = random.choice(response['items'])['link']
        await ctx.send(random_image_url)
    else:

        await ctx.send(f"I couldn't find any {search_query}. :sob:")
        
@bot.command()
async def deepfry(ctx, * , search_query):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "q": str(search_query),  # Ensuring the query is treated as a phrase
        "searchType": "image",
        "imgColorType": "color",  # Only fetch color image
        "num": 10   }
    response = requests.get(search_url, params=params).json()
    
    print(response)
    
    if 'items' in response:
        random_image_url = random.choice(response['items'])['link']
        image = Image.open(BytesIO(requests.get(random_image_url).content))
        
        enhancer = ImageEnhance.Sharpness(image)
        image = enhancer.enhance(5)
        
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(5)
        
        enhancer = ImageEnhance.Color(image)
        image = enhancer.enhance(5)
        
        
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        
        output_image_path = "deepfried_image.jpg"
        image.save(output_image_path)
        await ctx.send(file=discord.File(output_image_path))
        
        

        
    else:
        await ctx.send(f"I couldn't find any {search_query}. :sob:")
    
    
        
    
        
    
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

bot.run(DISCORD_TOKEN)
