"""
어린이집 봉사에 가지 못한 현욱이는 대신 은산이와 아쿠아리움에 가기로 했다.
아쿠아리움에는 정말 많은 물고기들이 가까이서 헤엄치고 있었다.
그러나 은산이의 눈에 들어온 것은 다름아닌 미역이었다.
은산이는 흔들거리는 해조류를 보고 있으면 번뇌가 사라지고 마음이 차분해지는 것이 좋았다.
은산이는 이 해조류의 움직임을 담아두고 싶었다.
컴퓨터공학과인 은산이는 코딩으로 해조류의 움직임을 재현하고자 한다.


해조류는 위에서 본 2차원 '수조'위에 숫자로 표현된다.
가장 아래 있는 다시마는 1로
중간에 위치한 미역은 2로
가장 위에 있는 김은 3으로 표현된다.


0은 빈 공간을 의미한다.
수조의 가장 왼쪽 위는 (0, 0)으로 표현할 수 있다.
m*n 수조에서 가장 오른쪽 아래의 좌표는 (m-1, n-1)이다.
m*n수조는 m개의 행 n개의 열을 가진 수조를 말한다.

해조류의 모양은 불규칙할 수도 있다.
다만 모두 같은 숫자로 연결되어 있다면 같은 하나의 해조류이다.
해조류는 하나의 좌표로 특정될 수 있다.

미역, 김, 다시마는 각각 0~1개가 있을 수 있다.
처음에 주어진 수조에서는 해조류가 붙어있을 수는 있지만 겹쳐있지는 않다.

해조류는 각각 움직임을 가지고 있는데, 움직임은 하나의 벡터로 주어진다.  (V⊂ R2)
어떤 해조류의 1초 뒤 위치는 움직임 벡터가 (a, b)라면 행 방향으로 a만큼 아래로, 열 방향으로 b만큼 오른쪽으로 이동하게 된다.
벽에 부딪히게 부딪힌 방향에 반대로 튕긴다.


위 9개의 사진은 미역이 (-1, -1) , 다시마가 (0, 0) 움직임 벡터를 가지고 움직일 때 수조의 모습이 변화하는 모습이다.
각 사진의 시간 간격은 1초이며 4번째 사진에서 왼쪽 벽에 부딪히고 움직임 벡터는 (-1, 1)로 변하며 벽에 튕겼다.
미역은 다시마보다 위에 있기 때문에 미역이 다시마와 겹치면 미역 다시마를 가린다. 마찬가지로 김은 미역과 다시마를 가린다.

수조의 모습과 움직임 벡터가 주어질 때, t초 뒤 수조의 모습을 구하는 함수를 만들어라.
"""

from enum import Enum

class SeaweedType(Enum):
    KELP = 1 # 다시마
    SEA_MUSTARD = 2 # 미역
    LAVER = 3 # 김


class Seaweed:

    def __init__(self, type: SeaweedType, coordinates: list):
        self.type = type
        self.coordinates = coordinates

    def getType(self) -> SeaweedType:
        return self.type

    def isKelp(self) -> bool:
        return self.type.value == SeaweedType.KELP.value
    
    def isSeaMustard(self) -> bool:
        return self.type.value == SeaweedType.SEA_MUSTARD.value
    
    def isLaver(self) -> bool:
        return self.type.value == SeaweedType.LAVER.value
    
    def isIn(self, coordinate: tuple) -> bool:
        return coordinate in self.coordinates

    def getNextVector(self, currentVector, t) -> tuple:
        if t < 1:
            return currentVector
        newX, newY = currentVector
        def calculate() -> tuple:
            xList = []
            yList = []
            for i in self.coordinates:
                xList.append(i[0])
                yList.append(i[1])
            return (min(xList), max(xList), min(yList), max(yList))
        [minX, maxX, minY, maxY] = calculate()
        while True:
            isValid = True
            if minX + newX < 0:
                newX = (-1) * (minX + newX) - 1
                isValid = False
                [minX, maxX, minY, maxY] = calculate()
            if maxX + newX > 9:
                newX = 9 - maxX - (maxX + newX)%9
                isValid = False
                [minX, maxX, minY, maxY] = calculate()
            if minY + newY < 0:
                newY -= (minY + newY)-1
                isValid = False
                [minX, maxX, minY, maxY] = calculate()
            if maxY + newY > 9:
                newY = 9 - maxY - (maxY + newY)%9
                isValid = False
                [minX, maxX, minY, maxY] = calculate()
            if isValid:
                break
        return self.getNextVector((newX, newY), t-1)
    

