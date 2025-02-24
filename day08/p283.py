class Treenode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

node1 = Treenode()
node1.data='화사'

node2 = Treenode()
node2.data='솔라'
node1.left = node2

node3 = Treenode()
node3.data='문별'
node1.right = node3

node4 = Treenode()
node4.data='휘인'
node2.left = node4

node5 = Treenode()
node5.data='쯔위'
node2.right = node5

node6 = Treenode()
node6.data='선미'
node3.left = node6

print(node1.data,end=' ')
print()
print(node1.left.data,node1.right.data,end=' ')
print()
print(node1.left.left.data,node1.left.right.data,node1.right.left.data,end=' ')
print()

def preorder(node):
    if node == None:
        return
    print(node.data, end='->')      
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.data, end='->')
    inorder(node.right)

def postorder(node):
    if node == None:
        return
    postorder(node.left)
    preorder(node.right)
    print(node.data, end='->')

# 전위순회 - 노드처리->왼쪽->오른쪽 
print('전위 순회 : ', end =' ')
preorder(node1)
print('끝')

# 중위순회 - 왼쪽->노드처리->오른쪽
print('중위 순회 : ', end =' ')
inorder(node1)
print('끝')

# 후위순회 - 왼쪽->오른쪽->노드처리
print('후위 순회 : ', end =' ')
postorder(node1)
print('끝')