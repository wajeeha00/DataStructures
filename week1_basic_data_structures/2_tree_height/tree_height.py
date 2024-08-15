# python3

import sys
import threading

class Node:
    def __init__(self):
        self.children=[]
    def addChild(self,child):
        self.children.append(child)

def height(current_node,nodes):
    if len(nodes[current_node].children)==0:
        return 1  
    else:
        h_c=[]
        for c in nodes[current_node].children:
            h_c.append(height(c,nodes))
        return 1+max(h_c)
def compute_height(n, parents):
    nodes=[Node() for i in range(n)]
    for i in range(n):
        if parents[i]==-1:
            root=i
        else:
            nodes[parents[i]].addChild(i)
    return height(root,nodes)



def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
