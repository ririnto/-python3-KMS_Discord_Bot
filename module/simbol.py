#!/usr/bin/env python3

import discord
from discord.ext import commands


def simbol1(a, b):
    result1 = 0
    result2 = 0
    for i in range(1, a):
        result1 += (i * i) + 11
    for i in range(1, b):
        result2 += (i * i) + 11
    result = result2 - result1
    return format(result, ',')


def simbol2(a, b):
    result1 = 0
    result2 = 0
    for i in range(1, a):
        result1 += 2370000 + (7130000 * i)
    for i in range(1, b):
        result2 += 2370000 + (7130000 * i)
    result = result2 - result1
    return format(result, ',')


def simbol3(a, b):
    result1 = 0
    result2 = 0
    for i in range(1, a):
        result1 += 12440000 + (6600000 * i)
    for i in range(1, b):
        result2 += 12440000 + (6600000 * i)
    result = result2 - result1
    return format(result, ',')


class Simbol(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 심볼(self, ctx, *args):
        msg = ['#심볼']
        msg.extend(args)
        if len(msg) == 3:
            if msg[1].isdecimal() and msg[2].isdecimal():
                msg1 = float(msg[1])
                msg2 = float(msg[2])
                if msg1 == int(msg1) and msg2 == int(msg2):
                    msg1 = int(msg1)
                    msg2 = int(msg2)
                    if 0 < msg1 < 21 and 0 < msg2 < 21:
                        if msg1 > msg2:
                            output = discord.Embed(title="Warning!!!", description='옵션 1은 옵션 2의 값을 넘을 수 없습니다!',
                                                   color=0xff0000)
                            return output
                        else:
                            output = discord.Embed(title="심볼 %d → %d" % (msg1, msg2),
                                                   description='필요 성장치 : %s \n 소멸의 여로 심볼 강화 비용 : %s \n 츄레아모에 심볼 강화 비용 : %s'
                                                   % (simbol1(msg1, msg2), simbol2(msg1, msg2),
                                                      simbol3(msg1, msg2)), color=0x0000ff)
                            return output
                    else:
                        output = discord.Embed(
                            title="Warning!!!", description='숫자 범위 초과!', color=0xff0000)
                        output.set_footer(text="1이상, 20 이하의 정수만 입력해주세요!")
                        return output
                else:
                    output = discord.Embed(
                        title="Warning!!!", description='데이터는 정수값이어야 합니다!', color=0xff0000)
            else:
                output = discord.Embed(
                    title="Warning!!!", description='두 개의 숫자를 입력하세요!', color=0xff0000)
                output.set_footer(text="#심볼 (옵션1) (옵션2)")
        else:
            output = discord.Embed(
                title="#심볼", description='#심볼 (옵션1) (옵션2)을 입력하여 (옵션1)부터 (옵션2) 까지 심볼을 레벨업하는 데  필요한 심볼 갯수, 메소를 확인할 수 있습니다.', color=0x00ff00)
            output.set_footer(text="#심볼 7 12")

        await ctx.send(embed=output)


def setup(bot):
    bot.add_cog(Simbol(bot))
