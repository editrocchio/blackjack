import random
import time

class Mechanics(object):
    
    def create_deck(self):
        #Generate numbers from 2-10 and give them suits. Stores them in dict with their values.
        #Do the same for the face cards. Give aces a value of 11.
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
    
    def ace_check(self, card_set_p, card_set_d):
        #Add up the value of all cards, and number of aces. For each ace, subtract 10 until value is less than 21.
        p = 0
        d = 0
        ace_count_p = 0
        ace_count_d = 0
        
        for card in card_set_p:
            p += int(card[1])
            if 'A' in card[0]:
                ace_count_p += 1
                
        for card in card_set_d:
            d += int(card[1])
            if 'A' in card[0]:
                ace_count_d += 1

        if ace_count_p > 0:
            for num in range(ace_count_p):
                if p > 21:
                    p -= 10

        if ace_count_d > 0:
            for num in range(ace_count_d):
                if d > 21:
                    d -= 10

        return p, d

    def win_loss(self, p_cards, d_cards):
        #Basic check  for win conditions, if cards are both 21, either player or dealer has 21,
        #or player has higher than 21, end the player's choice and restart the round.
        global play

        p_checked, d_checked = self.ace_check(p_cards, d_cards)
        
        deck = []        
        disp = []
        for card in d_cards:
            disp.append(card[0])

        print "Your total: " + str(p_checked)

        if p_checked == 21 and d_checked == 21:
            print "You and dealer both have 21... Push." + \
                  "\n--------------------"
            player.money += int(wager)
            play = False
            
        elif p_checked == 21 and d_checked != 21:
            print "Blackjack! You win. Dealer cards: " + str(disp) + \
                  "\n--------------------"
            player.money += int((wager*2))
            play = False
            
        elif p_checked != 21 and d_checked == 21:
            print "Dealer has blackjack, you lose. " + str(disp) + \
                  "\n--------------------"
            play = False
            
        elif p_checked > 21:
            print "You bust. Dealer cards: " + str(disp) + \
                  "\n--------------------"
            play = False
            
        else:
            pass
        

    def stand_check(self, p_cards, d_cards):
        #Compares dealer cards to player cards on stand.
        p_checked, d_checked = self.ace_check(p_cards, d_cards)

        print "Your total: " + str(p_checked) + "\nDealer total: " + str(d_checked)
            
        if p_checked == d_checked:
            player.money += int(wager)
            print "Push." + \
                  "\n--------------------"
        elif p_checked > d_checked:
            player.money += int((wager*2))
            print "You win!" + \
                  "\n--------------------"
        elif d_checked > p_checked:
            player.money -= int(wager)
            print "You lose." + \
                  "\n--------------------"
        elif p_checked != 21 and d_checked == 21:
            player.money -= int(wager)
            print "Dealer has blackjack, you lose." + \
                  "\n--------------------"

class Player(object):

    player_cards = []
    
    def __init__(self, money):
        self.money = money
           
    def choice(self):
        #If hit, add new card and call display_cards, which calls win_loss function to check for win conditions.
        #If stand, call stand_check to check for win conditions.
        global play
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
                play = False

    def bet(self):
        betting = True
        while betting:
            try:
                print "You have $" + str(self.money) + " remaining."
                amount = raw_input("Enter wager: ")
                if int(amount) > self.money:
                    print "You don't have enough, you have $" + str(self.money) + \
                          " remaining."
                else:
                    print "Wagering " + "$" + amount
                    self.money -= int(amount)
                    betting = False
            except ValueError:
                print "Please enter an integer."
        
        time.sleep(0.5)
        
        return amount        
                
class Dealer(object):

    dealer_cards = []
   
    def deal(self, created_deck):
        player.player_cards[:] = []
        dealer.dealer_cards[:] = []
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
                time.sleep(0.5)
            elif d_checked > 21:
                print "Dealer busts at " + str(d_checked)
                player.money += int((wager*2))
                break
            elif d_checked >= 17 and d_checked < 21:
                print "Dealer stands at " + str(d_checked)
                mechanics.stand_check(player.player_cards, dealer.dealer_cards)
                break
            elif d_checked == 21:
                print "Dealer has blackjack, you lose. "
                player.money -= int(wager)
                break

    def display_cards(self, p_cards, d_cards):
        x = []
        y = []
        disp_total = []
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

while player.money > 0:
    wager = player.bet()
    wager = int(wager)
    play = True
    deck = mechanics.create_deck()
    dealer.deal(deck)
    if play == True:
        player.choice()

print "You're out of money, game over."
