#!/usr/bin/env python3

import discord

description = '봇 서버를 켜지 않은 동안에는 작동하지 않으며, 봇의 온/오프라인 상태 확인으로 확인하실 수 있습니다.\n'


def help_main():
    output = discord.Embed(title="도움말", description=description, color=0x00ff00)
    output.add_field(name="#도움말", value="도움말을 표시합니다.", inline=False)
    output.add_field(name="#심볼 (옵션 1) (옵션 2)",
                     value="(옵션 1)부터 (옵션2)까지 심볼 레벨을 올리는 데 필요한 심볼 갯수, 메소를 확인할 수 있습니다.",
                     inline=False)
    output.add_field(name="#추옵 (셋트명) (무기 종류)", value="무기의 단계별 추옵 수치를 확인하실 수 있습니다.",
                     inline=False)
    output.add_field(name="#방무 (방어율 무시 1) (방어율 무시 2) ... (방어율 무시 n)",
                     value="몬스터에게 들어가는 데미지율을 확인할 수 있습니다.",
                     inline=False)
    output.add_field(name="#레벨 (닉네임)",
                     value="현재의 경험치와 250, 275까지 필요한 경험치량을 나타냅니다.\n메이플스토리 공식 홈페이지의 정보를 활용합니다.",
                     inline=False)
    output.add_field(name="#정보 (닉네임)",
                     value="사용자의 프로필을 확인할 수 있습니다.\n상세 정보 확인을 위해서는 #무릉, #시드, #유니온, #업적 명령어를 입력하세요.",
                     inline=False)
    output.add_field(name="#한강",
                     value="현재 한강의 수온 정보를 알려줍니다.",
                     inline=False)
    output.add_field(name="#골드애플, 로얄스타일, 원더베리 (횟수)",
                     value="확률성 아이템을 시뮬레이션 할 수 있으며, 횟수 옵션이 없는 경우 1회 시행합니다.",
                     inline=False)
    output.add_field(name="#루나 스윗/드림",
                     value="루나 크리스탈 스윗/드림을 시뮬레이션 할 수 있습니다.",
                     inline=False)
    output.add_field(name="#남자/여자 헤어/성형",
                     value="헤어와 성형을 시뮬레이션 할 수 있습니다.",
                     inline=False)
    output.add_field(name="#이벤트/캐시",
                     value="현재 진행중인 이벤트/현재 판매중인 캐시 정보를 불러옵니다.",
                     inline=False)
    output.add_field(name="#링크 (직업)",
                     value="유니온 효과와 링크스킬을 확인할 수 있습니다.",
                     inline=False)
    output.add_field(name="#심신 (시작 레벨) (끝 레벨)",
                     value="시작 레벨부터 끝 레벨까지 필요한 심신수련관에서의 시간을 나타냅니다.",
                     inline=False)

    output.set_footer(text="문의 : RIRINTO#0966")
    return output
