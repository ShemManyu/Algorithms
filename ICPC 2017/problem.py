import string
def main(sent):
    count = 0
    alphabet = string.ascii_lowercase
    wcount = {a:0 for a in alphabet}
    words = sent.lower().split(" ")
    sentence = ''.join(words)
    for word in words:
        if (set(word) & set(alphabet)) != set():
            count += 1
    for k in wcount.keys():
        wcount[k] = sentence.count(k)

    print("{}".format(count), end=" ")
    for k in sorted(wcount.keys()):
        print(wcount[k], end=" ")
    print("")

if __name__ == "__main__":
    sentences = []
    while True:
        inputs = input().strip()
        if inputs == '-1':
            break
        else:
            sentences.append(inputs)
    for sent in sentences:
        main(sent)