class Town:
    def __init__(self,has):
        self.left = None
        self.right = None
        self.has = has

def main(t, c):
    towns = [Town(int(o)) for o in t[0]]

    for i in c:
        towns[i+1]

if __name__ == "__main__":
    towns = []
    path = []
    while True:
        inputs = input().strip()
        if inputs == '-1':
            break
        else:
            n = int(inputs)
            towns.append(input().split(" "))
            path.append(input().split(" "))
    for town in towns:
        main(towns, path)