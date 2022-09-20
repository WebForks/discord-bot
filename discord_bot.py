import discord
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.listen()
async def on_ready():
    print(f'Logged in as {bot.user}') 
  
@bot.listen()
async def on_message(message):
    print(f'Message from {message.author}: {message.content}  ({message.channel})')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)  

@bot.event
async def on_message(message):
    if message.channel.name=='general':
        if message.content == 'hello':
            await message.channel.send('Hello!')
            return

bot.run('Token here')