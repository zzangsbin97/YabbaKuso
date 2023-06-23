image bg blackbackground:
    "blackbackground.jpg"

image bg pinkheart:
    "heart.jpg"

label ending_1:

    stop music

    show bg blackbackground

    play music "ending_1.mp3" fadein 1.5

    "이후로 시간이 메챠쿠챠 지나갔다."

    "신입생이었던 게 어제였던 거 같은데, 폭풍우같이 몰아치는 팀플에 정신을 잃고 어느새 막학기에 도달했다."

    "그러던 어느 날이었다."

    show professor standard with dissolve

    pr "시험이 끝나면... 잠깐 내 랩실로 오겠나?"

    p "...네, 그럼요."

    hide professor standard with dissolve

    "시험이 끝난 당일, 계속 떠올랐던 교수님과의 약속날이 되자 어쩐지 가슴 한구석이 요란했다."

    "이런저런 일로 많이 오갔던 곳이었으나, 오늘따라 왜인지 다르게 느껴지는 건 분명 착각이리라."

    "이를모를 감정에 술렁이는 가슴을 애써 억누르며 한걸음 한걸음 랩실로 향했다."

    show professor standard with dissolve

    pr "{color=#FFC4FF}그동안 자네를 지켜봐왔었지.{/color}"

    pr "{color=#FFC4FF}시험 첫날부터 계속...{/color}"
 
    "랩실에 울려퍼지는 교수님의 목소리는 부드러웠다."

    "고저없이 편안하게 느껴지는 그 목소리에 나는 홀린듯 창문을 등진 교수님을 바라보았다."

    pr "{color=#FFC4FF}정말 성실한 학생이었어. 아무리 어려운 시험이라도 백지로 내는 일이 없었지...{/color}"

    show professor happy with dissolve

    "작게, 교수님의 웃음소리가 들렸다."

    show professor standard with dissolve

    pr "{color=#FFC4FF}자네를 조금 더 지켜보고 싶어졌어.{/color}"

    stop music

    play music "ending.mp3" fadein 1.5

    pr "{color=#FF97FF}...내 가까이에서 말이야.{/color}"

    pr "{color=#FF97FF}석사까지라도 괜찮네...{/color} {color=#FF00DD}함께하겠나?{/color}"

    menu:
        "\"...네\"":
            p "...네"
        
        "고개를 끄덕인다.":
            "나는 천천히 고개를 끄덕였다."

    "열린 창문 틈새로 시원한 바람이 나부꼈다."

    "흔들리는 새하얀 커튼 사이로 내린 햇살이 교수님의 외곽선을 따라 일렁였다."

    "아아-"

    "{color=#12EAFF}여름이었다.{/color}"

    show heart behind professor with dissolve

    "{color=#FF48FF}True Ending - 부탁이야, 대학원으로 와줄래? 네/YES{/color}"

    "{color=#FF48FF}Special Thanks for 김석규 교수님{/color}"

    "{color=#FF48FF}And You.{/color}"