class SeaweedFactory:

    def __init__(self, waterTank: list):
        temp = []
        for l in waterTank:
            temp += l
        self.waterTank = temp
        self.storage = []
        self.scanAll()

    def getSeaweed(self, coordinate: tuple) -> Seaweed:
        for seaweed in self.storage:
            if seaweed.isIn(coordinate):
                return seaweed
        return None
    
    def getSeaweeds(self) -> list:
        return self.storage
    
    def getAllKelps(self) -> list:
        temp = []
        for seaweed in self.storage:
            if seaweed.isKelp():
                temp.append(seaweed)
        return temp
    
    def getAllSeaMustards(self) -> list:
        temp = []
        for seaweed in self.storage:
            if seaweed.isSeaMustard():
                temp.append(seaweed)
        return temp
    
    def getAllLavers(self) -> list:
        temp = []
        for seaweed in self.storage:
            if seaweed.isLaver():
                temp.append(seaweed)
        return temp
    
    def fillField(self, seaweed: Seaweed, field: list, vector: tuple):
        for i in seaweed.coordinates:
            coordinate = (i[0] + vector[0], i[1] + vector[1])
            index = self.getIndexByCoordinate(coordinate)
            field[index] = seaweed.getType().value
        return field
    
    @staticmethod
    def distance(coordinate1, coordinate2) -> int:
        return ((coordinate1[0] - coordinate2[0]) ** 2 + (coordinate1[1] - coordinate2[1]) ** 2) ** 0.5
    
    def getIndexByCoordinate(self, coordinate: tuple) -> int:
        return coordinate[1] + (coordinate[0] * 10)
    
    def getCoordinateByIndex(self, index) -> tuple:
        x = int(index/10)
        return (x, index - x*10)
    
    def scanAll(self):
        def isValid(targetCoordinate: tuple, findingTemp: list) -> bool:
            for i in findingTemp:
                if SeaweedFactory.distance(i, targetCoordinate) < 2:
                    return True
            return False
        waterTank = self.waterTank
        for i in range(len(waterTank)):
            value = waterTank[i]
            coordinate = self.getCoordinateByIndex(i)
            if value == 0:
                continue
            findingTemp = [coordinate]
            for j in range(i, len(waterTank)):
                if waterTank[j] != value:
                    continue
                coordinate_ = self.getCoordinateByIndex(j)
                if coordinate_ in findingTemp:
                    continue
                if isValid(coordinate_, findingTemp):
                    findingTemp.append(coordinate_)
            seaweed = Seaweed(SeaweedType(value), findingTemp)
            self.storage.append(seaweed)
            for k in findingTemp:
                self.waterTank[self.getIndexByCoordinate(k)] = 0


def san(tank: list, vector: list, t: int) -> list:
    def init(l):
        temp = {}
        for element in l:
            temp[element] = (0, 0)
        return temp
    seaweedFactory = SeaweedFactory(tank)
    kelps       = init(seaweedFactory.getAllKelps())
    seaMustards = init(seaweedFactory.getAllSeaMustards())
    lavers      = init(seaweedFactory.getAllLavers())
    count       = len(seaweedFactory.waterTank)
    for element in vector:
        seaweed = seaweedFactory.getSeaweed(element[0])
        if seaweed.isKelp():
            kelps[seaweed] = element[1]
        elif seaweed.isSeaMustard():
            seaMustards[seaweed] = element[1]
        elif seaweed.isLaver():
            lavers[seaweed] = element[2]
        else:
            raise Exception(f"[ERROR] unregistered seaweed type : {seaweed.getType()}")
    field = [0] * count
    for kelp in kelps:
        field = seaweedFactory.fillField(kelp, field, kelp.getNextVector(kelps[kelp], t))
    for seaMustard in seaMustards:
        field = seaweedFactory.fillField(seaMustard, field, seaMustard.getNextVector(seaMustards[seaMustard], t))
    for laver in lavers:
        field = seaweedFactory.fillField(laver, field, laver.getNextVector(lavers[laver], t))
    result = []
    temp = []
    for i in range(count):
        temp.append(field[i])
        if (i+1)%10 == 0:
            result += [temp]
            temp = []
    return result
        

"""
tank = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 1, 1, 1, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 1, 1, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 0, 0, 0, 0,
    2, 2, 2, 2, 2, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]
san(tank, [((1, 1), (7, 0))], 3)
"""

sujo = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

[0, 0, 0, 1, 1, 1, 1, 0, 0, 0], 

[0, 0, 0, 1, 1, 1, 1, 0, 0, 0], 

[0, 0, 1, 1, 1, 1, 1, 0, 0, 0], 

[0, 0, 1, 1, 0, 0, 0, 2, 2, 0], 

[0, 0, 0, 0, 0, 0, 2, 2, 2, 0], 

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

vactor = [((2, 3), (0, 0)), ((5, 8), (-1, -1))]

t = 1

result = san(sujo, vactor, t)

print(result)