## 클래스와 함수 선언 부분 ##
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGhaph(g): 
    global nameAry 
    print('\t', end='\t')
    for v in range(g.SIZE):
        print(nameAry[v], end='\t')
    print()

    for row in range(g.SIZE):
        print(nameAry[row], end='\t\t') 
        for col in range(g.SIZE):
            print(f'{g.graph[row][col]:>4d}', end='\t')
        print()

    print()