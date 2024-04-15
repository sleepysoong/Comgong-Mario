"""
인천대학교 컴퓨터공학부 학생회 Core에서는 학우들을 위해 간식나눔 행사를 기획했다. 
컴공의 능력있는 학회장 예나는 학우들을 위해 몬스터 음료 재휴를 받아와 이번 행사에서는 100명분의 몬스터 음료가 추가로 제공될 예정이다. 
간식을 받기 위해 줄을 서있던 희연이는 문뜩 자신이 받을 몬스터 음료가 무슨 맛이 될지 궁금해졌다. 

몬스터는 책상에 두 더미로 쌓여있다. 
하나의 더미는 한 줄로 높게 쌓여있으며 맨 위에 있는 몬스터만 가져갈 수 있다. 

몬스터의 맛은 0~9까지 정수로 이루어져있다.
숫자가 작을수록 연한 맛이고 숫자가 클수록 진한 맛이다. 

학생들은 한 줄로 서서 몬스터를 받아간다.

학생은 연한 맛을 선호하는 학생과 진한 맛을 선호하는 학생이 있는데,
두 줄의 선택지 중 자신이 더 선호하는 맛을 가져간다.

맛이 같을 경우는 더 높게 쌓여있는 더미에서 가져가며
높이와 맛이 같을 경우에는 왼쪽 더미에서 가져간다.
만약 한 줄이 비었다면 남은 한 줄에서만 가져갈 수 있다. 

희연이는 진한 맛을 선호한다. 

연한 맛을 선호하는 학생은 -1로, 진한 맛을 선호하는 학생은 1로, 희연이는 0으로 표현된다. 


희연이는 몬스터를 쌓는 일을 도왔기 때문에 몬스터가 어떤 순서로 쌓여있는지 알고 있다. 
몬스터 더미와 학생들의 줄이 주어졌을 때 희연이가 어떤 맛의 몬스터를 받을 수 있는지 구하여라. 


입력 형식:

첫째 줄에 왼쪽 더미의 몬스터 수, 오른쪽 더미의 몬스터 수, 학생의 수가 주어진다. 
둘째 줄에 왼쪽 더미의 아래에 있는 몬스터부터 띄어쓰기로 구분되어 주어진다. 
셋째 줄에 오른쪽 더미의 아래에 있는 몬스터부터 띄어쓰기로 구분되어 주어진다. 
넷째 줄에 학생들이 줄의 앞에 서있는 학생부터 띄어쓰기로 구분되어 주어진다. 희연이는 항상 줄의 맨 마지막에 있고, 반드시 음료를 받을 수 있다. 


출력 형식:

희연이가 받게될 음료의 맛을 출력하라. 


예시:
3 4 4
9 6 8
7 0 8 6
1 -1 1 0


처음 상태

왼쪽 더미: 9 6 8
오른쪽 더미: 7 0 8 6
학생 줄: 1 -1 1 0

첫 번째 학생은 진한 맛을 선호하기 때문에 왼쪽 더미에 8을 가져간다. 


왼쪽 더미: 9 6 
오른쪽 더미: 7 0 8 6
학생 줄:  -1 1 0

두 번째 학생은 연한 맛을 선호하지만 둘 다 6이기 때문에 더 높게 쌓여있는 오른쪽 더미의 6을 가져간다. 


왼쪽 더미: 9 6 
오른쪽 더미: 7 0 8 
학생 줄:   1 0

진한 맛을 선호하는 학생이 오른쪽 더미에 8을 가져간다. 


왼쪽 더미: 9 6 
오른쪽 더미: 7 0 
학생 줄:  0

진한 맛을 선호하는 희연이가 6을 가져간다. 


정답: 6


LV1 32점: 

문제를 해결하라. 

LV2 44점: 

언어 제한: C, C++

자료구조와 그 연산에 관련된 헤더파일을 사용하지 않고 문제를 해결하라. 


입력을 받을 때 '숫자를 입력하세요:' 이런 식의 문구를 사용하지 마세요. 그냥 입력만 받으세요. 
"""

def getDirection(preferredFlavor: int, topOfLeft: int, topOfRight: int, leftDummyCount: int, rightDummyCount: int) -> int: # 0: left, 1: right
    isSameHeight = leftDummyCount == rightDummyCount
    isSameFlavor = topOfLeft == topOfRight
    if isSameFlavor and isSameHeight:
        return 0 # 높이와 맛이 같을 경우 왼쪽 더미에서 가져간다.
    if isSameFlavor:
        return [leftDummyCount, rightDummyCount].index(max(leftDummyCount, rightDummyCount))
    if preferredFlavor < 0: # 연한 맛을 좋아한다
        return [topOfLeft, topOfRight].index(min(topOfLeft, topOfRight))
    return [topOfLeft, topOfRight].index(max(topOfLeft, topOfRight))


try:
    [leftDummyCount, rightDummyCount, studentsCount] = list(map(int, input().split(" ")))
    leftDummy = list(map(int, input().split(" ")))
    if len(leftDummy) != leftDummyCount:
        raise Exception("왼쪽 더미에 있는 음료수 수가 불일치 합니다.")
    rightDummy = list(map(int, input().split(" ")))
    if len(rightDummy) != rightDummyCount:
        raise Exception("오른쪽 더미에 있는 음료수 수가 불일치 합니다.")
    students = list(map(int, input().split(" ")))
    if len(students) != studentsCount:
        raise Exception("학생 수가 불일치 합니다.")
    for i in range(studentsCount):
        direction = getDirection(students[i], leftDummy[-1], rightDummy[-1], len(leftDummy), len(rightDummy))
        if direction == 0:
            takenMonster = leftDummy.pop()
        else:
            takenMonster = rightDummy.pop()
        if i == (studentsCount - 1):
            print(takenMonster)
except Exception as e:
    print(e)
