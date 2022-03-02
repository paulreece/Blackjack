import random
from click import style
from colorama import init
from colorama import Fore, Back, Style
import os
import sys
init()


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
    suits = [Fore.WHITE + Style.BRIGHT + Back.RED +
             "Diamonds", Fore.BLACK + Back.WHITE + Style.NORMAL + "Spades", Fore.WHITE + Style.BRIGHT + Back.RED + "Hearts", Fore.BLACK + Back.WHITE + Style.NORMAL + "Clubs"]
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
            print(Fore.WHITE + Style.BRIGHT + Back.MAGENTA +
                  "Player Card: " + card.show_card())

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
            print(Fore.WHITE + Style.BRIGHT + Back.BLUE +
                  "Dealer card:" + card.show_card())

    def evaluate_hand_points(self):
        points = 0
        for i in self.hand:
            points += i.evaluate_points()
        return points


def restart():
    restart = input("\nDo you want to restart the Game? [y/n] > ")
    if restart == "y":
        os.execl(sys.executable, sys.executable,
                 os.path.abspath(__file__), *sys.argv)
    else:
        print("\nGoodbye, thanks for playing!")
        sys.exit(0)


f_deck = Deck()

dealer = Dealer("dealer")
dealer.draw(f_deck).draw(f_deck)


def totaled():
    global total
    total = dealer.evaluate_hand_points()
    if total > 21:
        print("Dealer Bust!  You win!!!")
        restart()
    elif total >= 17:
        print(Fore.WHITE + Style.BRIGHT +
              Back.BLUE + "Dealer total:", str(total))
    elif total < 17:
        dealer.draw(f_deck)
        total = dealer.evaluate_hand_points()
        print(Fore.WHITE + Style.BRIGHT + Back.BLUE +
              "Dealer total:", str(total))
        if total > 21:
            print("Dealer Bust!  You win!!!")
            restart()
        elif total < 17:
            dealer.draw(f_deck)
            total = dealer.evaluate_hand_points()
            print(Fore.WHITE + Style.BRIGHT + Back.BLUE +
                  "Dealer total:", str(total))
            if total > 21:
                print("Dealer Bust!  You win!!!")
                restart()
            elif total < 17:
                dealer.draw(f_deck)
                total = dealer.evaluate_hand_points()
                print(Fore.WHITE + Style.BRIGHT + Back.BLUE +
                      "Dealer total:", str(total))


dealer.show_hand()
player = Player("player")
player.draw(f_deck)
player.show_hand()
playtotal = player.evaluate_hand_points()

theTotal = totaled()
print(Fore.WHITE + Style.BRIGHT + Back.MAGENTA + "Player total:", playtotal)


