def main(word):
    if word == word[::-1]:
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    vals = []
    while True:
        inputs = input().strip()
        if inputs == '-1':
            break
        else:
            vals.append(inputs)
    for w in vals:
        main(w)