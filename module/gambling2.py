#!/usr/bin/env python3

import discord
import random
import requests
from bs4 import BeautifulSoup
from module.timeout import *


@timeout(1)
def gambling(msg, display_name, title, target, times):
    url = requests.get("https://maplestory.nexon.com/Guide/CashShop/Probability/%s" % target)
    html = url.content
    soup = BeautifulSoup(html, 'html.parser')

    list = soup.select("div#container > div.div_inner > div.contents_wrap > table.my_page_tb2 > tr")

    itemname = []
    percentage = []
    startpoint = []
    endpoint = []
    randomlist = []
    resultlist = []
    result = ''

    if "Coupon" in target:
        if "남자" in msg[0] or "남성" in msg[0]:
            for i in range(1, 7):
                itemname.append(list[i].select('span')[0].text.strip())  # 아이템명
                if "%" in list[i].select('td')[1].text.strip():
                    percentage.append(float(list[i].select('td')[1].text.strip().rstrip('%')) * 0.01)  # 확률
                else:
                    percentage.append(float(list[i].select('td')[2].text.rstrip('%').strip()) * 0.01)  # 확률
        else:
            for i in range(7, 13):
                itemname.append(list[i].select('span')[0].text.strip())  # 아이템명
                if "%" in list[i].select('td')[1].text.strip():
                    percentage.append(float(list[i].select('td')[1].text.strip().rstrip('%')) * 0.01)  # 확률
                else:
                    percentage.append(float(list[i].select('td')[2].text.rstrip('%').strip()) * 0.01)  # 확률
    else:
        for i in range(1, len(list)):
            itemname.append(list[i].select('span')[0].text.strip())  # 아이템명
            if "%" in list[i].select('td')[1].text.strip():
                percentage.append(float(list[i].select('td')[1].text.strip().rstrip('%')) * 0.01)  # 확률
            else:
                percentage.append(float(list[i].select('td')[2].text.rstrip('%').strip()) * 0.01)  # 확률

    endpoint.append(percentage[0])
    for i in range(1, len(percentage)):
        endpoint.append(percentage[i] + endpoint[i - 1])  # 끝 지점 확률
    startpoint.append(float(0))
    for i in range(1, len(percentage)):
        startpoint.append(endpoint[i - 1])  # 시작 지점 확률
        
    if times == 0:
        randomnumber = random.randrange(0, int(endpoint[len(endpoint) - 1] * 10000000))  # 랜덤한 숫자 한 개 선정
        if 0 == times:
            for i in range(0, len(itemname)):
                if startpoint[i] <= randomnumber / 10000000 < endpoint[i]:
                    getitem = itemname[i]
        if "헤어" in title:
            output = discord.Embed(title="로얄 헤어 쿠폰",
                                   description='%s님의 헤어가 %s 로 변경되었습니다.' % (display_name, getitem),
                                   color=0x0000ff)
        elif "성형" in title:
            output = discord.Embed(title="로얄 성형 쿠폰",
                                   description='%s님의 얼굴이 %s 로 변경되었습니다.' % (display_name, getitem),
                                   color=0x0000ff)
        else:
            output = discord.Embed(title="%s" % title,
                                   description='%s님이 %s 을(를) 획득하였습니다.' % (display_name, getitem),
                                   color=0x0000ff)
    else:
        for i in range(0, times):
            randomlist.append(random.randrange(0, int(endpoint[len(endpoint) - 1] * 10000000)))  # 랜덤한 숫자를 times 만큼 리스트에 저장
        for i in range(0, times):
            for j in range(0, len(itemname)):
                if startpoint[j] <= randomlist[i] / 10000000 < endpoint[j]:  # 랜덤한 숫자 i가 있는 itemname을 찾아 resultlist에 저장
                    resultlist.append(itemname[j])
        for i in range(0, len(itemname)):
            for j in range(0, times):  # 정렬
                if resultlist[j] in itemname[i]:
                    if resultlist[j] not in result:
                        result += "%s : %d\n" % (resultlist[j], resultlist.count(resultlist[j]))
        output = discord.Embed(title="%s %d회 결과" % (title, times), description='%s' % result, color=0x0000ff)
        output.set_footer(text="도박중독, 당신의 가정을 무너뜨릴 수 있습니다. ☎1336")

    return output


