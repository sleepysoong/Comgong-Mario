"""
처음 코딩을 배우고 자신감이 붙은 민준이는 자판기 프로그램을 만들고자 한다. 
민준이는 멋진 UI를 구성하였고, 카카오페이 결제까지 가능한 자판기를 만들었지만 문제에 봉착했다. 
거스름돈을 어떻게 하면 최소로 줄 수 있을까? 민준이를 도와 자판기를 완성해보자.

거스름돈 x원이 주어질 때, 이를 가장 적은 수의 동전으로 거슬러주면 총 몇 개의 동전이 필요한지 찾아주는 함수를 완성하세요. 
거스름돈은 동전으로만 주며 동전의 종류는 500원, 100원, 50원, 10원 이 있다. 


x가 입력되면 필요한 동전의 수를 튜플에 담아 리턴하세요. (500원, 100원, 50원, 10원)

change(1100)
>>> (2, 1, 0, 0)

거슬러줄 수 없다면 0을 리턴합니다. 

change(999)
>>> 0
"""

def change(x):
    """
    내가 생각한 로직:

    거슬러줄 수 없는 상황 == 333(0*500 + 100*3 + 50*0 + 10*3 + 1*3)원처럼
    500원, 100원, 50원, 10원으로 표현하다보면 돈이 남는 경우

    즉, 만약에 1원짜리 동전이 존재한다고 쳤을 때
    1원짜리 동전을 1개라도 줘야 한다면 거슬러줄 수 없는 상황이라고 봄
    """
    fiveHundredWon = int(x / 500)
    oneHundredWon  = int((x - fiveHundredWon*500)/100)
    fiftyWon       = int((x - (fiveHundredWon*500 + oneHundredWon*100))/50)
    tenWon         = int((x - (fiveHundredWon*500 + oneHundredWon*100 + fiftyWon*50))/10)
    oneWon         = x - (fiveHundredWon*500 + oneHundredWon*100 + fiftyWon*50 + tenWon*10)
    return 0 if oneWon > 0 else (fiveHundredWon, oneHundredWon, fiftyWon, tenWon)

print(change(998))