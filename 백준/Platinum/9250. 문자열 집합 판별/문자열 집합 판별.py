import sys
from collections import deque
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = dict()  
        self.fail = None        
        self.output = []        

class Ahocorasick:
    def __init__(self):
        self.root = Node()  

    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node()
            cur = cur.children[ch]
        cur.output.append(word) 

    def failure_links(self):
        q = deque()

        for child in self.root.children.values():
            child.fail = self.root
            q.append(child)

        while q:
            curr_node = q.popleft()
            for ch, child_node in curr_node.children.items():
                q.append(child_node)
                fail_node = curr_node.fail
                
                while fail_node is not None and ch not in fail_node.children:
                    fail_node = fail_node.fail
                    
                if fail_node is None:
                    child_node.fail = self.root
                else:
                    child_node.fail = fail_node.children[ch]

                child_node.output += child_node.fail.output

    def search(self, text):
        ptr = self.root
        for char in text:
            while ptr != self.root and char not in ptr.children:
                ptr = ptr.fail

            if char in ptr.children:
                ptr = ptr.children[char]
            else:
                ptr = self.root

            if ptr.output:
                return True
        return False


def main():
    aho = Ahocorasick()
    N = int(input())
    for _ in range(N):
        word = input().strip()
        aho.insert(word)
    aho.failure_links()
    Q = int(input())
    for _ in range(Q):
        query = input().strip()
        if aho.search(query):
            print('YES')
        else:
            print('NO')
main()
