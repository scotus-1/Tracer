import discord
from discord.ext import commands

client = commands.Bot(command_prefix='*')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#
#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

@client.command()
async def hello(ctx):
    await ctx.send('Hello!')


client.run('NzY2NTIyMDAyNDMyNTg5ODU1.X4klPg.HDQwrA4MqNoei6pMnHsShm3dO7w')

