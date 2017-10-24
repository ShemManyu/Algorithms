import string
def main(val):
    alphabet = string.ascii_lowercase
    words = {alphabet.index(l) + 1:l for l in alphabet}

    return return_word(val, words)

def return_word(val, alphabet, word=''):
    mod = 26
    if int(val % 26) != 0:
        mod = int(val % 26)
        
    if val <=  26:
        word = alphabet[val] + word
        return word
    return return_word((val - mod) / 26, alphabet, alphabet[mod] + word)

if __name__ == "__main__":
    vals = []
    while True:
        inputs = input().strip()
        if inputs == '-1':
            break
        vals.append(int(inputs))
    for val in vals:
        print(main(val))