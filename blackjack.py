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
        
class Player(object):

    player_cards = []
    dealer_cards = []

    def __init__(self, money):
        self.money = []

    def win_loss(self, p_cards, d_cards):
        global play
        p = 0
        d = 0
        for card in p_cards:
            p += int(card[1])
        for card in d_cards:
            d += int(card[1])
        
        if p == 21 and d == 21:
            print "Push."
            play = False
        elif p == 21 and d != 21:
            print "Blackjack!"
            play = False
        elif p != 21 and d == 21:
            print "Dealer has blackjack, you lose."
            play = False
        elif p > 21:
            print "You bust."
            play = False
        else:       
            pass
    
    def display_cards(self, p_cards, d_cards):
        x = []
        y = []
        for card in p_cards:
            x.append(card[0])
        for card in d_cards:
            y.append(card[0])
        
        print "Here are your cards:\n" + str(x) + "\nHere is " \
              "the dealer card:\n" + str(y[0])
           
        self.win_loss(self.player_cards, self.dealer_cards)
           
    def choice(self):
        while play:
            c = raw_input("Do you want to [h]it or [s]tand? ")
            if c.lower() == "h":
                new_card = random.choice(create_deck())
                self.player_cards.append(new_card)
                self.display_cards(self.player_cards, self.dealer_cards)
                
class Dealer(Player):
   
    def deal(self, created_deck):
        count = 0
        while count < 2:
            chosen_card = deck.pop(0)
            self.player_cards.append(chosen_card)
            chosen_card = deck.pop(0)
            self.dealer_cards.append(chosen_card)
            count += 1
                   
        self.display_cards(self.player_cards, self.dealer_cards)

deck = create_deck()
play = True
player = Player(30)
dealer = Dealer(30)
dealer.deal(deck)
player.choice()



