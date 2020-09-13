import random

def show():
    print(answer)
    print(len(answer))
    j = []
    for i in range(len(answer)):
        j.append("_ ")
    print("".join(j))

def start():
    f = open("words.txt", "r").readlines()
    k = list(f[random.randrange(0, 497)])
    del k[-1]
    global answer
    answer = "".join(k)
    show()

if __name__ == "__main__":
    start()