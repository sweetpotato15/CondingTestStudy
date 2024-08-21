'''
sol1) 일정 길이 만큼 슬라이싱해서 문자별 등장횟수가 주어진 입력 조건에 해당하는지 확인 -> 맞으면 list에 저장
- 자료구조 : Counter, 슬라이딩 윈도우
- Counter : O(N) -> 시간초과 발생

sol2) Counter 에서 시간초과 발생 -> 매 반복마다 개수를 세는 것이 아니라 처음에 세고 맨 앞, 맨 뒤만 변화시키면서 이동
- 
'''
import sys
input = sys.stdin.readline

S, P = map(int, input().split())
string = input().strip()
genes = ['A','C','G','T']
password = list(map(int, input().split()))
ans = 0

first_string = string[:P]
now = {genes[x] : first_string.count(genes[x]) for x in range(4)}

string = string + 'A'
for i in range(S-P+1): # 문자열 시작하는 index
    flag = True
    
    for j in range(4):
        if password[j] > list(now.values())[j]:
            flag = False
            break
    if flag:
        ans += 1

    now[string[i]] -= 1 # 현재 문자열의 맨 앞 문자
    now[string[i+P]] += 1 # 다음 문자열의 맨 뒤 문자
    
print(ans)


