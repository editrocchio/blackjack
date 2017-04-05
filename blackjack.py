import random

suits = ['D', 'H', 'S', 'C']
face = ['J', 'Q', 'K', 'A']
deck = []
cards = []

for x in range(2, 11):
    for y in suits:
        deck.append(str(x) + y)

for x in face:
    for y in suits:
        deck.append(x + y)

print deck

class Player:

    def __init__(self, name):
        self.name = name.title()

    def deal(self):
        print 'Here are your cards, ' + self.name
        random.shuffle(deck)
        c1 = random.choice(deck)
        c2 = random.choice(deck)
        cards.append(c1 + ' ' + c2)
        return cards

    def choice(self):
        while True:
            c = raw_input('Do you want to [h]it, [f]old, or [s]plit? ')
            if c.lower() == 'h':
                cards.append(random.choice(deck))
                print cards
        

p1 = Player('emilio')

p1.deal()
p1.choice()

