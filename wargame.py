from random import shuffle

class Card:
    suits = ["spades","hearts","diamonds","clubs"]
    values = [None,None,"2","3","4","5",
              "6","7","8","9","10","Jack",
              "Queen","King","Ace"]

    def __init__(self,v,s):
        self.suit = s
        self.value = v

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        elif self.value == c2.value:
            return self.suit < c2.suit
        else:
            return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        elif self.value == c2.value:
            return self.suit > c2.suit
        else:
            return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return
        else:
            return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("name of player1 : ")
        name2 = input("name of player2 : ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def print_winner(self, winner):
        w = "{} win for this round."
        print(w.format(winner.name))

    def print_draw(self, p1, p2):
        d = "{} got {}, {} got {}."
        print(d.format(p1.name,p1.card,p2.name,p2.card))

    def play_game(self):
        cards = self.deck.cards
        print("WAR BEGINS!")
        while len(cards) >= 2:
            m = "\"q\" to quit, any others to play : "
            response = input(m)
            if response == "q":
                break
            else:
                self.p1.card = self.deck.draw()
                self.p2.card = self.deck.draw()
                self.print_draw(self.p1,self.p2)
                if self.p1.card > self.p2.card:
                    self.p1.wins += 1
                    self.print_winner(self.p1)
                else:
                    self.p2.wins += 1
                    self.print_winner(self.p2)

        win = self.winner(self.p1, self.p2)
        print("{}".format(win))
        print("{} : {}".format(self.p1.name,self.p1.wins))
        print("{} : {}".format(self.p2.name, self.p2.wins))


    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name + " win! "
        elif p1.wins < p2.wins:
            return p2.name + " win! "
        else:
            return "draw"

game = Game()
game.play_game()
        

