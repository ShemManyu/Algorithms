from collections import Counter
import copy

#Structure to represent nodes in a tree
#Letter is optional value since merging of two nodes will only hod a count value 
class HuffNode:
    def __init__(self, count, letter=None):
        self.letter = letter
        self.count = count
        self.right = None
        self.left = None

word = input()
d = dict(Counter(word))

#List of nodes that is sorted based on word count from most frequent to least frequent
Nodes = [HuffNode(d[w], w) for w in sorted(d, key=d.get, reverse=True)]

while len(Nodes) > 1:
    a = Nodes.pop()
    b = Nodes.pop()

    c = HuffNode(a.count+b.count)
    c.left, c.right = a, b

    Nodes.append(c)
    Nodes.sort(key=lambda x: x.count, reverse=True)

def printcode(l, n, code = ''):
    if n.letter == l:
        return code
    else:
        try:
            #print(n.count)
            return printcode(l, n.left, code + '0')
        except:
            #print(n.count)
            return printcode(l, n.right, code + '1')

#def traversal(node, d):
#    codes = copy.deepcopy(d)
#    for k in d.keys():
#        pass
#    if node.left == None and node.right == None:
        
print(printcode('h', Nodes[0]))