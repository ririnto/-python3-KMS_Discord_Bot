#!/usr/bin/env python3

import discord
import csv
import random


def gambling2(times, title, target):
    file = "module/database/gambling/%s.csv" % target
    maxnumber = float(0)
    with open(file, newline='', encoding='UTF-8') as database:  # 확률 총합 확인
        freader = csv.reader(database)
        next(freader)
        for row_list in freader:
            if maxnumber < float(row_list[3]):
                maxnumber = float(row_list[3])
    resultlist = []
    for i in range(0, times):  # 결과 누적 
        randomnumber = random.randrange(0, int(maxnumber*10000000))
        file = "module/database/gambling/%s.csv" % target
        with open(file, newline='', encoding='UTF-8') as database:
            freader = csv.reader(database)
            next(freader)
            for row_list in freader:
                if float(row_list[2]) <= randomnumber/10000000 < float(row_list[3]):
                    resultlist.append(row_list[0])
    result = ""
    with open(file, newline='', encoding='UTF-8') as database:  # 정렬
        freader = csv.reader(database)
        next(freader)
        for row_list in freader:
            for i in range(0, len(resultlist)):
                if resultlist[i] in row_list[0]:
                    if resultlist[i] not in result:
                        result += "%s : %d\n" % (resultlist[i], resultlist.count(resultlist[i]))
    output = discord.Embed(title="%s %d회 결과" % (title, times), description='%s' % result, color=0x0000ff)
    output.set_footer(text="도박중독, 당신의 가정을 무너뜨릴 수 있습니다. ☎1336")
    return output


def gambling1(display_name, title, target):
    file = "module/database/gambling/%s.csv" % target
    maxnumber = float(0)
    with open(file, newline='', encoding='UTF-8') as database:  # 확률 총합 확인
        freader = csv.reader(database)
        next(freader)
        for row_list in freader:
            if maxnumber < float(row_list[3]):
                maxnumber = float(row_list[3])
    randomnumber = random.randrange(0, int(maxnumber*10000000))
    file = "module/database/gambling/%s.csv" % target
    with open(file, newline='', encoding='UTF-8') as database:  # 랜덤 결과 확인
        freader = csv.reader(database)
        next(freader)
        for row_list in freader:
            if float(row_list[2]) <= randomnumber/10000000 < float(row_list[3]):
                getitem = row_list[0]
    if "헤어" in title:
        output = discord.Embed(title="로얄 헤어 쿠폰", description='%s님의 헤어가 %s 로 변경되었습니다.' % (display_name, getitem),
                               color=0x0000ff)
    elif "성형" in title:
        output = discord.Embed(title="로얄 성형 쿠폰", description='%s님의 얼굴이 %s 로 변경되었습니다.' % (display_name, getitem),
                               color=0x0000ff)
    else:
        output = discord.Embed(title="%s" % title, description='%s님이 %s 을(를) 획득하였습니다.' % (display_name, getitem),
                               color=0x0000ff)
    output.set_footer(text="도박중독, 당신의 가정을 무너뜨릴 수 있습니다. ☎1336")
    return output


def gambling_main(msg, display_name):
    if len(msg) is 1:
        if '골드' in msg[0] or '애플' in msg[0]:
            output = gambling1(display_name, "골드애플", "GoldApple")
        elif '로얄' in msg[0]:
            output = gambling1(display_name, "로얄스타일", "RoyalStyle")
        elif '원더' in msg[0] or '원기' in msg[0]:
            output = gambling1(display_name, "원더베리", "WispsWonderBerry")
        elif '루나' in msg[0]:
            output = discord.Embed(title="Warning!!!", description='올바른 옵션을 입력하세요.', color=0xff0000)
            output.set_footer(text="예) #루나 스윗/드림")
        elif '남자' in msg[0] or '남성' in msg[0] or '여자' in msg[0] or '여성' in msg[0]:
            output = discord.Embed(title="Warning!!!", description='올바른 옵션을 입력하세요.', color=0xff0000)
            output.set_footer(text="예) #남자/여자 헤어/성형")
    elif len(msg) is 2:
        if '루나' in msg[0]:
            if '스윗' in msg[1]:
                output = gambling1(display_name, "루나 크리스탈 스윗", "LunaCrystalSweet")
            elif '드림' in msg[1]:
                output = gambling1(display_name, "루나 크리스탈 드림", "LunaCrystalDream")
            else:
                output = discord.Embed(title="Warning!!!", description='올바른 옵션을 입력하세요.', color=0xff0000)
                output.set_footer(text="예) #루나 스윗/드림")
        elif '남자' in msg[0] or '남성' in msg[0]:
            if '헤어' in msg[1] or '머리' in msg[1]:
                output = gambling1(display_name, "헤어", "RoyalHairCouponMan")
            elif '성형' in msg[1] or '얼굴' in msg[1]:
                output = gambling1(display_name, "성형", "RoyalPlasticSurgeryCouponMan")
            else:
                output = discord.Embed(title="Warning!!!", description='올바른 옵션을 입력하세요.', color=0xff0000)
                output.set_footer(text="예) #남자 헤어/성형")
        elif '여자' in msg[0] or '여성' in msg[0]:
            if '헤어' in msg[1] or '머리' in msg[1]:
                output = gambling1(display_name, "헤어", "RoyalHairCouponWoman")
            elif '성형' in msg[1] or '얼굴' in msg[1]:
                output = gambling1(display_name, "성형", "RoyalPlasticSurgeryCouponWoman")
            else:
                output = discord.Embed(title="Warning!!!", description='올바른 옵션을 입력하세요.', color=0xff0000)
                output.set_footer(text="예) #여자 헤어/성형")
        else:
            if msg[1].isdecimal():
                times = int(float(msg[1]))
                if '로얄' in msg[0] and msg[1].isdecimal():
                    if 0 < times <= 1000:
                        output = gambling2(times, "로얄스타일", "RoyalStyle")
                    else:
                        output = discord.Embed(title="Warning!!!", description='1 ~ 1000 의 횟수를 지정해주세요.', color=0xff0000)
                elif ('원더' in msg[0] or '원기' in msg[0]) and msg[1].isdecimal():
                    if 0 < times <= 1000:
                        output = gambling2(times, "원더베리", "WispsWonderBerry")
                    else:
                        output = discord.Embed(title="Warning!!!", description='1 ~ 1000 의 횟수를 지정해주세요.', color=0xff0000)
                elif ('골드' in msg[0] or '애플' in msg[0]) and msg[1].isdecimal():
                    if 0 < times <= 100:
                        output = gambling2(times, "골드애플", "GoldApple")
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

    return output