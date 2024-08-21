'''
주어진 N에 대하여 연속된 자연수의 합으로 나타내는 가짓수 출력
'''
N = int(input())
start, end = 1, 1
value = 1
ans = 0

while start <= end <= N:
    if value == N:
        ans += 1
        end += 1
        value += end
    elif value < N:
        end += 1
        value += end
    else:
        value -= start
        start += 1

print(ans)
