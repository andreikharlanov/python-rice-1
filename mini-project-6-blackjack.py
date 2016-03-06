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
        pass	# draw a hand on the canvas, use the draw method for cards
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

# define draw handler
def draw(canvas):
    one_card.draw(canvas, (155, 90))

# define frame and register draw handler
frame = simplegui.create_frame("Card draw", 300, 200)
frame.set_draw_handler(draw)

# createa card
one_card = Card('H', 'A')

frame.start()
