#!/usr/bin/env python3

from module.help import *
from module.simbol import *
from module.additional_options import *
from module.defense_percentage_ignore import *
from module.level import *
from module.information import *
from module.hangang import *
from module.logging import *
from module.gambling import *
from module.homepage import *
from module.linknunion import *
from module.BodyAndMindTrainingCenter import *

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('hello')
    activity = discord.Game(name="#도움말 for help")
    await client.change_presence(status=discord.Status.idle, activity=activity)


@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith("#"):
        logging_main(message)

    if message.content.startswith("#help") or message.content.startswith("#도움말"):
        output = help_main()
        await message.channel.send(embed=output)

    if message.content.startswith("#심볼"):
        msg = message.content.split(" ")
        output = simbol_main(msg)
        await message.channel.send(embed=output)

    if message.content.startswith("#추옵"):
        msg = message.content.split(" ")
        output = additional_options_main(msg)
        await message.channel.send(embed=output)

    if message.content.startswith("#방무"):
        msg = message.content.split(" ")
        output = defense_percentage_ignore_main(msg)
        await message.channel.send(embed=output)

    if message.content.startswith("#레벨"):
        msg = message.content.split(" ")
        output = level_main(msg)
        await message.channel.send(embed=output)

    if message.content.startswith("#정보") \
            or message.content.startswith("#무릉") \
            or message.content.startswith("#시드") \
            or message.content.startswith("#더시드") \
            or message.content.startswith("#유니온") \
            or message.content.startswith("#업적"):
        msg = message.content.split(" ")
        output = information_main(msg)
        await message.channel.send(embed=output)

    if message.content.startswith("#한강"):
        output = hangang_main()
        await message.channel.send(embed=output)

    if message.content.startswith("#골드") \
            or message.content.startswith("#애플") \
            or message.content.startswith("#로얄") \
            or message.content.startswith("#원더") \
            or message.content.startswith("#원기") \
            or message.content.startswith("#루나") \
            or message.content.startswith("#남자") \
            or message.content.startswith("#여자") \
            or message.content.startswith("#남성") \
            or message.content.startswith("#여성"):
        msg = message.content.split(" ")
        display_name = message.author.display_name
        output = gambling_main(msg, display_name)
        await message.channel.send(embed=output)

    if message.content.startswith('#이벤') \
            or message.content.startswith("#캐시"):
        msg = message.content.split(" ")
        output = homepage_main(msg)
        await message.channel.send(embed=output)

    if message.content.startswith('#링크'):
        msg = message.content.split(" ")
        output = linknunion_main(msg)
        await message.channel.send(embed=output)

    if message.content.startswith('#심신'):
        msg = message.content.split(" ")
        output = BodyAndMindTrainingCenter_main(msg)
        await message.channel.send(embed=output)


client.run('')
