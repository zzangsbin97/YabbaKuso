# 이 파일에 게임 스크립트를 입력합니다.



# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

image bg test1 = "bgtest1.png"
image elsword standard:
    "elswordtestnograde.png"
image blackmage standard:
    "blackmage.gif"
    zoom 2.0


# 게임에서 사용할 캐릭터를 정의합니다.

init python:
    playername = "롸"
    player = Character('playername', dynamic = True, color="#8ea5b2")
    playername = "당신"


label tutorial:

    "삑- 하차입니다. "

    "명쾌한 하차음을 뒤로 한 채 버스에서 내렸다."

    player "내 20대의 청춘을 보낼 대학교가 바로..."
 
    "잠깐 멈춰서 아직 겨울의 차가움이 가시지 않은 바람을 폐 안에 채워본다."
    
    "주인공" "흐으읍..."

    "숨을 뱉으려는 찰나 점점 커지는 발걸음 소리에 뒤를 돌아보니..."

    "???" "...저기요!"

    player "...응?"

    "???" "너무 마음에 들어서 그런데 혹시..."

    "이건 설마...?"

    "???" "번호 좀 주실 수 있을까요?"

    player "네?"

    "나도 드디어 말로만 듣던 \'번따\'라는 걸 당해보는 건가?"

    player "아 네... 주세요."

    "나는 떨리는 손가락으로 번호를 누른 후 핸드폰을 건넸다."

    "???" "성함이..."

    player "아, 네"

    python:
        playername = renpy.input("내 이름은...\n")

        playername = playername.strip() 

        playername = playername

    player "[playername]입니..."


    "빠앙-"

    "말을 마치려던 순간 귓가에 큰 소리가 스쳐지나가며 찬물을 얼굴에 끼얹은 듯 정신이 들었다."

    player "...에휴. 역시 그럴 리가 없지."

    "허망한 발걸음으로 봄내음 가득한 캠퍼스를 뒤로한 채 나는 발걸음을 옮겼다."
 
    


# 여기에서부터 게임이 시작합니다.
label test:

    scene bg test1
    show elsword standard at left
    show blackmage standard at right

    e "엘의회랑 별거아니죠?"

    e "노전한테 다털렸죠?"

    e "아무것도못하죠?"

    "노전이 저런 대사를 치는 것을 보니"

    "나는 엘소드가 너무 하기 싫어졌다."

    return


label start:
    call tutorial

    return
