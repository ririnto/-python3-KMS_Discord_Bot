#!/usr/bin/env python3

import discord
from discord.ext import commands
import csv
from module.changename import *
import module.hidden


def linknunion1(msg):
    title = ''
    linkfile = "module/database/linknunion/linkskill.csv"
    unionfile = "module/database/linknunion/union.csv"
    image = False
    name = ''
    for i in range(1, len(msg)):
        name += msg[i]

    name = changename(name)

    with open(linkfile, newline='', encoding='UTF-8') as database:
        freader = csv.reader(database)
        for row_list in freader:
            if name.replace(" ", "") in row_list[0].replace(" ", ""):
                subtitle = row_list[1]
                value2 = row_list[2]
                image = "http://" + serverurl + "/image/linkskill/%s.png" % \
                        row_list[3]

    with open(unionfile, newline='', encoding='UTF-8') as database:
        freader = csv.reader(database)
        for row_list in freader:
            if name.replace(" ", "") in row_list[0].replace(" ", ""):
                title = row_list[0]
                value1 = row_list[1]
    if image:
        output = discord.Embed(title=title, color=0x0000ff)
        output.add_field(name="공격대원 효과", value=value1, inline=False)
        output.add_field(name=subtitle, value=value2, inline=False)
        output.set_image(url=image)
    else:
        output = discord.Embed(title="Warning!!!", description='올바른 옵션을 입력하세요.',
                               color=0xff0000)
        output.set_footer(text="예) #링크 키네시스, #링크 제로")
    return output


class Linknunion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 링크(self, ctx, *args):
        msg = ['#링크']
        msg.extend(args)
        if len(msg) is not 1:
            output = linknunion1(msg)
        else:
            output = discord.Embed(title="#링크", description='#링크 (직업명) 으로 사용 가능합니다.\n명령어 입력 시 해당 직업의 유니온 효과와 링크스킬을 확인하실 수 있습니다.', color=0x00ff00)
            output.set_footer(text="예) #링크 키네시스, #링크 제로")
        
        await ctx.send(embed=output)

def setup(bot):
    bot.add_cog(Linknunion(bot))