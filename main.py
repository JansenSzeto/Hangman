import random
import os

j = []
got = 0
loss = 0

man = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def show():
    global j
    global got
    global loss
    os.system('cls')
    print(answer)
    print(len(answer))
    print(man[loss])
    print("".join(j))
    input_ = input()
    if len(input_) == 1 and input_.isalpha() == True:
        if input_ in list(answer):
            for x in range(len(answer)):
                if input_ == list(answer)[x]:
                    j[x] = f"""{input_} """
                    got += 1
        else:
            loss += 1
    show()
    


def start():
    f = open("words.txt", "r").readlines()
    k = list(f[random.randrange(0, 497)])
    del k[-1]
    global answer
    answer = "".join(k)
    global j
    for i in range(len(answer)):
        j.append("_ ")
    show()

if __name__ == "__main__":
    start()