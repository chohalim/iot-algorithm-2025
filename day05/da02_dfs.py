# da02_dfs.py
# 그래프 깊이 우선탐색

# 전역변수
stack = [] # 스택
visitedAry = [] # 방문기록
G1 = None

# 그래프 클래스
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

## 메인코드
SIZE = 4
G1 = Graph(SIZE)
# 0:A, 1:B, 2:C, 3:D
G1.graph[0][2] = 1
G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1
G1.graph[2][1] = 1
G1.graph[2][3] = 1
G1.graph[3][0] = 1
G1.graph[3][2] = 1

print('## G1 무방향 그래프')
for row in range(G1.SIZE):
    for col in range(G1.SIZE):
        print(G1.graph[row][col], end=' ')
    print()

print('## DFS 시작!')

current = 0 # A
stack.append(current) # Stack push(A)
visitedAry.append(current) # 방문기록(A)

while len(stack) != 0: # Stack 길이가 0이 되면 모든 정점을 방문했다는 뜻 ## 스택의 길이가 0이 아닐동안 while반복
    next = None
    for vertex in range(SIZE):
        if G1.graph[current][vertex] == 1: # 간선이 있다
            if vertex in visitedAry: # 도착점이 이미 방문한 곳이면
                continue # 됐고
            else: # 그렇지 않으면
                next = vertex # 그 정점을 다음 방문할 곳으로 해라
                break
    
    if next != None: # 다음에 방문할 정점이 있다(넌이 아님)
        current = next # 현재시점의 이동
        stack.append(current) # 이동한 현재를 스택에 추가
        visitedAry.append(current) # 방문기록에도 추가
    else:
        current = stack.pop() # 다음에 방문할 정점이 없으면 스택에서 꺼내자

print('방문순서', end='->')
for i in visitedAry:
    print(chr(ord('A')+i),end=' ')

print() # 붙여나오지 않게 하려고
print(chr(ord('A')+0)) # A의 ASCII 코드 값 출력




        

