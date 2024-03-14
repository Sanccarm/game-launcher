import unittest
from unittest.mock import patch
import game


class TestGameSetup(unittest.TestCase):

    """""
    -Test cases assert players money to confirm that the program is working as intended
    -due to the randomness of the game some tests just make sure the result is withing the range of correct values
    -tests 6 and 9 run the program as normal in order to test the programs ability to quit and repeat
    """""

    @staticmethod
    def start_up_fix(game_num):
        game_num.deck.deck += game_num.dealer.hand
        for player in game_num.players:
            game_num.deck.deck += player.hands[0].hand

    @patch('builtins.input', side_effect=['0', 'a', '.5', '3', '100', '1', 'Bob',
                                          'Alex', 'John', '.5', '200', '.5', '70',
                                          '20', '30', 'y', 'a', '.5', '20',
                                          '5', 'y', '30', "n", 'sp', 'su', 'su', 'hi', 'hi', 'st', 'st'])
    def test_game_1_test(self, mock_input):  # mock_input is needed for the @patch to work
        game1 = game.Game()

        game1.game_startup()
        self.start_up_fix(game1)
        print(len(game1.deck.deck))
        self.assertEqual(len(game1.deck.deck), 52)
        game1.dealer.hand = [game.Card('Ace', 11, 'Spades'), game.Card('6', 6, 'Hearts')]
        game1.players[0].hands[0].hand = [game.Card('Ace', 11, 'Hearts'), game.Card('Ace', 11, 'Clubs')]
        game1.players[1].hands[0].hand = [game.Card('2', 2, 'Diamonds'), game.Card('2', 2, 'Hearts')]
        game1.players[2].hands[0].hand = [game.Card('10', 10, 'Spades'), game.Card('King', 10, 'Clubs')]

        game1.players_turn()
        game1.results(False)

        self.assertEqual(len(game1.players), 3)

        self.assertEqual(game1.players[0].money, 55.0)
        self.assertEqual(game1.players[1].money, 90.0)
        self.assertEqual(game1.players[2].money, 70.0)

    @patch('builtins.input', side_effect=['3', '100', '1', 'Bob', 'Alex', 'John', '100', '20', '30', 'y', '3',
                                          'y', '7000', '40', '2', 'n'])
    def test_game_2_test(self, mock_input):
        game1 = game.Game()

        game1.game_startup()
        self.start_up_fix(game1)
        game1.dealer.hand = [game.Card('Ace', 11, 'Spades'), game.Card('10', 10, 'Hearts')]
        game1.players[0].hands[0].hand = [game.Card('Ace', 11, 'Hearts'), game.Card('10', 10, 'Clubs')]
        game1.players[1].hands[0].hand = [game.Card('2', 2, 'Diamonds'), game.Card('2', 2, 'Hearts')]
        game1.players[2].hands[0].hand = [game.Card('7', 7, 'Spades'), game.Card('King', 10, 'Clubs')]
        game1.players_turn()
        game1.results(False)

        self.assertEqual(game1.players[0].money, 100.0)
        self.assertEqual(game1.players[1].money, 80.0)
        self.assertEqual(game1.players[2].money, 70.0)

    @patch('builtins.input', side_effect=['3', '100', '1', 'Bob', 'Alex', 'John', '10', '20',
                                          '30', 'bad input', 'sp', 'do', 'su', 'st',
                                          'st', 'hi', 'st', 'st', 'st'])
    def test_game_3_test(self, mock_input):
        game1 = game.Game()

        game1.game_startup()
        self.start_up_fix(game1)
        game1.dealer.hand = [game.Card('4', 4, 'Spades'), game.Card('10', 10, 'Hearts')]
        game1.players[0].hands[0].hand = [game.Card('Ace', 11, 'Hearts'), game.Card('10', 10, 'Clubs')]
        game1.players[1].hands[0].hand = [game.Card('2', 2, 'Diamonds'), game.Card('2', 2, 'Hearts')]
        game1.players[2].hands[0].hand = [game.Card('7', 7, 'Spades'), game.Card('2', 2, 'Clubs')]
        game1.players_turn()
        game1.results(False)

        self.assertEqual(game1.players[0].money, 105.0)  # First player has blackjack and wins 50%
        self.assertEqual(game1.players[1].money, 60)  # Second player will always lose both hands
        self.assertLessEqual(game1.players[2].money, 130)  # Thirds player will sometimes hit and win
        self.assertGreaterEqual(game1.players[2].money, 70)  # and sometimes lose

    @patch('builtins.input', side_effect=['3', '100', '1', 'Bob', 'Alex', 'John', '10', '20',
                                          '30', 'sp', 'do', 'su', 'st', 'st', 'hi', 'st'])
    def test_game_4_test(self, mock_input):
        game1 = game.Game()

        game1.game_startup()
        self.start_up_fix(game1)
        game1.dealer.hand = [game.Card('2', 2, 'Diamonds'), game.Card('2', 2, 'Hearts')]
        game1.players[0].hands[0].hand = [game.Card('Ace', 11, 'Hearts'), game.Card('4', 4, 'Clubs')]
        game1.players[1].hands[0].hand = [game.Card('2', 3, 'Diamonds'), game.Card('2', 3, 'Hearts')]
        game1.players[2].hands[0].hand = [game.Card('7', 7, 'Spades'), game.Card('7', 7, 'Clubs')]
        game1.players_turn()
        game1.results(False)

        self.assertEqual(game1.players[0].money, 120.0)
        self.assertEqual(game1.players[1].money, 90.0)
        self.assertEqual(game1.players[2].money, 130.0)

    @patch('builtins.input', side_effect=['3', '100', '1', 'Bob', 'Alex', 'John', '10', '20',
                                          '30', 'sp', 'st', 'st', 'do', 'hi', 'st'])
    def test_game_5_test(self, mock_input):
        game1 = game.Game()

        game1.game_startup()
        self.start_up_fix(game1)
        game1.dealer.hand = [game.Card('8', 8, 'Spades'), game.Card('7', 7, 'Hearts')]
        game1.players[0].hands[0].hand = [game.Card('3', 3, 'Hearts'), game.Card('4', 4, 'Clubs'),
                                          game.Card('7', 7, 'Diamonds')]
        game1.players[0].hands[0].first_draw = False
        game1.players[1].hands[0].hand = [game.Card('2', 2, 'Diamonds'), game.Card('2', 2, 'Hearts')]
        game1.players[2].hands[0].hand = [game.Card('7', 7, 'Spades'), game.Card('7', 7, 'Clubs')]
        game1.players_turn()
        game1.results(False)

        self.assertEqual(game1.players[0].money, 90.0)
        self.assertEqual(game1.players[1].money, 80.0)
        self.assertLessEqual(game1.players[2].money, 160)
        self.assertGreaterEqual(game1.players[2].money, 40)

    @patch('builtins.input', side_effect=['1', '100', '1', 'Bob', '10', 'st', 'st', 'q'])
    def test_game_6_test(self, mock_input):
        game1 = game.Game()
        game1.running_game()

        self.assertLessEqual(game1.players[0].money, 110)
        self.assertGreaterEqual(game1.players[0].money, 90)

    @patch('builtins.input', side_effect=['2', '100', '1', 'Bob', 'Alex', 'John', '10', '20',
                                          '30', 'sp', 'st', 'st', 'do', 'hi', 'st'])
    def test_game_7_test(self, mock_input):
        game1 = game.Game()
        game1.add_player(100)
        game1.players[0].money = 0
        game1.game_startup()
        self.start_up_fix(game1)
        game1.dealer.hand = [game.Card('8', 8, 'Spades'), game.Card('7', 7, 'Hearts')]
        game1.players[0].hands[0].hand = [game.Card('3', 3, 'Hearts'), game.Card('4', 4, 'Clubs')]
        game1.players[0].hands[0].first_draw = False
        game1.players[1].hands[0].hand = [game.Card('2', 2, 'Diamonds'), game.Card('2', 2, 'Hearts')]
        game1.players_turn()
        game1.results(False)

        self.assertEqual(game1.players[0].money, 90.0)
        self.assertEqual(game1.players[1].money, 80.0)

    @patch('builtins.input', side_effect=['1', '100', '1', 'Bob', '10', 'do'])
    def test_game_8_test(self, mock_input):
        game1 = game.Game()

        game1.game_startup()
        self.start_up_fix(game1)
        game1.dealer.hand = [game.Card('2', 2, 'Diamonds'), game.Card('2', 2, 'Hearts')]
        game1.players[0].hands[0].hand = [game.Card('Ace', 11, 'Hearts'), game.Card('4', 4, 'Clubs')]
        game1.players_turn()
        game1.results(False)

        self.assertEqual(game1.players[0].money, 120.0)

    @patch('builtins.input', side_effect=['1', '100', '1', 'Bob', '10', 'st', 'st', 'c', '10', 'st', 'st', 'q'])
    def test_game_9_test(self, mock_input):
        game1 = game.Game()
        game1.running_game()

        self.assertLessEqual(game1.players[0].money, 120)
        self.assertGreaterEqual(game1.players[0].money, 80)
