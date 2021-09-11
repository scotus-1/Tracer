import os
import discord
import requests
import aiohttp
from datetime import datetime
from discord.ext import commands

token = os.environ['DISCORD_PRIVATE_KEY']
intents = discord.Intents.default()
intents.members = True
intents.presences = True


# memberList.append(discord.utils.get(client.guilds[0].members, name='scotus*'))

client = commands.Bot(command_prefix='#', intents=intents)
session = aiohttp.ClientSession()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

memberList = []

@client.command()
async def track(ctx, member: discord.Member):
    await ctx.send("Tracking!")
    memberList.append(member)

@client.event
async def on_member_update(before, after):
    embed = {
        "title": "",
        "color": 0,
        "timestamp": "",
        "footer": {
            # "icon_url": "",
            "text": ""
        },
        "thumbnail": {
            "url": ""
        },
        "author": {
            "name": "",
            "icon_url": ""
        },
        "fields": [
            {
                "name": "Before:",
                "value": "",
                "inline": True
            },
            {
                "name": "After:",
                "value": "",
                "inline": True
            }
        ]
    }

    for index, member in enumerate(memberList):
        if member == after:
            if before.status != after.status or before.mobile_status != after.mobile_status:
                if before.status != after.status:
                    platform = 'Desktop'
                    opposite = 'Mobile'
                else:
                    platform = 'Mobile'
                    opposite = 'Desktop'

                if after.nick is not None: nickname = after.name
                else: nickname = after.name

                embed['title'] = f"`{nickname}`'s status (`{after.name}`#`{after.discriminator}` | {platform})"
                embed['color'] = int(str(after.color)[1:], 16)
                embed['timestamp'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z")

                embed['footer']['text'] = f'({opposite}: {after.mobile_status})'

                embed['thumbnail']['url'] = str(after.avatar_url)

                embed['author']['name'] = memberList[index].name + '#' + memberList[index].discriminator
                embed['author']['icon_url'] = str(memberList[index].avatar_url)

                embed['fields'][0]['value'] = str(before.status).upper()
                embed['fields'][1]['value'] = str(after.status).upper()

                print(before.status, after.status)

                response = await session.post(url=os.environ['webhook_url'], json={'embeds':[embed]})
                async with response as resp:
                    print(await resp.text())

client.run(token)
