#!/usr/bin/env python3

import discord
from discord.ext import commands
import csv


def BodyAndMindTrainingCenter1(msg1, msg2):
    file = "module/database/level/BodyAndMindTrainingCenter.csv"
    time = float(0)
    need = int(0)

    with open(file, newline='', encoding="utf-8") as database:
        freader = csv.reader(database)
        next(freader)
        for row_list in freader:
            if msg1 <= int(row_list[0]) < msg2:
                time += float(row_list[4])
                need += int(row_list[3])
    hour = int(time / 60)
    day = int(hour / 24)

    title = "심신 %d → %d" % (msg1, msg2)
    data = '필요 경험치 : %s\n' % format(need, ',')
    data += '소요 시간 : '
    if day != 0:
        data += "%s일 " % format(day, ',')
    if hour != 0:
        data += "%s시간 " % format((hour - (day * 24)), ',')
    data += "%2.2f분\n\n" % (time - (hour * 60))
    data += "심신수련관 입장 부적(다이아) : %d 개\n" % (int(time / 60 / 18) + 1)
    data += "심신수련관 입장 부적(골드) : %d 개\n" % (int(time / 60 / 9) + 1)
    data += "심신수련관 입장 부적(실버) : %d 개\n" % (int(time / 60 / 3) + 1)
    data += "심신수련관 입장 부적(브론즈) : %d 개\n" % (int(time / 60) + 1)

    output = discord.Embed(title=title, description=data, color=0x0000ff)

    return output

class BnMTrainCenter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 심신(self, ctx, *args):
        msg = ['#심신']
        msg.extend(args)
        if len(msg) == 3:
            if msg[1].isdecimal() and msg[2].isdecimal():
                msg1 = float(msg[1])
                msg2 = float(msg[2])
                if msg1 == int(msg1) and msg2 == int(msg2):
                    msg1 = int(msg1)
                    msg2 = int(msg2)
                    if 105 <= msg1 < 275 and 105 < msg2 <= 275:
                        if msg1 > msg2:
                            output = discord.Embed(title="Warning!!!", description='시작 레벨은 끝 레벨의 값을 넘을 수 없습니다!',
                                                color=0xff0000)
                        else:
                            output = BodyAndMindTrainingCenter1(msg1, msg2)
                    else:
                        output = discord.Embed(title="Warning!!!", description='숫자 범위 초과!', color=0xff0000)
                        output.set_footer(text="105이상, 275이하의 값만 입력해주세요!")
                else:
                    output = discord.Embed(title="Warning!!!", description='데이터는 정수값이어야 합니다!', color=0xff0000)
            else:
                output = discord.Embed(title="Warning!!!", description='두 개의 숫자를 입력하세요!', color=0xff0000)
                output.set_footer(text="예) #심신 105 150")
        else:
            output = discord.Embed(title="#심신",
                                description='#심신 (시작 레벨) (끝 레벨)으로 사용 가능하며, 시작 레벨부터 끝 레벨까지 필요한 심신수련관에서의 시간을 나타냅니다.',
                                color=0x00ff00)
            output.set_footer(text="예) #심신 105 150")

        await ctx.send(embed=output)

def setup(bot):
    bot.add_cog(BnMTrainCenter(bot))