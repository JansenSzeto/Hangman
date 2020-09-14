import random
import os
import sys

j = []
tried = []
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

def win():
    os.system('cls')
    print("You won!")
    input()
    sys.exit(0)

def loss_():
    os.system('cls')
    print("You loss!")
    print(man[6])
    input()
    sys.exit(0)

def show():
    global j
    global got
    global loss
    global tried
    os.system('cls')
    print(answer)
    print(man[loss])
    print("".join(j))
    print(" ".join(tried))
    input_ = input()
    if len(input_) == 1 and input_.isalpha() == True:
        if input_ in list(answer):
            for x in range(len(answer)):
                if input_ == list(answer)[x]:
                    j[x] = f"""{input_} """
                    got += 1
        else:
            if input_ in tried:
                pass
            else:
                loss += 1
                tried.append(input_)
    if got == len(answer):
        win()
    if loss == 6:
        loss_()
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