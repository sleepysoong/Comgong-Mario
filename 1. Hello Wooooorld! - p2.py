"""
Hello world!
마리오가 되기 위해 학술행사에 참여한 컴퓨터공학부 학우들은 첫 번째 문제부터 난관에 부딪혔다. 
바로 헬로월드를 출력하는 것!
컴퓨터공학부 학우들은 무사히 첫 번째 문제를 통과하고 마리오가 되기 위한 여정에 오를 수 있을까?!

p2 <1점>
음이 아닌 정수 n을 입력받고, 입력받은 숫자만큼의 'o'를 넣어 "Hello World"를 출력하세요. 
입력: 5
출력: Hello Wooooorld
"""

try:
    n = int(input())
    if n < 0:
        print("음이 아닌 정수 n을 입력하세요")
    else:
        print("Hello W" + "o" * n + "rld")
except:
    print("음이 아닌 정수 n을 입력하세요")