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

"""
<입력>
3 4 4
9 6 8
7 0 8 6
1 -1 1 0

<출력>
6
"""