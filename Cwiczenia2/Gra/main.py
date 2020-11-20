import random

from easyAI import TwoPlayersGame, Human_Player, AI_Player, Negamax


class GameOfEye(TwoPlayersGame):
    """Authors: Tomasz Mnich, Wojciech Szypelt
    Rules: https://pl.wikipedia.org/wiki/Oczko_(gra_karciana) without exception "Persian eye"
    To play this game you need Python 3.8 https://www.python.org/downloads/ and easyAI https://pypi.org/project/easyAI/ """

    def __init__(self, players):
        """
        This function prepares players and card decks for play

        Parameters:
        human_player (int): Number describe when human have they turn. Value from easyAI documentation
        computer_player (int): Number describe when human have they turn. Value from easyAI documentation
        players (object): Players who participate in the game
        human_pass(boolean): Value that indicates that a player has stopped the game. Default to False, if you change the value to True, the game will end
        computer_pass(boolean): Value that indicates that the game has been interrupted by the computer. Default to False, if you change the value to True, the game will end
        nplayer(object): the variable takes the form of the value of the player who starts
        deck(list): A collection of cards in the form of their point value in the game Oczko.

        :rtype: object
        :param players:
        """
        print("Witaj w grze oczko! zasady gry: https://pl.wikipedia.org/wiki/Oczko_(gra_karciana)'brak wyjatku perskie oczko' ")
        print("Dobierz karte(up) albo spasuj(pass). Powodzenia! ")

        self.human_player = 1
        self.human_points = 0
        self.computer_player = 2
        self.computer_points = 0
        self.players = players
        self.human_pass = False
        self.computer_pass = False
        self.human_winner = False

        self.nplayer = self.human_player  # player 1 starts
        self.deck = [2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7,
                     7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11]

    def possible_moves(self):
        """Choice of player and computer about whether they want to draw a card or already fold

        Returns:
        list:Returning value
        """
        return ["up", "pass"]

    def make_move(self, move):
        """The function is responsible for handling the player's decisions

        Parameters:
        move (String): One of the allowable movements defined in the method "possible_moves"

        Returns:
        int:Returning value
        """

        if self.human_pass == True and self.computer_points > self.human_points:
            self.computer_pass = True
        elif move == "up":
            card = random.choice(self.deck)
            self.deck.remove(card)
            if self.nopponent == self.computer_player:
                self.human_points += card
            elif self.nopponent == self.human_player:
                self.computer_points += card
        elif move == "pass":
            if self.nopponent == self.computer_player:
                self.human_points += 0
                self.human_pass = True
            elif self.nopponent == self.human_player:
                self.computer_points += 0
                self.computer_pass = True
        if self.human_player == self.nopponent and self.human_pass == True:  # exchange from player to computer if we have already entered a 'pas'
            TwoPlayersGame.switch_player(self)

    def win(self):
        """The function that defines when the game ends
        :return:
        """
        if self.human_points == 21:
            self.human_winner = True
            return True
        if self.computer_points > 21:
            self.human_winner = True
            return True
        if self.computer_points == 21:
            self.human_winner = False
            return True
        if self.human_points > 21:
            self.human_winner = False
            return True
        if self.computer_pass == True and self.human_pass == True:
            return True

        return False

    def is_over(self):
        """
        :return:
        """
        return self.win()

    def show(self):
        """
        :return:
        """
        print("%d score human" % self.human_points)
        print("%d score  computer" % self.computer_points)

    def scoring(self):
        """
        :return:
        """
        return 100 if game.win() else 0  # For the AI


# Start a match (and store the history of moves when it ends)
ai = Negamax(13)  # The AI will think 13 moves in advance

while True:

    game = GameOfEye([Human_Player(), AI_Player(ai)])
    history = game.play()

    if game.human_winner == True:
        print("Koniec gry! Zwyciezyles! Brawo!")
    elif game.human_winner == False:
        print("Koniec gry! Niestety komputer wygral")
    print("Jesli chcesz zakonczyc wpisz 'N' ")
    if input() == 'N':
        break

exit()
