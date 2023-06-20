image bg tutorialbusstation: # 튜토리얼 버스 정류장 사진 배경 설정
    "tutorial_busstation.png"
    zoom 2.1

image bg tutorialclass: # 튜토리얼 강의실 배경 설정
    "tutorial_class.jpg"


label tutorial_bus: # 튜토리얼 버스 장면 시작


    naration "{color=#f47fb4} Ch 0. 교수는 다정하고 귀여운 존재라고 생각하던 시기가 저한테도 있었습니다.{/color}"

    with fade # 화면 전환 효과 (var 파일에 정의해뒀습니다)
    

    scene bg tutorialbusstation # 튜토리얼 버스정류장 사진 가져옴

    "삑- 하차입니다. "

    "명쾌한 하차음을 뒤로 한 채 버스에서 내렸다."

    p "내 20대의 청춘을 보낼 대학교가 바로..."
 
    "잠깐 멈춰서 아직 겨울의 차가움이 가시지 않은 바람을 폐 안에 채워본다."
    
    "주인공" "흐으읍..."

    "숨을 뱉으려는 찰나 점점 커지는 발걸음 소리에 뒤를 돌아보니..."

    show mob standard

    "???" "...저기요!"

    p "...응?"

    "???" "너무 마음에 들어서 그런데 혹시..."

    "이건 설마...?"

    "???" "번호 좀 주실 수 있을까요?"

    p "네?"

    "나도 드디어 말로만 듣던 \'번따\'라는 걸 당해보는 건가?"

    p "아 네... 주세요."

    "나는 떨리는 손가락으로 번호를 누른 후 핸드폰을 건넸다."

    "???" "성함이..."

    p "아, 네"

    python:
        playername = renpy.input("내 이름은...\n")

        playername = playername.strip() 

        playername = playername

    p "[playername]입니..."

    hide mob standard

    "빠앙-"

    "말을 마치려던 순간 귓가에 큰 소리가 스쳐지나가며 찬물을 얼굴에 끼얹은 듯 정신이 들었다."

    p "...에휴. 역시 그럴 리가 없지."

    "허망한 발걸음으로 발걸음을 옮기던 중 무언가 이상함을 느낀 나는 고개를 들어 주위를 살펴봤다."

    "사방을 아무리 둘러봐도 대학교 같은 건물은 보이지 않았다."

    "분명 정류장 이름은 상명대 입구가 맞는데?"

    p "...아, 설마."

    "이리저리 살피던 중 무성한 나무 사이에 \[상명대학교\]라는 글씨가 눈에 들어왔다."

    "...그 아래에 있는 오르막길과 함께..."

    "오르막길을 올라가는 버스의 뒤통수를 보며 그제서야 버스를 잘못 탔다는 것을 깨달았다."

    p "저 위까지 가는 버스가 따로 있었구나..."

    "이미 엎질러진 물을 어쩌랴."

    "첫 강의인 전공수업까지 남은 시간은 10분."

    "나는 언덕을 향해 한걸음 내딛었다."

label tutorial_class:

    with fade

    scene bg tutorialclass

    "Tlqkf, 하필 강의실이 4층이라니."

    "가까스로 강의 직전에 도착한 나는 운이 좋겟도 비어있는 뒷자리를 발견했다."

    p "저, 여기 자리 있을까요?"

    "아예 빈자리는 아니었기에, 옆에 앉아있던 사람에게 말을 걸었다."

    show heroine standard

    h "아니요, 앉으셔도 돼요."

    "속으로 안도의 한숨을 내뱉으며 자리에 앉았다."

    "그나저나 저 사람... 나랑 같은 수업이면 내 동기 맞지?"

    "이런저런 생각이 꼬리를 물던 중, 교수님이 강의실로 들어오셨다."

    hide heroine standard

    "출석을 부르기 시작하는 교수님이 모습은 얼핏보기에도 젊어보이셨다."

    "분명 88학번이라고 들었는데 거짓말이었나?"

    show professor standard

    pr "자, 여러분. 난 김석교라고 하고."

    "교수님은 챗GPT에서 얻어낸듯한 자기소개를 하기 시작하셨다."

    hide professor standard

    p "특이한 교수님이네..."

    show heroine smile

    h "...풋"

    hide heroine standard # 나중에 웃는 이미지 수정 필요

    "생각이 입으로 나온 것일까, 옆에서 설핏 웃는 소리가 들렸다."

    "그것도 잠시, 김석교 교수님은 본격적인 OT를 시작하셨다."

    show professor standard at left

    pr "(대충 설명)"

    "교수님의 목소리가 무척이나 감미로워서 나도 모르게 잠에 들어버리고 말았다."

    "눈을 뜨자 교수님과 눈이 마주쳤고 피하기에는 이미 너무 늦었다"

    "...고 생각하던 와중, "    

    pr "{color=#90FFFF}백소영{/color}, 넌 2학년이면서 이 수업을 왜 들어?"

    "다행히도 내가 아닌 \'백소영\'이라는 사람에게 말을 거셨다."
     
    "\'백소영\'이라는 사람 누군지는 몰라도 참 불쌍하..."

    $ heroinename = "백소영"

    show heroine nervoussmile at right

    h "하하... 성적이 조금... "

    "바로 옆에서 대답이 들려왔다.\n뭐야 저사람. 나랑 동갑 아니었어?" 

    hide professor standard
    
    show professor happy at left

    pr "아니 자네가 출튀를 했잖아. 호의가 계속되면 권리인 줄 안다고."

    pr "도망가는 사람들 내가 다 알고있어. 여러분, 출튀는 엄벌이야."

    hide professor happy
    hide heroine nervoussmile

    "교수님의 말씀에 강의실은 웃음바다가 되었다."






    