def hitme():
    action = ["Hit", "Stay"]
    hit = input(Fore.WHITE + Style.BRIGHT + Back.GREEN + "Hit or Stay? ")
    while hit not in action:
        if hit not in action:
            print("Please type Hit or Stay.")
            hit = input(Fore.WHITE + Style.BRIGHT +
                        Back.GREEN + "Hit or Stay? ")
        elif hit in action:
            break
    if hit == "Hit":
        player.draw(f_deck)
        player.show_hand()
        playtotaled = player.evaluate_hand_points()
        print(Fore.WHITE + Style.BRIGHT + Back.BLUE + "Dealer total:", total)
        print(Fore.WHITE + Style.BRIGHT + Back.MAGENTA +
              "Player total:", playtotaled)
        if 21 - playtotaled < 21 - total:
            print("You beat the computer, good job!!")
            restart()
        elif playtotaled == total:
            print("Draw!!!")
            restart()
        elif playtotaled == 21:
            print("You win!!")
            restart()
        elif playtotaled < 21:
            hitter = input(Fore.WHITE + Style.BRIGHT +
                           Back.GREEN + "Hit or Stay? ")
            while hitter not in action:
                if hitter not in action:
                    print("Please type Hit or Stay.")
                    hitter = input(Fore.WHITE + Style.BRIGHT +
                                   Back.GREEN + "Hit or Stay? ")
                elif hitter in action:
                    break
            if hitter == "Stay":
                if 21 - playtotaled < 21 - total:
                    print("You beat the computer, good job!!")
                    restart()
                elif playtotaled == total:
                    print("Draw!!!")
                    restart()
                elif playtotaled == 21:
                    print("You win!!")
                    restart()
                elif 21 - playtotaled > 21 - total:
                    print("Bust!! Sorry the computer beat you this time!")
                    restart()
            elif hitter == "Hit":
                player.draw(f_deck)
                player.show_hand()
                playaplaya = player.evaluate_hand_points()
                print(Fore.WHITE + Style.BRIGHT +
                      Back.BLUE + "Dealer total:", total)
                print(Fore.WHITE + Style.BRIGHT +
                      Back.MAGENTA + "Player total:", playaplaya)
                if playaplaya > 21:
                    print("Bust! You lose, better luck next time!")
                    restart()
                elif playaplaya == total:
                    print("Draw!!!")
                    restart()
                elif playaplaya == 21:
                    print("You win!!")
                    restart()
                elif playaplaya < 21:
                    hittery = input(Fore.WHITE + Style.BRIGHT +
                                    Back.GREEN + "Hit or Stay? ")
                    while hittery not in action:
                        if hittery not in action:
                            print("Please type Hit or Stay.")
                            hittery = input(Fore.WHITE + Style.BRIGHT +
                                            Back.GREEN + "Hit or Stay? ")
                        elif hittery in action:
                            break
                    if hittery == "Stay":
                        if 21 - playaplaya < 21 - total:
                            print("You beat the computer, good job!!")
                            restart()
                        elif playaplaya == total:
                            print("Draw!!!")
                            restart()
                        elif playaplaya == 21:
                            print("You win!!")
                            restart()
                        elif 21 - playaplaya > 21 - total:
                            print("Bust!! Sorry the computer beat you this time!")
                            restart()
                    elif hittery == "Hit":
                        player.draw(f_deck)
                        player.show_hand()
                        playaplayit = player.evaluate_hand_points()
                        print(Fore.WHITE + Style.BRIGHT +
                              Back.BLUE + "Dealer total:", total)
                        print(Fore.WHITE + Style.BRIGHT +
                              Back.MAGENTA + "Player total:", playaplayit)
                        if playaplayit > 21:
                            print("Bust! You lose, better luck next time!")
                            restart()
                        elif playaplayit == 21:
                            print("You win!!")
                            restart()
                        if playaplayit < 21:
                            hitityo = input(
                                Fore.WHITE + Style.BRIGHT + Back.GREEN + "Hit or Stay?")
                            while hitityo not in action:
                                if hitityo not in action:
                                    print("Please type Hit or Stay.")
                                    hitityo = input(Fore.WHITE + Style.BRIGHT +
                                                    Back.GREEN + "Hit or Stay? ")
                                elif hitityo in action:
                                    break
                            if hitter == "Stay":
                                if 21 - playaplayit < 21 - total:
                                    print("You beat the computer, good job!!")
                                    restart()
                                elif playaplayit == total:
                                    print("Draw!!!")
                                    restart()
                                elif playaplayit == 21:
                                    print("You win!!")
                                    restart()
                                elif 21 - playaplayit > 21 - total:
                                    print(
                                        "Bust!! Sorry the computer beat you this time!")
                                    restart()
                            if hitityo == "Hit":
                                player.draw(f_deck)
                                player.show_hand()
                                playaplayedd = player.evaluate_hand_points()
                                print(Fore.WHITE + Style.BRIGHT +
                                      Back.BLUE + "Dealer total:", total)
                                print(Fore.WHITE + Style.BRIGHT +
                                      Back.MAGENTA + "Player total:", playaplayedd)
                                if 21 - playaplayedd < 21 - total:
                                    print("You beat the computer, good job!!")
                                    restart()
                                elif playaplayedd == total:
                                    print("Draw!!!")
                                    restart()
                                elif playaplayedd == 21:
                                    print("You win!!")
                                    restart()
                                elif 21 - playaplayedd > 21 - total:
                                    print(
                                        "Bust!! Sorry the computer beat you this time!")
                                    restart()
                                    # elif playaplaya > 21:
                                    #     print("You lose!!")


hitme()

if 21 - playtotal < 21 - total:
    print("You beat the computer, good job!!")