def gambling_main(msg, display_name):
    output = ''
    if len(msg) is 1:
        times = 0
        if '골드' in msg[0] or '애플' in msg[0]:
            output = gambling(msg, display_name, "골드애플", "GoldApple", times)
        elif '로얄' in msg[0]:
            output = gambling(msg, display_name, "로얄스타일", "RoyalStyle", times)
        elif '원더' in msg[0] or '원기' in msg[0]:
            output = gambling(msg, display_name, "위습의 원더베리", "WispsWonderBerry", times)
        elif '루나' in msg[0]:
            output = discord.Embed(title="#루나", description='#루나 (옵션)으로 사용 가능하며, 옵션으로 사용 가능한 항목은 스윗/드림 입니다.',
                                   color=0x00ff00)
            output.set_footer(text="예) #루나 스윗")
        elif '남자' in msg[0] or '남성' in msg[0] or '여자' in msg[0] or '여성' in msg[0]:
            output = discord.Embed(title="#남자/여자", description='#남자/여자 (옵션)으로 사용 가능하며, 옵션으로 사용 가능한 항목은 헤어/성형 입니다.',
                                   color=0x00ff00)
            output.set_footer(text="예) #남자 성형")
    elif len(msg) is 2:
        if '루나' in msg[0]:
            times = 0
            if '스윗' in msg[1]:
                output = gambling(msg, display_name, "루나 크리스탈 스윗", "LunaCrystalSweet", times)
            elif '드림' in msg[1]:
                output = gambling(msg, display_name, "루나 크리스탈 드림", "LunaCrystalDream", times)
            else:
                output = discord.Embed(title="Warning!!!", description='올바른 옵션을 입력하세요.', color=0xff0000)
                output.set_footer(text="예) #루나 스윗/드림")
        elif '남자' in msg[0] or '남성' in msg[0]:
            times = 0
            if '헤어' in msg[1] or '머리' in msg[1]:
                output = gambling(msg, display_name, "헤어", "RoyalHairCoupon", times)
            elif '성형' in msg[1] or '얼굴' in msg[1]:
                output = gambling(msg, display_name, "성형", "RoyalPlasticSurgeryCoupon", times)
            else:
                output = discord.Embed(title="Warning!!!", description='올바른 옵션을 입력하세요.', color=0xff0000)
                output.set_footer(text="예) #남자 헤어/성형")
        elif '여자' in msg[0] or '여성' in msg[0]:
            times = 0
            if '헤어' in msg[1] or '머리' in msg[1]:
                output = gambling(msg, display_name, "헤어", "RoyalHairCoupon", times)
            elif '성형' in msg[1] or '얼굴' in msg[1]:
                output = gambling(msg, display_name, "성형", "RoyalPlasticSurgeryCoupon", times)
            else:
                output = discord.Embed(title="Warning!!!", description='올바른 옵션을 입력하세요.', color=0xff0000)
                output.set_footer(text="예) #여자 헤어/성형")
        else:
            if msg[1].isdecimal():
                times = int(float(msg[1]))
                if '로얄' in msg[0] and msg[1].isdecimal():
                    if 0 < times <= 1000:
                        output = gambling(msg, display_name, "로얄스타일", "RoyalStyle", times)
                    else:
                        output = discord.Embed(title="Warning!!!", description='1 ~ 1000 의 횟수를 지정해주세요.', color=0xff0000)
                elif ('원더' in msg[0] or '원기' in msg[0]) and msg[1].isdecimal():
                    if 0 < times <= 1000:
                        output = gambling(msg, display_name, "위습의 원더베리", "WispsWonderBerry", times)
                    else:
                        output = discord.Embed(title="Warning!!!", description='1 ~ 1000 의 횟수를 지정해주세요.', color=0xff0000)
                elif ('골드' in msg[0] or '애플' in msg[0]) and msg[1].isdecimal():
                    if 0 < times <= 100:
                        output = gambling(msg, display_name, "골드애플", "GoldApple", times)
                    else:
                        output = discord.Embed(title="Warning!!!", description='1 ~ 100 의 횟수를 지정해주세요.', color=0xff0000)
            else:
                output = discord.Embed(title="Warning!!!", description='올바른 옵션을 입력하세요.', color=0xff0000)
                output.set_footer(
                    text="#골드애플 (횟수), 골드애플과 로얄스타일, 원더베리를 시뮬레이션 할 수 있으며, 횟수 옵션이 없으면 1회 시행합니다. #루나 스윗/드림은 횟수를 지정할 수 없습니다.")
    else:
        output = discord.Embed(title="Warning!!!", description='올바른 옵션을 입력하세요.', color=0xff0000)
        output.set_footer(
            text="#골드애플 (횟수), 골드애플과 로얄스타일, 원더베리를 시뮬레이션 할 수 있으며, 횟수 옵션이 없으면 1회 시행합니다. #루나 스윗/드림, #남자/여자 헤어/성형 은 횟수를 지정할 수 없습니다.")

    if not output:
        output = discord.Embed(title="Warning!!!", description='서버로부터 응답이 없습니다.', color=0xff0000)
        output.set_footer(text="단시간 내 많은 연결 요청으로 발생합니다. 잠시 후 다시 시도해주세요.")

    return output
