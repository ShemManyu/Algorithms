def main(t, m, o):
    print("{} {} {}".format(t, m, o))

if __name__ == "__main__":
    topings = []
    menu = []
    orders = []
    p = {}
    while True:
        inputs = input().strip()
        if inputs == '-1':
            break
        else:
            top, pizaa = inputs.split(" ")
            for i in range(int(top)):
                v, t = input().split(" ")
                topings.append((int(v), t))
            #for j in range(int(pizaa)):
            p_t_n = input().strip().split(" ")
            
            menu.append(int(p), int(t), n)

            number_t = input().split(" ")
            orders = tuple([i for i in number_t])

    main(topings, menu, orders)