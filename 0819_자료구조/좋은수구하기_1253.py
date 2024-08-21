'''
다른 두 수의 합으로 표현되면 좋은 수
'''
import sys
input = sys.stdin.readline

def good_number(array, x):
    array.remove(x)
    start, end = 0, len(array)-1
    while start < end:
        value = array[start] + array[end]
        if value == x:
            return 1
        elif value < x:
            start += 1
        else:
            end -= 1
    return 0

N = int(input())
array = sorted(list(map(int, input().split())))
ans = 0
for i in range(N):
    number = array[:]
    ans += good_number(number, array[i])

print(ans)