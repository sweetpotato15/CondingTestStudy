'''
오큰수 : 내 오른쪽에 있는 수 중 나보다 크면서 가장 왼쪽에 있는 수
'''
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
array = list(map(int, input().split()))
answer = [-1]*(N)
mystack = deque([]) # index 담기

for i in range(N):
    while mystack and array[mystack[-1]] < array[i]:
        answer[mystack.pop()] = array[i]
    mystack.append(i)    

print(*answer, end=' ')