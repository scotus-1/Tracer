import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = commands.Bot(command_prefix='#', intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

memberList = []

@client.command()
async def track(ctx, member: discord.Member):
    await ctx.send(member.status)
    memberList.append(member)

@client.event
async def on_member_update(before, after):
    for member in memberList:
        if member == after:
            print(before.status, after.status)


with open('token.txt') as tokenFile:
    token = tokenFile.readline()
    client.run(token)
