import random


class Card(object):

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return self.show_card()

    def __repr__(self):
        return self.show_card()

    def show_card(self):
        return "{} of {}".format(self.value, self.suit)

    def evaluate_points(self):

        for i in range(2, 11):
            if self.value == i:
                return int(i)

        if self.value == "Jack" or self.value == "Queen" or self.value == "King":
            return int(10)

        else:
            return int(11)


class Deck(object):
    suits = ["Diamonds", "Spades", "Hearts", "Clubs"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

    def __init__(self):
        self.deck = []
        self.build_deck()
        self.shuffle_cards()

    def build_deck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append(Card(value, suit))

    def shuffle_cards(self):
        return random.shuffle(self.deck)

    def show_deck(self):
        for card in self.deck:
            print(card.show_card())

    def empty_deck(self):
        self.deck = []

    def draw_card(self):
        return self.deck.pop()


class Player(object):
    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw(self, deck):
        self.hand.append(Deck.draw_card(deck))
        return self

    def show_hand(self):
        for card in self.hand:
            print("Player Card: " + card.show_card())

    def evaluate_hand_points(self):
        points = 0
        for i in self.hand:
            points += i.evaluate_points()
        return points


class Dealer(object):
    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw(self, deck):
        self.hand.append(Deck.draw_card(deck))
        return self

    def show_hand(self):
        for card in self.hand:
            print("Dealer card:" + card.show_card())

    def evaluate_hand_points(self):
        points = 0
        for i in self.hand:
            points += i.evaluate_points()
        return points


f_deck = Deck()

dealer = Dealer("dealer")
dealer.draw(f_deck).draw(f_deck)
total = dealer.evaluate_hand_points()
print("Dealer total:", total)


def totaled():
    if total < 17:
        global totallied
        global totalotaled
        dealer.draw(f_deck)
        totallied = dealer.evaluate_hand_points()
        print("Dealer total:", str(totallied))
        if totallied < 17:
            dealer.draw(f_deck)
            totalotaled = dealer.evaluate_hand_points()
            print("Dealer total:", str(totalotaled))
            if totalotaled < 17:
                dealer.draw(f_deck)
                totalized = dealer.evaluate_hand_points()
                print("Dealer total:", str(totalized))


totaled()


dealer.show_hand()
player = Player("player")
player.draw(f_deck)
player.show_hand()
playtotal = player.evaluate_hand_points()
print("Player total: ", playtotal)
hit = input("Hit or Stay?")


def hitme():
    if hit == "Hit":
        player.draw(f_deck)
        player.show_hand()
        playtotaled = player.evaluate_hand_points()
        print("Player total: ", playtotaled)
        if playtotaled > 21:
            print("Bust! You lose, better luck next time!")
        elif playtotaled == 21:
            print("You win!!")
        elif playtotaled < 21:
            hitter = input("Hit or Stay?")
            if hitter == "Stay":
                if 21 - playtotaled < 21 - total:
                    print("You beat the computer, good job!!")
                elif 21 - playtotaled > 21 - total:
                    print("Sorry the computer beat you this time!")
            elif hitter == "Hit":
                player.draw(f_deck)
                player.show_hand()
                playaplaya = player.evaluate_hand_points()
                print("Player total: ", playaplaya)
                if playaplaya > 21:
                    print("Bust! You lose, better luck next time!")
                elif playaplaya == 21:
                    print("You win!!")
                elif playaplaya < 21:
                    hittery = input("Hit or Stay?")
                    if hittery == "Stay":
                        if 21 - playtotaled < 21 - total:
                            print("You beat the computer, good job!!")
                        elif 21 - playtotaled > 21 - total:
                            print("Sorry the computer beat you this time!")
                    elif hittery == "Hit":
                        player.draw(f_deck)
                        player.show_hand()
                        playaplayit = player.evaluate_hand_points()
                        print("Player total: ", playaplayit)
                        if playaplayit > 21:
                            print("Bust! You lose, better luck next time!")
                        elif playaplayit == 21:
                            print("You win!!")
                        if playaplayit < 21:
                            hitityo = input("Hit or Stay?")
                            if hitter == "Stay":
                                if 21 - playtotaled < 21 - total:
                                    print("You beat the computer, good job!!")
                                elif 21 - playtotaled > 21 - total:
                                    print(
                                        "Sorry the computer beat you this time!")
                            if hitityo == "Hit":
                                player.draw(f_deck)
                                player.show_hand()
                                playaplayedd = player.evaluate_hand_points()
                                print("Player total: ", playaplayedd)
                # elif playaplaya > 21:
                #     print("You lose!!")


hitme()

if 21 - playtotal < 21 - total:
    print("You beat the computer, good job!!")
