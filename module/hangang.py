#!/usr/bin/env python3
import discord
from discord.ext import commands
from requests import get
import json


def download():
    with open('module/json/hangang.json', "wb") as file:
        response = get('http://hangang.dkserver.wo.tc/')
        file.write(response.content)


class Hangang(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 한강(self, ctx):
        download()
        with open('module/json/hangang.json') as json_file:
            json_data = json.load(json_file)
            temperature = json_data["temp"]
            time = json_data["time"]

        output = discord.Embed(title="지금 한강 온도", description='%s °C\n최종 업데이트 시간 : %s' % (temperature, time), color=0xff0000)
        output.set_footer(text="도움이 필요하세요? ☎ 1393")

        await ctx.send(embed=output)

def setup(bot):
    bot.add_cog(Hangang(bot))