import random

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

    for y in suits:
        deck_vals.update({'A' + y:11})
    
    items = deck_vals.items()
    random.shuffle(items)
    
    return items

def win_loss(card_set):
    global play
    c = 0
    for card in card_set:
        c += int(card[1])
        if c == 21:
            print "you win"
            play = False
        elif c > 21:
            print "you lose"
            play = False
        else:
            pass

def display_cards(card_set):
    x = []
    for card in card_set:
        x.append(card[0])

    print "Here are your cards:\n" + str(x)

    win_loss(player_cards)
         
class Player:

    def __init__(self, name, money):
        self.name = name.title()
        self.money = []

    def deal(self, created_deck):
        count = 0
        while count < 2:
            chosen_card = random.choice(created_deck)
            created_deck.remove(chosen_card)
            count += 1
            player_cards.append(chosen_card)
                   
        display_cards(player_cards)
           
    def choice(self):
        while play:
          #  if split == True:
           #     s = raw_input("Do you want to split? [y/n]")
                
            c = raw_input("Do you want to [h]it or [s]tand?")
            if c.lower() == "h":
                new_card = random.choice(create_deck())
                player_cards.append(new_card)
                display_cards(player_cards)
                
    #        elif c.lower() == "s":
                
play = True
split = False
player_cards = []
p1 = Player('bob', 30)
p1.deal(create_deck())
p1.choice()


