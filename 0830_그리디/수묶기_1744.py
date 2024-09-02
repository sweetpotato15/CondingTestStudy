import sys
input = sys.stdin.readline

N = int(input())
minus, plus = [], []

array = [int(input()) for _ in range(N)]
minus = sorted([x for x in array if x <= 0])
plus = sorted([x for x in array if x > 1])
plus_one = array.count(1)

ans = 0
while len(minus) > 1:
    ans += minus.pop(0) * minus.pop(0)
if minus:
    ans += minus.pop()

while len(plus) > 1:
    ans += plus.pop() * plus.pop()
if plus:
    ans += plus.pop()
ans += plus_one

print(ans)