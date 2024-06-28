"""
은지는 core 동아리 회식을 준비하기 위해 통장을 관리하고 있다.
통장 관리를 편하게 하기 위해 프로그램을 만들고자 한다.

해당 통장을 관리할 때 3가지의 모드가 필요하다. (회원은 k명으로 가정한다.)
각 모드의 이름은 int형 1 2 3 4

1: 회원이 통장에 입금한다. 0을 리턴한다. (1000<=X<=10000)
2: 방금 입금한 회원이 환불을 원한다. 통장에 입금 내역이 있다면 가장 최근의 입금 내역을 통장에서 지우고 리턴한다. 없다면 -1을 리턴
3: 현재까지 입금한 인원 수를 리턴한다.
4. 현재까지 입금한 총 금액을 리턴한다.

위 4가지 모드를 모두 구현하여 k명에게 입금 받아 최종적으로 모은 금액을 출력하는 gongkoom 함수를 만들어라.


예시:
gongkoom(1, 1000) >>> 0
gongkoom(2) >>> 1000
gongkoom(2) >>> -1
gongkoom(3) >>> 0
gongkoom(1, 3000) >>> 0
gongkoom(1, 7000) >>> 0
gongkoom(4) >>> 10000
gongkoom(3) >>> 2

레퍼런스: 가변인자, 매개변수의 디폴트 값, static, 전역 변수
"""

from enum import Enum

class Mode(Enum):
    DEPOSIT = 1
    REFUND = 2
    TOTAL_MEMBERS = 3
    TOTAL_BALANCE = 4

global history
history = []

class Account:

    @staticmethod
    def deposit(amount: int):
        history.append(amount)

    @staticmethod
    def refund() -> int:
        if len(history) < 1:
            return -1
        return history.pop(-1)
    
    @staticmethod
    def totalMembers() -> int:
        return len(history)
    
    @staticmethod
    def totalBalance() -> int:
        return sum(history)
    
def gongkoom(*args):
    if args[0] == Mode.DEPOSIT.value:
        Account.deposit(int(args[1]))
        return
    if args[0] == Mode.REFUND.value:
        return Account.refund()
    if args[0] == Mode.TOTAL_MEMBERS.value:
        return Account.totalMembers()
    if args[0] == Mode.TOTAL_BALANCE.value:
        return Account.totalBalance()