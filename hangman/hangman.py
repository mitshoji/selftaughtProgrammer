import random


def wordselect():
    
    filepath = "/media/mitsuru/data/python/hangman/quantum.txt"

    with open(filepath, "r") as f:
        word_list = f.read()

    words = word_list.split(" ")
    upr = len(words)
    windex = random.randint(0,upr)

    return words[windex]



keyword = wordselect()



def hangman(word):
    wrong = 0
    stages = ["",
              "________       ",
              "|              ",
              "|       |      ",
              "|       0      ",
              "|      /|\     ",
              "|      / l     ",
              "|              ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to the Hangman!")


    while wrong < len(stages) - 1 :
        print("\n")
        msg = "Guess a letter :  "
        char = input(msg)

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1

        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[:e]))

        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[:wrong+1]))
        print("You lose... the word is {}.".format(word))


hangman(keyword)
