#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import discord
import requests
from bs4 import BeautifulSoup
import imgkit
import random


def information1(msg):

    f = open('./module/css/style.css', "r", encoding="utf8")
    css_data = f.read()
    f.close()

    data = '<style>\n%s\n</style>\n' % css_data
    result = [[]]

    url = "https://maple.gg/u/%s" % (msg[1])
    url = requests.get(url)
    html = url.content
    soup = BeautifulSoup(html, 'html.parser')
    finder = soup.select("div#exampleModal > div > div.character-card")

    for i in range(0, 3, 2):
        p_tag = finder[0].select('img')[i]
        del p_tag['crossorigin']

    result.append(finder[0])
    data += '<body>\n'
    data += '%s' % result[1]
    data += '\n</body>'
    f = open('/var/www/html/information/temp.html', "w", encoding="UTF-8")
    f.write(data)
    f.close()
    options = {
        'format': 'png',
        'encoding': "UTF-8",
        "xvfb": "",
        'quiet': '',
        'crop-w': '303',
        'crop-h': '442',
        'crop-x': '360',
        'crop-y': '8'
    }
    with open('/var/www/html/information/temp.html', 'r', encoding="UTF-8") as f:
        imgkit.from_file(f, '/var/www/html/information/temp.png', options=options)

    output = discord.Embed()
    output.set_footer(text="https://maple.gg/u/%s" % msg[1])
    path = '/var/www/html/information/temp.png'
    return path


def information_help(msg):
    output = discord.Embed(title="#정보",
                           description='#정보 (닉네임)을 입력하여 프로필을 확인할 수 있습니다.\n상세 정보 확인을 위해서는 #정보 대신 #무릉, #시드, #유니온, #업적 을 입력해주세요.',
                           color=0x00ff00)
    output.set_footer(text="예) #정보 RIRINTO, #무릉 RIRINTO")
    return output


def information_none():
    output = discord.Embed(title="Warning!!!", description='검색결과가 없습니다.', color=0xff0000)
    output.set_footer(text="캐릭터 이름을 다시 한 번 확인해주세요. 대소문자를 구분하며, 메이플지지의 정보를 기반으로 합니다.")
    return output

def information_reader(message):
    msg = message.content.split(" ")
    if len(msg) is 2:
        url = 'https://maple.gg/u/%s' % msg[1]
        url = requests.get(url)
        html = url.content
        soup = BeautifulSoup(html, 'html.parser')
        finder = soup.select(".bg-light")
        if finder[0].select('h3')[0].text == '검색결과가 없습니다.':
            return 1
        return 2
    else:
        return 3
