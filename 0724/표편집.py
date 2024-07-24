'''
https://school.programmers.co.kr/learn/courses/30/lessons/81303
'''
'''
Linked list (연결리스트) 

- 각 데이터가 다음 데이터의 위치를 가리키는 형태로 구성 (단방향)
* 양방향이라면 이전, 다음 데이터의 위치를 같이 포함 (이전-현재-다음)
* 자료를 추가하거나 삭제하는 일이 많다면 연결리스트 자료구조 활용 *
'''
class Node: # 현재 삭제 여부, 이전 노드 정보, 다음 노드 정보
    survived = True
    def __init__(self, p, n):
        self.prev = p if p >= 0 else None
        self.next = n if n < N else None

def solution(n, k, command):
    global N
    N = n
    table = {i : Node(i-1,i+1) for i in range(n)}
    current = k
    removed = []

    for cmd in command:
        if cmd == 'C': # 삭제 (이전 노드와 다음 노드 연결)
            table[current].survived = False
            removed.append(current)

            c_prev, c_next = table[current].prev, table[current].next
            if c_prev is not None:
                table[c_prev].next = c_next
            if c_next is not None:
                table[c_next].prev = c_prev
                            
            # 현재 위치 설정
            if c_next is None: # 뒤에 더 없다면 
                current = c_prev
            else:
                current = c_next

        elif cmd == 'Z' : # 되돌리기
            recovered = removed.pop()
            table[recovered].survived = True

            r_prev, r_next = table[recovered].prev, table[recovered].next
            if r_prev is not None:
                table[r_prev].next = recovered
            if r_next is not None:
                table[r_next].prev = recovered

        else: # 위, 아래 이동
            c, amount = cmd.split()
            if c == 'U':
                for _ in range(int(amount)):
                    current = table[current].prev
            
            else:
                for _ in range(int(amount)):
                    current = table[current].next

    return ''.join(['O' if table[i].survived else 'X' for i in range(n)])

