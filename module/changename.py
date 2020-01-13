#!/usr/bin/env python3


def changename(name):
    name = "히어로" if "혀로" in name else name
    name = "다크나이트" if "닼나" in name else name
    name = "아크메이지(불, 독)" if "불독" in name else name
    name = "아크메이지(썬, 콜)" if "썬콜" in name else name
    name = "보우마스터" if "보마" in name else name
    name = "패스파인더" if "패파" in name else name
    name = "나이트로드" if "나로" in name else name
    name = "듀얼블레이드" if "듀블" in name else name
    name = "바이퍼" if "바퍼" in name else name
    name = "캐논슈터" if "캐슈" in name else name
    name = "소울마스터" if "소마" in name else name
    name = "플레임위자드" if "플위" in name else name
    name = "윈드브레이커" if "윈브" in name else name
    name = "나이트워커" if "나워" in name else name
    name = "스트라이커" if "스커" in name else name
    name = "메르세데스" if "메세" in name else name
    name = "데몬슬레이어" if "데슬" in name else name
    name = "데몬어벤져" if "데벤" in name else name
    name = "배틀메이지" if "배메" in name else name
    name = "와일드헌터" if "와헌" in name else name
    name = "엔젤릭버스터" if "엔버" in name else name

    return name