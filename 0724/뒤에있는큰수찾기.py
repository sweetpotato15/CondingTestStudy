'''
https://school.programmers.co.kr/learn/courses/30/lessons/154539
'''

'''
자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수 - 뒷큰수
내가 누군가의 뒷큰수가 될수 있냐의 관점

q에 numbers의 뒤에서부터 삽입하고, 앞으로 가면서 q에 있는 값이 뒷큰수가 될 수 있는지 chk
'''
from collections import deque

def solution(numbers):
    q = deque()
    numbers = deque(enumerate(numbers)) #(index, value) 형태
    answer = [-1] * len(numbers)

    while numbers: # numbers에서 top 보다 작거나 같은 애들 삭제 
        top = numbers.pop()
        while q and q[-1][1] <= top[1]:
            q.pop()       
        if q:
            answer[top[0]] = q[-1][1]      
        q.append(top)

    return answer