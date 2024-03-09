import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True  # Enable intents for receiving message content

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()  # Use the bot.command() decorator to register a command
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.display_name}.')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

bot.run(DISCORD_TOKEN)
