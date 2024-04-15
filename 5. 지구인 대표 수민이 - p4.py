"""
외계인이 있다는 것을 믿지 않는 수민이를 혼내주기 위해 한밤중에 외계인들이 수민이를 납치해갔다. 
갑작스럽게 지구인 대표가 된 수민이는 외계인들에게 지구인의 지성을 증명해야한다. 
다음 코드를 완성해 수민이를 도와 지구인의 역량을 증명하자!

p4 <4점, 20명>

0 b c d 0
f 0 h 0 j
k l 0 n o
p 0 r 0 t
0 v w x 0
"""

def sumin():
    return [[0 if (i==j or i+j == 4) else chr(5*i + j + 97) for j in range(5)] for i in range(5)]

for i in sumin():
    print(*i)