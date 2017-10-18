from collections import Counter

#Structure to represent nodes in a tree
#Letter is optional value since merging of two nodes will only hod a count value 
class Node:
    def __init__(self, count, letter=None):
        self.letter = letter
        self.count = count
        self.right = None
        self.left = None

word = input()
d = dict(Counter(word))

#List of nodes that is sorted based on word count from most frequent to least frequent
Nodes = [Node(d[w], w) for w in sorted(d, key=d.get, reverse=True)]

while len(Nodes) > 1:
    a = Nodes.pop()
    b = Nodes.pop()

    c = Node(a.count+b.count)
    c.left, c.right = a, b

    Nodes.append(c)
    Nodes.sort(key=lambda x: x.count, reverse=True)
          
print(Nodes[0].right.right.right.letter)