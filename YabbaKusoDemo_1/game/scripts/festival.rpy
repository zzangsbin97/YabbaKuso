image bg festival:
    "festival.jpg"


label festival:

    scene bg festival with dissolve 
     
    #학교 정문 사진 삽입
    
    "평소와 같이 등교하는 날."

    "수상할 정도로 많은 인파가 학교 입구에 몰려있었다."

    p "...오늘 무슨 날인가?"

    "의아함을 느끼며 과방으로 향했다."

    #과방 화면

    p "야, 오늘 무슨 날이냐?"

    show mob standard with dissolve

    "동기" "...오늘 축제잖아 미친놈아."

    "오늘이 축제였어?"

    "벙찐 표정으로 있자, 동기가 어이없다는 듯 말을 이었다."

    "동기" "다들 음식 팔고, 코스프레하고 다니고 그러는데. 그 정도면 대충 눈치채지 않냐?"

    "확실히 코스프레는 본 것 같은데"

    p "그럼 우리과는 뭐하는데?"

    "동기" "지금 서빙 자리는 다 찼고, 요리할 사람 찾고 있더라."
    
    "동기" "아니면 장기자랑 할 사람 모집하던데 그쪽으로 가보든가. 그냥 구경만 해도 되고. 축제 갈거지?"

    "그 말에 나는 씨익 웃으며 대답했다."

    p "당연하지!"

    hide mob standard with dissolve

"""
    menu:
        "요리 부스"
        #call cook

        "장기 자랑"

        "구경"
"""

label cook:

    p "안녕하세요? 아까 연락 드린 23학번 신입생인데요..."

    show mob standard with dissolve

    "선배" "아, 왔구나! 우리 노예! 아니, 크흠... 우리 신입생, 일단 이쪽으로 와볼래?"

    hide mob standard with dissolve

    "선배에게 붙잡혀 부스 안쪽으로 끌려들어갔다."

    "주위를 살펴보니 움직이는 사람들 사이로 메이드복이 눈에 들어왔다."

    "서빙을 메이드복 입고 하네. 대체 누구 취향인거지?"

    "{color=#FF1212}정말 최고야!!!{/color}"

    show mob standard with dissolve

    "선배" "네가 할 일은"

    hide mob standard

    #서빙







    hide festival

    