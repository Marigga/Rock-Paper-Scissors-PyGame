
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def beats(one, two):

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class Human(Player):
    def move(self):
        your_move = ""

        while True:
            your_move = input("Enter your move: rock / paper / scissors \n")
            if your_move.lower() == 'r' or your_move.lower() == 'rock':
                your_move = 'rock'
                break
            elif your_move.lower() == 'p' or your_move.lower() == 'paper':
                your_move = 'paper'
                break
            elif your_move.lower() == 's' or your_move.lower() == 'scissors':
                your_move = 'scissors'
                break
            else:
                print("Invalid input. Try again!")
        return your_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        self.previous_move2 = random.choice(moves)

    def move(self):
        return self.previous_move2

    def learn(self, my_move, their_move):
        self.previous_move2 = their_move


class CyclePlayer(Player):

    def __init__(self):
        self.previous_move1 = random.choice(moves)

    def move(self):
        moves_available = moves.index(self.previous_move1)
        if moves_available == 2:
            return moves[0]
        else:
            return moves[moves_available + 1]

    def learn(self, my_move, their_move):
        self.previous_move1 = my_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.player_one = 0
        self.player_two = 0
        self.tiegame = 0

    def opponent_player(self):
        print("Select your opponent:\n"
              " Primary - 'rock' is played by opponent every round\n"
              " Random - opponent plays a random choice\n"
              " Cycle  - remembers what was played and cycles through moves\n"
              " Mirror - opponent mimics yours move next round")
        while True:
            opponent = (input("Choose your opponent: "))
            if opponent.lower() == "p" or opponent.lower() == "primary":
                self.p2 = Player()
                break
            elif opponent.lower() == "r" or opponent.lower() == "random":
                self.p2 == RandomPlayer()
                break
            elif opponent.lower() == "c" or opponent.lower() == "cycle":
                self.p2 = CyclePlayer()
                break
            elif opponent.lower() == "m" or opponent.lower() == "mirror":
                self.p2 = ReflectPlayer()
                break
            else:
                print("That is not an option. Try again. ")

    def play_rules(self):
        print("Rock, Paper, Scissors\n"
              "Rules:\n"
              "  Scissors cuts Paper\n"
              "  Paper covers Rock\n"
              "  Rock crushes Scissors\n")

    def game_round(self):
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
        print("Game over!")
        self.results()

    def outcome(self, first_play, second_play):
        if beats(first_play, second_play):
            self.player_one += 1
            print("Move '{0}' beats '{1}'.You won "
                  "this round!".format(first_play, second_play))
            print("Score:")
            print("You: {0}".format(self.player_one))
            print("Opponent: {0}".format(self.player_two))
            print("Ties: {0}".format(self.tiegame))

        elif beats(second_play, first_play):
            self.player_two += 1
            print("Move '{0}' beats '{1}'. Your opponent "
                  "won this round!".format(second_play, first_play))
            print("Score:")
            print("You: {0}".format(self.player_one))
            print("Opponent: {0}".format(self.player_two))
            print("Ties:{0}".format(self.tiegame))
        else:
            self.tiegame += 1
            print("No winners, it's a tie this round.")
            print("Score:")
            print("You:{0}".format(self.player_one))
            print("Opponent:{0}".format(self.player_two))
            print("Ties:{0}".format(self.tiegame))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print("You: {0}  Opponent: {1}".format(move1, move2))
        self.outcome(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def results(self):
        print("Total score:")
        print("You WON: {0}".format(self.player_one))
        print("Opponent WON: {0}".format(self.player_two))
        print("Ties: {0}".format(self.tiegame))
        if self.player_one > self.player_two:
            print("You WON!")
        elif self.player_one < self.player_two:
            print("Your opponent WON!")
        else:
            print("It's a tie!")
        exit(0)

    def start_game(self):
        self.play_rules()
        self.opponent_player()
        self.game_round()
        self.play_round()
        self.outcome()
        self.results()


if __name__ == '__main__':
    game = Game(Human(), RandomPlayer())
    game.start_game()
