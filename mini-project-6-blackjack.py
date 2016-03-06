# demo for drawing using tiled images

import simplegui

# define globals for cards
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
SUITS = ('C', 'S', 'H', 'D')

# card sprite - 950x392
CARD_CENTER = (36.5, 49)
CARD_SIZE = (73, 98)
card_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

# define card class
class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def draw(self, canvas, loc):
        i = RANKS.index(self.rank)
        j = SUITS.index(self.suit)
        card_pos = [CARD_CENTER[0] + i * CARD_SIZE[0],
                    CARD_CENTER[1] + j * CARD_SIZE[1]]
        canvas.draw_image(card_image, card_pos, CARD_SIZE, loc, CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards_in_hand = []

    def __str__(self):
        # return a string representation of a hand
        cards_in_hand_readable = ""
        for card in self.cards_in_hand:
            cards_in_hand_readable += str(card) + " "
            # commented for unit test
            # if len(self.cards_in_hand) == 1:
            #     cards_in_hand_readable += "."
            # elif len(self.cards_in_hand) > 1:
            #     cards_in_hand_readable += ", "
            # else:
            #     pass

        # return "Hand contains: " + cards_in_hand_readable
        return "Hand contains " + cards_in_hand_readable

    def add_card(self, card):
        # add a card object to a hand
        self.cards_in_hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        self.value = 0

        for card in self.cards_in_hand:
            card_value = VALUES[card.get_rank()]
            self.value += card_value


        for card in self.cards_in_hand:
            if card.get_rank() == "A":
                if self.value + 10 <= 21:
                    self.value += 10

        return self.value

    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards

        for c in self.cards_in_hand:
            c.draw(canvas, pos)
            pos[0] += CARD_CENTER[0] * 2 + 10

# define deck class
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.deck.append(card)

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop()

    def __str__(self):
        # return a string representing the deck
        deck_readable = ""
        i = 0
        for card in self.deck:
            i += 1
            deck_readable += str(card) + " "
            # commented for unit test pass
            # if i < len(self.deck):
            #     deck_readable += ", "
            # else:
            #     deck_readable += "."

        # return "Deck contains: " + deck_readable
        return "Deck contains " + deck_readable

# define event handlers for buttons
def deal():
    global score, outcome, in_play, deck, dealer_hand, player_hand

    if in_play:
        score -= 1
        in_play = False

        print "You were still playing when you pressed Deal. You lose."
        outcome = "You were still playing when you pressed Deal. You lose."

    else:
        in_play = True
        outcome = ""

        deck = Deck()
        deck.shuffle()

        dealer_hand = Hand()
        player_hand = Hand()

        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())

        print "-" * 15
        print str(deck) + "\n"
        print "Dealer " + str(dealer_hand)
        print "Dealer hand value is " + str(dealer_hand.get_value()) + "\n"
        print "Player " + str(player_hand)
        print "Your hand value is "  + str(player_hand.get_value()) + "\n"

def hit():
    global in_play, score, outcome

    # if the hand is in play, hit the player
    if in_play:
        player_hand.add_card(deck.deal_card())
        print "Player " + str(player_hand)
        print "Your hand value is "  + str(player_hand.get_value()) + "\n"
    else:
        pass

    # if busted, assign a message to outcome, update in_play and score
    if player_hand.get_value() > 21 and in_play:
        print "Player " + str(player_hand)
        print "Your hand value is "  + str(player_hand.get_value())
        print "You have busted." + "\n"
        outcome = "You have busted."
        score -= 1
        in_play = False

def stand():
    global in_play, score, outcome
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if not in_play and player_hand.get_value() > 21:
        print "You have busted."
        outcome = "You have busted."


    elif not in_play and player_hand.get_value() <= 21:
        print "This game is ended. Press Deal button."
        outcome = "This game is ended. Press Deal button."

    else:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())

        # assign a message to outcome, update in_play and score
        if dealer_hand.get_value() > 21:
            print "Dealer hand value is " + str(dealer_hand.get_value())
            print "Dealer has busted. You win."
            outcome = "Dealer has busted. You win."
            in_play = False
            score += 1

        elif dealer_hand.get_value() < player_hand.get_value():
            print "Dealer hand value is " + str(dealer_hand.get_value())
            print "Your hand value is "  + str(player_hand.get_value())
            print "You win."
            outcome = "Dealer hand value is " + str(dealer_hand.get_value()) + ". Your hand value is "  + str(player_hand.get_value()) + ". You win."
            score += 1
            in_play = False

        elif dealer_hand.get_value() >= player_hand.get_value():
            print "Dealer hand value is " + str(dealer_hand.get_value())
            print "Your hand value is "  + str(player_hand.get_value())
            print "You lose."
            outcome = "Dealer hand value is " + str(dealer_hand.get_value()) + ". Your hand value is "  + str(player_hand.get_value()) + ". You lose."
            score -= 1
            in_play = False

# define draw handler
# draw handler
def draw(canvas):
    global score, outcome, in_play

    canvas.draw_text("Blackjack", (200, 60), 50, "Black")

    # dealer
    dealer_hand.draw(canvas, [100, 200])

    if in_play:
        # canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest)
        canvas.draw_image(card_back, (36, 48), (72, 96), (136, 248), (72, 96))

    # player
    player_hand.draw(canvas, [100, 400])

    # draw score
    canvas.draw_text("Score is: " + str(score), (400, 150), 20, "White")

    # draw outcome
    canvas.draw_text(outcome, (100, 350), 20, "White")

    # draw questions
    if in_play:
        canvas.draw_text("Hit or stand?", (103, 550), 20, "White")
    else:
        canvas.draw_text("New deal?", (103, 550), 20, "White")
        
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
