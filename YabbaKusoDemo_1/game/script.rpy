# 이 파일에 게임 스크립트를 입력합니다.


# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"


# 게임에서 사용할 캐릭터를 정의합니다.


init python:
    
    playername = "롸"
    p = Character('playername', dynamic = True, color="#8ea5b2")
    playername = "당신"

#    pth = Character("", color="#ababab") # 캐릭터 생각
    
    naration = Character("", color="#64efff")

    heroinename = "???"
    h = Character('heroinename', dynamic = True, color="#f47fb4") # 히로인 정보

    pr = Character('김석교', color="#93c28e") # 김석교 교수님 정보


# 여기에서부터 게임이 시작합니다.


label start:

    stop music fadeout 1.0

    call tutorial_bus from _call_tutorial_bus # 튜토리얼 장면 시작
#   call tutorial_class
    call festival from _call_festival

    call ending_1 from _call_ending_1

    call ending

    return
