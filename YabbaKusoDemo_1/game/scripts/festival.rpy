image bg festival:
    "festival.jpg"

define senior = Character("선배", color="#5d5d5d61")

label festival:
    scene bg festival with dissolve 
    
    "평소와 같이 등교하는 날."

    "수상할 정도로 많은 인파가 학교 입구에 몰려있었다."

    p "...오늘 무슨 날인가?"

    "의아함을 느끼며 과방으로 향했다."

    #과방 화면

    p "야, 오늘 무슨 날이냐?"

    show mob at right
    "동기" "...오늘 축제잖아 미친놈아."

    "오늘이 축제였어?"

    "벙찐 표정으로 있자, 동기가 어이없다는 듯 말을 이었다."

    "동기" "다들 음식 팔고, 코스프레하고 다니고 그러는데. 그 정도면 대충 눈치채지 않냐?"

    "확실히 코스프레는 본 것 같은데"

    p "그럼 우리과는 뭐하는데?"

    "동기" "지금 서빙 자리는 다 찼고, 요리할 사람 찾고 있더라. 아니면 장기자랑 할 사람 모집하던데 그쪽으로 가보던가. 그냥 구경만 해도 되고. 축제 갈거지?"

    "그 말에 나는 씨익 웃으며 대답했다."

    p "당연하지"

    hide mob

    menu:
        "요리 부스":
            jump cook

        "장기 자랑":
            jump talent

        "구경":
            jump tour
    
label cook:
    p "안녕하세요? 아까 연락 드린 23학번 신입생인데요..."

    "선배" "아, 왔구나! 우리 노예! 아니, 크흠... 우리 신입생, 일단 이쪽으로 와볼래?"

    "선배에게 붙잡혀 부스 안쪽으로 끌려들어갔다."

    "주위를 살펴보니 열심히 움직이는 사람들 사이로 메이드복이 눈에 들어왔다."

    "서빙을 메이드복 입고 하네. 대체 누구 취향인거지?"

    "정말 최고야!!!"

    "선배" "네가 할일은..."

    "..."

    "성황리에 부스를 마치고"

    p "와, 저희 재료 다 떨어졌어요!"

    "선배" "그래, 우리도 드디어 마감이다!"

    "이제 저 망할 쓰레기들을 치울 일만 남았다."

    "하, 내년에 축제 참가하나봐라..."

    "..."

    "정신없이 부스를 정리하던 중 주변이 소란스러워졌다."

    "우리 학과의 아이도루, 김석교 교수님의 등장이었다."

    show prof_happy at center
    pr "어어, [p]. 학과 부스에 열심히 참여하고 있구나?"

    p "아아, 교수님! 제가 맛깔나는 음식 한 번 뽑아보겠습니다."
    
    hide prof_happy
    show prof_standard at center
    pr "아니야, 그냥 구경온거야, 구경. 우리 애들이 얼마나 잘하고 있는지 보려고."

    "그 말이 정말이었는지 교수님은 주위를 쓱 둘러보시곤 만족스럽게 웃으셨다."

    hide prof_standard
    show prof_happy at center
    pr "그래, 잘 하고 있네."

    jump festival_done

label talent:
    "그래도 축제인데 즐겨야하지 않겠어?"

    "나는 장기자랑에 참가하기 위해 명단을 제출했다."

    "(시간이 지나고...)"

    "두근두근 드디어 내 차례다!"

    menu:
        "멋있고 기깔나게 부르기":
            jump goodSong

        "간지나고 작살나게 부르기":
            jump badSong

label goodSong:
    show mob standard
    "???" "우와아아아앗!!! 쟤 뭐야?"
    
    "???" "누구야? 어디 과래?"

    "???" "오이오이 저 녀석 굉장하잖냐!"

    hide mob
    "무대를 마치고 내려가자 동기들이 환호하며 다가왔다."

    show mob at right
    "동기" "와 진짜 미쳤다!!! 너 가수 아니야?"

    "오잉? 사람들 사이로 석교 교수님이 다가왔다."

    hide mob
    show prof_happy at center
    pr "이야~ 이렇게 노래를 잘하는 줄 몰랐네! 다시 봤어~"

    p "헤헤 감사합니다 교수님"

    jump festival_done

label badSong:
    show mob standard
    "???" "오..."
    
    "???" "음......"

    "???" "아.........ㅋㅋㅋ 어디 과냐?"

    hide mob
    "무대를 마치고 내려가자 동기가 다가왔다."

    show mob at right
    "동기" "넌 무슨 생각으로 나갔냐?ㅋㅋㅋ"

    "동기와 대화하던 중 석교 교수님이 다가왔다."

    hide mob
    show professor embarassed at center
    pr "네가 장기자랑 나간 애지? 그래, 수고했다."

    "사람들의 무관심한 호응에 수치스러워하며 공연을 마무리했다..."

    jump festival_done

label tour:
    "이런날에 일은 무슨 일이야."

    "나는 고생하고 있을 동기들을 놀리기 위해 학과 부스로 향했다."

    "오므라이스를 주문하고 한량처럼 자리잡았다."

    "동기들이 만든 맛있는 오므라이스를 먹을 생각에 웃음이 났다."

    "???" "주문하신 오므라이스 나왔습니다."

    p "감사합... 엇, 선배?"

    "익숙한 목소리에 고개를 들어보니 선배가 있었다."

    show heroine_closebigsmile_red at center
    h "동기가 하도 사정사정하길래... 하하."

    p "선배가 축제 참여하실 줄 몰랐어요. 그러니까..."

    menu:
        "완전 잘 어울리세요!":
            jump badChoice
        
        "학과 활동 열심히 하시네요.":
            jump goodChoice

    jump festival_done

label goodChoice:
    p "학과 활동 열심히 하시네요! 이럴 줄 알았으면 저도 요리나 했어야 했나..."

    h "나도 작년엔 구경만 했었거든...이렇게라도 참여하는게 좋을 것 같더라고."

    h "자, 오므라이스에 그림이나 그려줄게. 뭐 그려줄까?"

    p "그럼... 고양이?"

    "선배는 익숙한 듯 바로 고양이를 그려냈다."

    p "와... 귀엽다."

    "선배의 오므라이스를 먹은 나는"

    "의지로 가득찼다."

    jump festival_done

label badChoice:
    p "완전 잘 어울리세요!"
    
    h "...그거 칭찬 맞지?"

    hide heroine_closebigsmile_red
    show heroine_nervous at standard
    "앗! 화제가 그리 달갑진 않은 모양이다. 선배 표정이 구려졌다."

    jump festival_done

label festival_done:
    show bg blackbackground
    hide professor embarassed
    hide prof_happy
    ""