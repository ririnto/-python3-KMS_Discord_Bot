#!/usr/bin/env python3

import discord
import requests
from bs4 import BeautifulSoup
from module.timeout import *


def homepage2(target1, title):
    file = "module/homepage/" + target1 + ".txt"

    with open(file, "r", encoding="utf-8") as file:
        list = file.readlines()

    output = discord.Embed(title=title, color=0x0000ff)

    for i in range(0, len(list), 3):
        output.add_field(name="ㅤ\n" + list[i], value=list[i + 1] + list[i + 2], inline=False)

    return output


@timeout(1)
def homepage1(target1, target2, title):
    result = ''

    url = requests.get("https://maplestory.nexon.com/News/" + target1)
    html = url.content
    soup = BeautifulSoup(html, 'html.parser')

    board = soup.select("div." + target2 + "_board > ul > li")
    list = [[], [], []]

    for i in range(0, len(board)):
        list[0].append(board[i].select('dd')[0].text.strip())
        list[1].append(board[i].select('dd')[1].text.strip())
        list[2].append("https://maplestory.nexon.com" + board[i].select('a')[0].attrs['href'])

    output = discord.Embed(title=title, color=0x0000ff)
    for i in range(0, len(list[0])):
        output.add_field(name="ㅤ\n" + list[0][i], value=list[1][i] + "\n" + list[2][i], inline=False)

    with open("module/homepage/" + target1 + ".txt", "w", encoding="utf-8") as file:
        for i in range(0, len(list[0])):
            for j in range(0, 3):
                result += list[j][i] + "\n"
        file.write(result)

    return output


def homepage_main(msg):
    output = ''
    if '이벤' in msg[0]:
        output = homepage1("Event", "event", "이벤트")
    elif '캐시' in msg[0]:
        output = homepage1("CashShop", "cash", "캐시샵 공지")

    if not output:
        if '이벤' in msg[0]:
            output = homepage2("Event", "이벤트")
        elif '캐시' in msg[0]:
            output = homepage2("CashShop", "캐시샵 공지")

    return output
