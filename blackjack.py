import random

player_cards = []
split = False

def create_deck():
    
    deck_vals = {}
    suits = ['D', 'H', 'S', 'C']
    face = ['J', 'Q', 'K']
    
    for x in range(2, 11):
        for y in suits:
            deck_vals.update({str(x) + y:x})

    for x in face:
        for y in suits:
            deck_vals.update({x + y:10})
            deck_vals.update({'A' + y:11})

    keys = deck_vals.keys()
    random.shuffle(keys)
    display_deck = [(key, deck_vals[key]) for key in keys]

    return display_deck

def blackjack(card1, card2):
    if card1 + card2 == 21:
        print 'you win'
    else:
        p1.choice()
         
class Player:

    def __init__(self, name, money):
        self.name = name.title()
        self.money = []

    def deal(self, created_deck):
        print "Here are your cards, " + self.name
        
        c1 = random.choice(created_deck)
        c2 = random.choice(created_deck)

        if c1[1] == c2[1]:
            split = True
            
        player_cards.append(c1[0] + ', ' + c2[0])

        created_deck.remove(c1)
        created_deck.remove(c2)
        
        print player_cards
        

        #Check for blackjack
        blackjack(c1[1], c2[1])

    
    def choice(self):
        while True:
            if split == True:
                s = raw_input("Do you want to split? [y/n]")
                
            c = raw_input("Do you want to [h]it or [s]tand?")
            if c.lower() == "h":
                new_card = random.choice(deck)
                cards.append(new_card)
                deck.remove(new_card)
                print cards
           # elif c.lower() == "s"
    

p1 = Player('emilio', 30)
p1.deal(create_deck())



