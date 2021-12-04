import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv(dotenv_path='C:/Users/Ben/Desktop/.env')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'sus':
        with open('images/sussy.gif', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)
        f.close()

    elif message.content == 'raise-exception':
        raise discord.DiscordException


@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='real-python'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')
bot.run(TOKEN)

@bot.event
async def on_error(event, *args, **kwargs):
    with open('logs/err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

bot.run(TOKEN)






