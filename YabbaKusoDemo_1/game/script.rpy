﻿# 이 파일에 게임 스크립트를 입력합니다.


# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"


# 게임에서 사용할 캐릭터를 정의합니다.

image heroine standard:
    "heroine_beta.png"
    zoom 1.34

init python:
    playername = "롸"
    player = Character('playername', dynamic = True, color="#8ea5b2")
    playername = "당신"
    
    naration = Character("", color="#64efff")

    heroinename = "???"
    heroine = Character('heroinename', dynamic = True, color="#f47fb4")


# 여기에서부터 게임이 시작합니다.


label start:

    call tutorial_bus # 튜토리얼 장면 시작
    call tutorial_class

    return
