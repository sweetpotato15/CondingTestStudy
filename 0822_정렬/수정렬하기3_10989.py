# 기수정렬 사용해서 정렬하기 -> O(kn) n:데이터 개수, k:자릿수 개수
# import sys
# input = sys.stdin.readline
# import heapq

# N = int(input())
# count = [[] for _ in range(10)]

# for i in range(N):
#     value = input().strip().zfill(5)
#     count[int(value[-1])].append(int(value))

# 계수정렬 : 나올 수 있는 값을 index로 리스트 만든후, value 1씩 늘리기
import sys
input = sys.stdin.readline

N = int(input())
count = [0]*10001

for i in range(N):
    count[int(input())] += 1

for i in range(1,10001):
    for j in range(count[i]):
        print(i)