from discord.ext import commands

from module.help import *
from module.simbol import *
from module.additional_options import *
from module.defense_percentage_ignore import *
from module.level import *
from module.information1 import *
from module.informaiton2 import *
from module.hangang import *
from module.logging import *
from module.gambling import *
from module.homepage import *
from module.linknunion import *
from module.BodyAndMindTrainingCenter import *

PREFIX = '#'

extension_list = ['module.help', 'module.simbol',
                  'module.additional_options', 'module.defense_percentage_ignore',
                  'module.level', 'module.hangang',
                  'module.linknunion',
                  'module.BodyAndMindTrainingCenter']

todolist = ['module.gambling', 'module.information', 'module.homepage']

bot = commands.AutoShardedBot(command_prefix=PREFIX)
bot.remove_command('help')

for extension in extension_list:
    bot.load_extension(extension)


# client = discord.Client()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('hello')
    activity = discord.Game(name="#도움말 for help")
    await bot.change_presence(status=discord.Status.idle, activity=activity)


@bot.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith("#"):
        logging_main(message)

    elif message.content.startswith("#정보"):
        status = information_reader(message)
        msg = message.content.split(" ")
        if status is 1:
            output = information_none()
            await message.channel.send(embed=output)
        elif status is 2:
            path = information1(msg)
            await message.channel.send(file=discord.File(path, filename=msg[1] + '.png'))
            output = discord.Embed()
            output.set_footer(text="https://maple.gg/u/%s" % msg[1])
            await message.channel.send(embed=output)
        else:
            output = information_help()
            await message.channel.send(embed=output)

    elif message.content.startswith("#무릉") \
            or message.content.startswith("#시드") \
            or message.content.startswith("#더시드") \
            or message.content.startswith("#유니온") \
            or message.content.startswith("#업적"):
        msg = message.content.split(" ")
        output = information2_main(msg)
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

    await bot.process_commands(message)


try:
    import keys

    key = keys.key
except:
    key = ''

bot.run(key)
