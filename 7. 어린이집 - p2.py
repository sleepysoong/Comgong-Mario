"""
중간고사가 끝난 현욱이는 시험이 끝난 것을 기념하여 친구들과 어린이집에서 봉사활동을 하기로 하였다.
(보기보다 현욱이는 착하다. )

봉사 신청을 하기 위해 어린이집 원장님께 전화를 했고, 이번주 주말에 봉사활동을 와도 좋다는 대답을 받았다.
그러나 조건이 하나 붙었다.

자라나는 어린이들에게 나쁜 영향을 끼칠 수도 있기 때문에, 중간고사를 망친 사람은 봉사활동을 올 수 없다는 것이었다.
현욱이는 문뜩 불안해졌다.

현욱이의 중간고사를 채점하여 현욱이가 어린이집 봉사활동에 갈 수 있을지 알아보자!

---
p2 <3점>
현욱이가 해당 수업의 중간고사 평균을 넘으면  봉사활동을 갈 수 있다.
"""

def hyeonuk(n, s):
    n.sort(reverse=True)
    return int(s >= n[int(len(n) / 2)])