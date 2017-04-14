import random


deck = []
actual_vals = []
cards = []

def create_deck():

    deck[:] = []
    actual_vals[:] = []
    
    suits = ['D', 'H', 'S', 'C']
    face = ['J', 'Q', 'K', 'A']
    
    for x in range(2, 11):
        for y in suits:
            deck.append(str(x) + y)

    for x in face:
        for y in suits:
            deck.append(x + y)

    return deck

created_deck = create_deck()

def get_actual_vals(c, value):
    actual_vals = deck
    for card in actual_vals:
        if card[0] == c:
            card[0] == value
            print card
            
def blackjack():
        for card in deck:
            print card[0]
    
    
class Player:

    def __init__(self, name):
        self.name = name.title()

    def deal(self):
        print "Here are your cards, " + self.name
        random.shuffle(deck)
        c1 = random.choice(deck)
        c2 = random.choice(deck)
        cards.append(c1 + ', ' + c2)
        print cards
        
        deck.remove(c1)
        deck.remove(c2)

    
    def choice(self):
        while True:
            c = raw_input("Do you want to [h]it, [f]old, or [s]plit? ")
            if c.lower() == "h":
                new_card = random.choice(deck)
                cards.append(new_card)
                deck.remove(new_card)
                print cards
           # elif c.lower() == "f"
      #      elif c.lower == "s" 

p1 = Player('emilio')
print created_deck
get_actual_vals('K', '10')
p1.deal()
blackjack()
# p1.choice()


