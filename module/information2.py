#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import discord
import requests
from bs4 import BeautifulSoup
import imgkit
import random
import hidden


def achievement(msg, data, i):  # 업적
    temp = [[], [], [], []]
    result = [[], [], [], []]
    temp[0].append(data[i].select('div')[2].text.strip())  # 등급
    temp[1].append(data[i].select('span')[0].text.strip())  # 점수
    temp[2].append(
        data[i].select('span')[1].text.replace("\n", "").replace(" ", "").replace("/", " / ").strip())  # 레벨 / 직업
    temp[3].append(data[i].select('span')[4].text.strip())  # 기준일

    rank = temp[0]

    if "브론즈" in rank:
        rank = "bronze"
    elif "실버" in rank:
        rank = "silver"
    elif "골드" in rank:
        rank = "gold"
    elif "플래티넘" in rank:
        rank = "platinum"
    elif "다이아몬드" in rank:
        rank = "diamond"
    elif "마스터" in rank:
        rank = "master"

    for k in range(0, 4, 1):
        result[k] = temp[k][0]
    output = discord.Embed(title=msg[1],
                           description='%s\n%s\n%s\n%s' % (result[0], result[1], result[2], result[3]),
                           color=0x0000ff)
    output.set_thumbnail(
        url="http://" + serverurl + "/image/achievement/%s.png" % rank)
    output.set_footer(text="https://maple.gg/u/%s" % msg[1])

    return output


def union(msg, data, i):  # 유니온
    temp = [[], [], [], []]
    result = [[], [], [], []]
    temp[0].append(data[i].select('div')[2].text.strip())  # 등급
    temp[1].append(data[i].select('span')[0].text.strip())  # 레벨
    temp[2].append(data[i].select('span')[1].text.lstrip('전투력 ').replace(",", "").strip())  # 전투력
    temp[3].append(data[i].select('span')[4].text.strip())  # 기준일

    num = int(temp[2][0]) * 0.000000864
    num = int(num)
    rank = temp[0][0]

    if "그랜드" in rank:
        rank1 = "grandmaster"
        rank2 = rank.lstrip('그랜드마스터 ')
    elif "마스터" in rank:
        rank1 = "master"
        rank2 = rank.lstrip('마스터 ')
    elif "베테랑" in rank:
        rank1 = "veteran"
        rank2 = rank.lstrip('베테랑 ')
    elif "노비스" in rank:
        rank1 = "novice"
        rank2 = rank.lstrip('노비스 ')

    for k in range(0, 4, 1):
        result[k] = temp[k][0]
    output = discord.Embed(title=msg[1],
                           description='%s\n등급 : %s\n전투력 : %s\n%s\n일일 코인 획득량 : %d' % (
                               result[1], result[0], format(int(result[2]), ','), result[3], num),
                           color=0x0000ff)
    output.set_thumbnail(
        url="http://" + serverurl + "/image/union/%s/%s.png" % (rank1, rank2))
    output.set_footer(text="https://maple.gg/u/%s" % msg[1])

    return output


def information2(msg, data, i):  # 무릉, 더시드
    temp = [[], [], [], []]
    result = [[], [], [], []]
    temp[0].append(data[i].select('h1')[0].text.replace(" ", "").replace("\n", " "))  # 최고층
    temp[1].append(data[i].select('small')[0].text.strip())  # 시간
    temp[2].append(
        data[i].select('span')[1 - i].text.replace("\n", "").replace(" ", "").replace("/", " / ").strip())  # 레벨 / 직업
    temp[3].append(data[i].select('span')[4 - i].text.lstrip('기준일: ').strip())  # 날짜

    for k in range(0, 4, 1):
        result[k] = temp[k][0]
    output = discord.Embed(title=msg[1],
                           description='%s\n기록 : %s\n시간 : %s\n날짜 : %s' % (result[2], result[0], result[1], result[3]),
                           color=0x0000ff)
    output.set_footer(text="https://maple.gg/u/%s" % msg[1])
    return output


def information2_main(msg):
    if len(msg) is 2:
        url = 'https://maple.gg/u/%s' % msg[1]
        url = requests.get(url)
        html = url.content
        soup = BeautifulSoup(html, 'html.parser')
        finder = soup.select(".bg-light")
        if finder[0].select('h3')[0].text == '검색결과가 없습니다.':
            output = discord.Embed(title="Warning!!!", description='검색결과가 없습니다.', color=0xff0000)
            output.set_footer(text="캐릭터 이름을 다시 한 번 확인해주세요. 대소문자를 구분하며, 메이플지지의 정보를 기반으로 합니다.")
        else:
            if '정보' in msg[0]:
                output = information1(msg)
            else:
                data = soup.select("div.bg-light > section > div > div")
                if '무릉' in msg[0]:
                    if data[0].select('div')[2].text == '기록이 없습니다.':
                        output = discord.Embed(title="Warning!!!", description='기록이 없습니다.', color=0xff0000)
                        output.set_footer(text="https://maple.gg/u/%s" % msg[1])
                    else:
                        output = information3(msg, data, 0)
                elif '시드' in msg[0]:
                    if data[1].select('div')[2].text == '기록이 없습니다.':
                        output = discord.Embed(title="Warning!!!", description='기록이 없습니다.', color=0xff0000)
                        output.set_footer(text="https://maple.gg/u/%s" % msg[1])
                    else:
                        output = information3(msg, data, 1)
                elif '유니온' in msg[0]:
                    if data[2].select('div')[2].text == '기록이 없습니다.':
                        output = discord.Embed(title="Warning!!!", description='기록이 없습니다.', color=0xff0000)
                        output.set_footer(text="https://maple.gg/u/%s" % msg[1])
                    else:
                        output = union(msg, data, 2)
                elif '업적' in msg[0]:
                    if data[3].select('div')[2].text == '기록이 없습니다.':
                        output = discord.Embed(title="Warning!!!", description='기록이 없습니다.', color=0xff0000)
                        output.set_footer(text="https://maple.gg/u/%s" % msg[1])
                    else:
                        output = achievement(msg, data, 3)
    else:
        output = discord.Embed(title="#정보",
                               description='#정보 (닉네임)을 입력하여 프로필을 확인할 수 있습니다.\n상세 정보 확인을 위해서는 #정보 대신 #무릉, #시드, #유니온, #업적 을 입력해주세요.',
                               color=0x00ff00)
        output.set_footer(text="예) #정보 RIRINTO, #무릉 RIRINTO")

    return output
