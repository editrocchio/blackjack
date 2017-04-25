import random

class Mechanics(object):
    
    def create_deck(self):
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
            deck_vals.update({'A' + y:[11,1]})
        
        items = deck_vals.items()
        random.shuffle(items)
        
        return items
    
    def ace_check(self, card_set_p, card_set_d):
        p = 0
        d = 0
        end = False
        for card in card_set_p:
            if 'A' not in card[0]:
                p += int(card[1])
            elif 'A' in card[0]:
                if p + int(card[1][0]) <= 21:
                    p += int(card[1][0])
                elif p + int(card[1][0]) > 21:
                    p += int(card[1][1])

        for card in card_set_d:
            if 'A' not in card[0]:
                d += int(card[1])
            elif 'A' in card[0]:
                if d + int(card[1][0]) <= 21:
                    d += int(card[1][0])
                elif d + int(card[1][0]) > 21:
                    d += int(card[1][1])

        for card in card_set_p:
            if 'A' in card[0] and p > 21 and end == False:
                p -= 10
                end = True
            else:
                pass

        for card in card_set_d:
            if 'A' in card[0] and d > 21 and end == False:
                d -= 10
                end = True
            else:
                pass

        return p, d

    def win_loss(self, p_cards, d_cards):
        global play

        p_checked, d_checked = self.ace_check(p_cards, d_cards)

        print p_checked
        print d_checked
                
        disp = []
        for card in d_cards:
            disp.append(card[0])
            
        if p_checked == 21 and d_checked != 21:
            print "Blackjack! You win. Dealer cards: " + str(disp)
            play = False
        elif p_checked != 21 and d_checked == 21:
            print "Dealer has blackjack, you lose. " + str(disp)
            play = False
        elif p_checked > 21:
            print "You bust. Dealer cards: " + str(disp) 
            play = False

    def stand_check(self, p_cards, d_cards):

        p_checked, d_checked = self.ace_check(p_cards, d_cards)

        print "Your total: " + str(p_checked) + "\nDealer total: " + str(d_checked)
            
        if p_checked == d_checked:
            print "Push."
        elif p_checked > d_checked:
            print "You win!"
        elif d_checked > p_checked:
            print "You lose."
        elif p_checked != 21 and d_checked == 21:
            print "Dealer has blackjack, you lose."

class Player(object):

    player_cards = []
    
    def __init__(self, money):
        self.money = money
           
    def choice(self):
        while play:
            c = raw_input("Do you want to [h]it or [s]tand? ")
            if c.lower() == "h":
                new_card = deck.pop(0)
                self.player_cards.append(new_card)
                dealer.display_cards(self.player_cards, dealer.dealer_cards)

            if c.lower() == "s":
                print "Dealer cards: " + str(dealer.dealer_cards[0][0]) + \
                      ", " + str(dealer.dealer_cards[1][0])
                dealer.self_deal(dealer.dealer_cards)
                break
                
class Dealer(object):

    dealer_cards = []
   
    def deal(self, created_deck):
        count = 0
        while count < 2:
            new_card = deck.pop(0)
            player.player_cards.append(new_card)
            new_card = deck.pop(0)
            self.dealer_cards.append(new_card)
            count += 1
                   
        self.display_cards(player.player_cards, dealer.dealer_cards)

    def self_deal(self, d_cards):
        while True:
            p_checked, d_checked = mechanics.ace_check(player.player_cards, d_cards)
            if d_checked < 17:
                new_card = deck.pop(0)
                self.dealer_cards.append(new_card)
                print "Dealing... " + new_card[0]
            elif d_checked > 21:
                print "Dealer busts at " + str(d_checked)
                break
            elif d_checked >= 17 and d_checked < 21:
                print "Dealer stands at " + str(d_checked)
                mechanics.stand_check(player.player_cards, dealer.dealer_cards)
                break
            elif d_checked == 21:
                print "Dealer has blackjack, you lose. " 
                break

    def display_cards(self, p_cards, d_cards):
        x = []
        y = []
        for card in p_cards:
            x.append(card[0])
        for card in d_cards:
            y.append(card[0])
            
        print "Here are your cards:\n" + str(x) + "\nHere is " \
              "the dealer card:\n" + str(y[0])
           
        mechanics.win_loss(player.player_cards, dealer.dealer_cards)

mechanics = Mechanics()
player = Player(30)
dealer = Dealer()
deck = mechanics.create_deck()

play = True

dealer.deal(deck)
player.choice()



