def main(lang, person):
    if lang == 0:
        print("Bonjour {}".format(person))
    elif lang == 1:
        print("Ola {}".format(person))
    else:
        print("Hello {}".format(person))

if __name__ == "__main__":
    vals = []
    while True:
        inputs = input().strip()
        if inputs == '-1':
            break
        else:
            lang, person = inputs.split(" ")
            vals.append((int(lang), person))
    for k,v in enumerate(vals):
        main(vals[k][0], vals[k][1])