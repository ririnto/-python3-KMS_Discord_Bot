#!/usr/bin/env python3

import discord
from discord.ext import commands

def defense_percentage_ignore1(defense_percentage_ignore, percentage):
    monster_damage_percentage = 1 - (percentage * (1 - defense_percentage_ignore))
    if monster_damage_percentage < 0:
        monster_damage_percentage = 0
    return monster_damage_percentage


class DefperIgnore(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 방무(self, ctx, *args):
        msg = ['#방무']
        msg.extend(args)
        if len(msg) is 1:
            output = discord.Embed(title="#방무",
                                description='#방무 (방어율 무시 1) (방어율 무시 2)... (방어율 무시 n)로 사용 가능하며, 몬스터에게 들어가는 데미지율을 확인할 수 있습니다.',
                                color=0x00ff00)
            output.set_footer(text="예) #방무 85 40 20")
        else:
            num = 2
            for i in msg:
                if not i.isdecimal():
                    num = num - 1
            if num is 1:
                defense_percentage_ignore = 1
                defense_percentage_ignore_options = list(range(1, len(msg), 1))
                for i in defense_percentage_ignore_options:
                    defense_percentage_ignore = defense_percentage_ignore * (1 - float(msg[i]) / 100)
                defense_percentage_ignore = 1 - defense_percentage_ignore

                if defense_percentage_ignore > 1:
                    output = discord.Embed(title="Warning!!!", description='방어율 무시는 100%를 넘을 수 없습니다.', color=0xff0000)
                    output.set_footer(text="#방무 (방어율 무시 1) (방어율 무시 2)... (방어율 무시 n)")
                else:
                    output = discord.Embed(title="방어율 무시 %3.2f %% 몬스터 공격 시 데미지" % (defense_percentage_ignore * 100),
                                        description="방어율 100%% 몬스터 공격 시 데미지 : %3.2f %%\n"
                                                    "방어율 150%% 몬스터 공격 시 데미지 : %3.2f %%\n"
                                                    "방어율 200%% 몬스터 공격 시 데미지 : %3.2f %%\n"
                                                    "방어율 250%% 몬스터 공격 시 데미지 : %3.2f %%\n"
                                                    "방어율 300%% 몬스터 공격 시 데미지 : %3.2f %%\n"
                                                    % (defense_percentage_ignore1(defense_percentage_ignore, 1) * 100,
                                                        defense_percentage_ignore1(defense_percentage_ignore, 1.5) * 100,
                                                        defense_percentage_ignore1(defense_percentage_ignore, 2) * 100,
                                                        defense_percentage_ignore1(defense_percentage_ignore, 2.5) * 100,
                                                        defense_percentage_ignore1(defense_percentage_ignore, 3) * 100),
                                        color=0x0000ff)
            else:
                output = discord.Embed(title="Warning!!!", description='#방무 의 옵션에는 숫자만 입력 가능합니다.', color=0xff0000)
                output.set_footer(text="#방무 85 40 20")

        await ctx.send(embed=output)

def setup(bot):
    bot.add_cog(DefperIgnore(bot))