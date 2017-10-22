from collections import Counter

#Structure to represent nodes in a tree
#Letter parameter is optional since merging of two nodes will only hold a count value 
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

#This could be done better. After two letters are merged
#generate a new node and append it to the list of nodes then sort the list
while len(Nodes) > 1:
    a = Nodes.pop()
    b = Nodes.pop()

    c = HuffNode(a.count+b.count)
    c.left, c.right = a, b

    Nodes.append(c)
    Nodes.sort(key=lambda x: x.count, reverse=True)

def make_code(node, prefix=''):
    if node is None:
        return []
    if node.letter is not None:
        return [(prefix, node.letter)]
    else:
        result = []
        result.extend(make_code(node.left, prefix + '0'))
        result.extend(make_code(node.right, prefix + '1'))
        return result

print(make_code(Nodes[0]))