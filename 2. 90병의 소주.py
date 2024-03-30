"""
https://namu.wiki/w/99%EB%B3%91%EC%9D%98%20%EB%A7%A5%EC%A3%BC

주당 정진이는 술을 정말 좋아한다. 너무 좋아하여 집에 소주를 짝으로 쌓아두고 마시는데, 소주 한 짝에는 소주 30병이 들어있다.
정진이는 하루에 소주를 한 병씩 꼭 마신다. 그리고 술에 취해 노래를 한 소절 부르는데, 내용은 다음과 같다. 


(day 1)

우리 집에 소주 3짝이 있었네
내가 1병을 먹고 2짝과 29병이 남았네
아아 89일이면 다 마시겠구나!


(day 2)

우리 집에 소주 2짝과 29병이 있었네
내가 1병을 먹고 2짝과 28병이 남았네
아아 88일이면 다 마시겠구나!

.
.
.

(day 90)

우리 집에 소주 1병이 있었네
내가 1병을 먹고 하나도 남지 않았네
아아 다시 3짝을 사와야지!


(day 91)

우리 집에 소주 3짝이 있었네
내가 1병을 먹고 2짝과 29병이 남았네
아아 89일이면 다 마시겠구나!


사실 정진이는 주당이라 1병을 먹어서는 취하지 않는다.
날짜가 주어졌을 때 정진이가 부르는 노래를 출력해주는 함수를 만들어보자. 

def jj_song(day):
	(여기를 수정하세요)
	return 0;


함수에 날짜를 넣으면 그 날짜에 정진이가 부르는 노래가 출력되고  0을 리턴하는 함수를 만드세요.  <6점>
제출은 함수만 제출하세요. (c와 c++은 include와 define 등 컴파일 코드와 함께 제출해주세요. )
함수의 이름은 jj_song 입니다. 
가능한 파이썬 코드로 제출해주세요(채점하기 어려워요 ㅜ)
하나의 함수로 만들 필요는 없습니다. 제출할 함수의 기능을 보조하는 함수를 만들어도 됩니다. 
C와 C++의 경우 main함수를 만들지 않아도 됩니다. 
"""

def jj_song(day):
    leftSoju = 90 - day % 90
    if leftSoju == 90:
        print("우리 집에 소주 1병이 있었네")
        print("내가 1병을 먹고 하나도 남지 않았네")
        print("아아 다시 3짝을 사와야지!")
        return 0
    def getLeftJjak(number):
        return int(number/30)
    def getLeftBottle(number):
        return number - getLeftJjak(number) * 30
    def getLeftSojuMessage(jjak, bottle):
        message = ""
        if jjak != 0:
            message += str(jjak) + "짝"
        if jjak != 0 and bottle != 0:
            message += "과 "
        if bottle != 0:
            message += str(bottle) + "병"
        return message
    print("우리 집에 소주 " + getLeftSojuMessage(getLeftJjak(leftSoju + 1), getLeftBottle(leftSoju + 1)) + "이 있었네")
    print("내가 1병을 먹고 " + getLeftSojuMessage(getLeftJjak(leftSoju), getLeftBottle(leftSoju)) + "이 남았네")
    print("아아 " + str(leftSoju) + "일이면 다 마시겠구나!")
    return 0

while True:
    jj_song(int(input()))