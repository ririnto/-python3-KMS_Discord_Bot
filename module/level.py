#!/usr/bin/env python3

import discord
from discord.ext import commands
import csv
import requests
from bs4 import BeautifulSoup
from module.timeout import *


@timeout(3)
def level1(url):
    url = requests.get(url)
    html = url.content
    soup = BeautifulSoup(html, 'html.parser')
    ranking = soup.select(".rank_table_wrap table > tbody > tr")

    result = [[], [], [], [], [], [], []]

    for i in range(0, len(ranking)):
        if ranking[i].select('td')[0].text.strip():
            result[0].append(ranking[i].select('td')[0].text.strip())  # 순위
            result[1].append(ranking[i].select('a')[0].text.strip())  # 닉네임
            result[2].append(ranking[i].select('dd')[0].text.strip())  # 직업 / 직업
            result[3].append(ranking[i].select('td')[2].text.strip())  # 레벨
            result[4].append(ranking[i].select('td')[3].text.strip())  # 경험치량
            result[5].append(ranking[i].select('td')[4].text.strip())  # 인기도
            result[6].append(ranking[i].select('td')[5].text.strip())  # 길드
    return result


def level2(result, msg1, url):
    optlist = [[], [], [], [], [], [], []]
    data = ''
    file = "module/database/level/level.csv"
    if not result:
        output = discord.Embed(title="Warning!!!", description='서버로부터 응답이 없습니다.', color=0xff0000)
        output.set_footer(text="단시간 내 많은 연결 요청으로 발생합니다. 잠시 후 다시 시도해주세요.")
    else:
        for i in range(0, len(result[0])):
            if result[1][i] == msg1:
                for j in range(0, 6):
                    optlist[j] = result[j][i]

        title = optlist[1]

        if not title:
            output = discord.Embed(title="Warning!!!", description='랭킹 정보가 없습니다!', color=0xff0000)
            output.set_footer(text="대소문자를 구분합니다.")
        else:
            now_level = optlist[3]
            now_level = now_level[3:]
            level_250 = str(250)
            level_275 = str(275)

            with open(file, newline='', encoding="utf-8") as database:
                freader = csv.reader(database)
                next(freader)
                for row_list in freader:
                    station_name = row_list[0]
                    if station_name.startswith(now_level):
                        experience_temp = int(row_list[1])
                        accumulate_experience_temp = int(row_list[2])
                    elif station_name.startswith(level_250):
                        accumulate_experience_250 = int(row_list[2])
                    elif station_name.startswith(level_275):
                        accumulate_experience_275 = int(row_list[2])

            temp = optlist[4]
            temp = temp.replace(",", "")
            now_experience = int(temp)
            now_level = int(now_level)

            data += '직업 : %s\n' % optlist[2]
            data += '레벨 : %s\n' % optlist[3]
            if now_level < 275:
                data += '현재 경험치 : %s (%3.2f%%)\n\n' % (
                    format(now_experience, ','), now_experience / experience_temp * 100)
                if now_level < 250:
                    data += "250 까지 남은 경험치 : %s\n" % format(
                        accumulate_experience_250 - accumulate_experience_temp - now_experience, ',')
                data += "275 까지 남은 경험치 : %s\n" % format(
                    accumulate_experience_275 - accumulate_experience_temp - now_experience, ',')

            if not title:
                output = discord.Embed(title="Warning!!!", description='랭킹 정보가 없습니다!', color=0xff0000)
                output.set_footer(text="대소문자를 구분합니다.")
            else:
                output = discord.Embed(title=title, description=data, color=0x0000ff)
                output.set_footer(text=url)

    return output

class Level(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 레벨(self, ctx, *args):
        msg = ['#레벨']
        msg.extend(args)
        if len(msg) is 2:
            empty_result = [[], [], [], [], [], [], []]

            main_url = 'https://maplestory.nexon.com/Ranking/World/Total?c=%s' % msg[1]
            reboot_url = 'https://maplestory.nexon.com/Ranking/World/Total?c=%s&w=254' % msg[1]
            main_result = level1(main_url)

            if main_result == empty_result:
                reboot_result = level1(reboot_url)
                if reboot_result == empty_result:
                    output = discord.Embed(title="Warning!!!", description='랭킹 정보가 없습니다!', color=0xff0000)
                else:
                    output = level2(reboot_result, msg[1], reboot_url)
            else:
                output = level2(main_result, msg[1], main_url)
        else:
            output = discord.Embed(title="#레벨",
                                description='#레벨 (닉네임)으로 사용 가능하며, 현재의 경험치와 250, 275까지 필요한 경험치 량을 나타냅니다.\n메이플스토리 공식 홈페이지의 정보를 활용합니다.',
                                color=0x00ff00)
            output.set_footer(text="예) #레벨 RIRINTO")

        await ctx.send(embed=output)

def setup(bot):
    bot.add_cog(Level(bot))