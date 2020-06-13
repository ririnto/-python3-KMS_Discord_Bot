#!/usr/bin/env python3

import discord
from discord.ext import commands
import csv
from module.hidden import *

server_url = server_url()


def additional_options1(msg, weapon):
    title = ''
    file = "module/database/additional_options/%s.csv" % weapon
    if "해카" in msg[1]:
        msg[1] = "해방"
    if "알리" in msg[1] or "변질" in msg[1] or "해방" in msg[1] or "카이" in msg[1] or "라이트" in msg[1] or "류드" in msg[1]:
        oneline = 1
    else:
        oneline = 0
    with open(file, newline='', encoding='UTF-8') as database:
        freader = csv.reader(database)
        for row_list in freader:
            if oneline is 1:
                target1 = msg[1]
                target2 = row_list[1]
            else:
                target1 = msg[2]
                target2 = row_list[0]
            if target1 in target2:
                if target1 == '1':
                    msg[2] = "1형"
                title = row_list[1]
                data = "기본 공격력 : " + row_list[2] + "\n\n"
                for k in range(1, len(row_list) - 3):
                    data += "☆" * (len(row_list) - 4 - k) + "★" * \
                            k + " : " + row_list[k + 2] + "\n"
                image = server_url + "/image/weapon/%s/%s.png" % (
                    weapon, row_list[len(row_list) - 1])
    if not title:
        output = discord.Embed(
            title="Warning!!!", description='올바른 옵션을 입력하세요.', color=0xff0000)
        output.set_footer(text="#추옵 (셋트 종류) (무기 종류)")
        if oneline is 0:
            with open(file, newline='', encoding='UTF-8') as database:
                freader = csv.reader(database)
                for row_list in freader:
                    target1 = msg[2]
                    target2 = row_list[1]
                    if target1 in target2:
                        title = row_list[1]
                        data = "기본 공격력 : " + row_list[2] + "\n\n"
                        for k in range(1, len(row_list) - 3):
                            data += "☆" * (len(row_list) - 4 - k) + \
                                    "★" * k + " : " + row_list[k + 2] + "\n"
                        image = server_url + "/image/weapon/%s/%s.png" % (
                            weapon, row_list[len(row_list) - 1])
        if title:
            output = discord.Embed(
                title="%s" % title, description='%s' % data, color=0x0000ff)
            output.set_thumbnail(url=image)
    else:
        output = discord.Embed(title="%s" %
                                     title, description='%s' % data, color=0x0000ff)
        output.set_thumbnail(url=image)
    return output


class AddiOptions(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 추옵(self, ctx, *args):
        msg = ['#추옵']
        msg.extend(args)
        if len(msg) is 1:
            output = discord.Embed(title="#추옵", description='#추옵(셋트명) (무기 종류)로 사용 가능합니다.\n무기의 단계별 추옵 수치를 확인하실 수 있습니다.',
                                   color=0x00ff00)
            output.set_footer(text="예) #추옵 우트가르드 케인, #추옵 제로 1형, #추옵 해카세")
        else:
            if msg[1].startswith("알리") \
                    or msg[1].startswith("변질"):
                output = additional_options1(msg, "alicia's_mutated_staff")
            elif msg[1].startswith("아케") \
                    or msg[1].startswith("아셰"):
                output = additional_options1(msg, 'arcane_umbra')
            elif msg[1].startswith("시그") \
                    or msg[1].startswith("여제") \
                    or msg[1].startswith("라이온") \
                    or msg[1].startswith("드래") \
                    or msg[1].startswith("팔콘") \
                    or msg[1].startswith("레이") \
                    or msg[1].startswith("샤크"):
                output = additional_options1(msg, 'cygnus')
            elif msg[1].startswith("파프"):
                output = additional_options1(msg, 'fafnir')
            elif msg[1].startswith("제네"):
                output = additional_options1(msg, 'genesis')
            elif msg[1].startswith("쟈이"):
                output = additional_options1(msg, 'jaihin')
            elif msg[1].startswith("해방") \
                    or msg[1].startswith("해카") \
                    or msg[1].startswith("카이"):
                output = additional_options1(msg, 'liberated_kaiserium')
            elif msg[1].startswith("라이"):
                output = additional_options1(msg, 'lightseeker')
            elif msg[1].startswith("네크"):
                output = additional_options1(msg, 'necro')
            elif msg[1].startswith("반레"):
                output = additional_options1(msg, 'royal_von_leon')
            elif msg[1].startswith("류드"):
                output = additional_options1(msg, "ryude's_sword")
            elif msg[1].startswith("우트"):
                output = additional_options1(msg, 'utgard')
            elif msg[1].startswith("자쿰") \
                    or msg[1].startswith("포이"):
                output = additional_options1(msg, "zakum's_poisonic")
            elif msg[1].startswith("제로") \
                    or msg[1].startswith("라피스") \
                    or msg[1].startswith("라즐리"):
                output = additional_options1(msg, 'zero')
            elif msg[1].startswith("앱솔"):
                output = additional_options1(msg, 'absolab')
            else:
                output = discord.Embed(
                    title="Warning!!!", description='올바른 옵션을 입력하세요.', color=0xff0000)
                output.set_footer(text="#추옵 (셋트 종류) (무기 종류)")

        await ctx.send(embed=output)


def setup(bot):
    bot.add_cog(AddiOptions(bot))
