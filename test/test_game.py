from unittest import TestCase
from src.game import Game
from src.errors import DuplicatedPlayerError, GameHasAlreadyBeenWonError


class TestGame(TestCase):

    def test_duplicate_player_error(self):
        self.assertRaises(DuplicatedPlayerError, Game, "A", "A")

    def test_get_player1_name(self):
        game = Game("A", "B")
        self.assertEqual("A", game.get_player1_name())

    def test_get_player2_name(self):
        game = Game("A", "B")
        self.assertEqual("B", game.get_player2_name())

    def test_game_status_at_beginning(self):
        game = Game("A", "B")
        self.assertEqual("A love - B love", game.get_game_status())

    def test_first_player_wins(self):
        game = Game("A", "B")
        game.increment_player_score("A")
        game.increment_player_score("A")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("B")
        game.increment_player_score("A")
        self.assertEqual("A wins", game.get_game_status())

    def test_second_player_wins(self):
        game = Game("B", "A")
        game.increment_player_score("A")
        game.increment_player_score("A")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("B")
        game.increment_player_score("A")
        self.assertEqual("A wins", game.get_game_status())

    def test_15_to_40(self):
        game = Game("A", "B")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("B")
        game.increment_player_score("B")
        self.assertEqual("A fifteen - B forty", game.get_game_status())

    def test_15_to_30(self):
        game = Game("A", "B")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("B")
        self.assertEqual("A fifteen - B thirty", game.get_game_status())

    def test_15_to_15(self):
        game = Game("A", "B")
        game.increment_player_score("A")
        game.increment_player_score("B")
        self.assertEqual("A fifteen - B fifteen", game.get_game_status())

    def test_40_to_15(self):
        game = Game("A", "B")
        game.increment_player_score("A")
        game.increment_player_score("A")
        game.increment_player_score("A")
        game.increment_player_score("B")
        self.assertEqual("A forty - B fifteen", game.get_game_status())

    def test_40_to_30(self):
        game = Game("A", "B")
        game.increment_player_score("A")
        game.increment_player_score("A")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("B")
        self.assertEqual("A forty - B thirty", game.get_game_status())

    def test_deuce_at_40_to_40(self):
        game = Game("A", "B")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("A")
        game.increment_player_score("B")
        self.assertEqual("Deuce", game.get_game_status())

    def test_game_is_deuce_at_three_points(self):
        game = Game("A", "B")
        game.increment_player_score("A")
        game.increment_player_score("A")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("B")
        game.increment_player_score("B")
        self.assertEqual("Deuce", game.get_game_status())

    def test_advantage_50_40(self):
        game = Game("A", "B")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("A")
        self.assertEqual("Advantage A", game.get_game_status())

    def test_advantage_40_50(self):
        game = Game("B", "A")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("A")
        self.assertEqual("Advantage A", game.get_game_status())

    def test_deuce_after_advantage_50_50(self):
        game = Game("A", "B")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("A")
        game.increment_player_score("B")
        game.increment_player_score("A")
        game.increment_player_score("B")
        self.assertEqual("Deuce", game.get_game_status())

    def test_game_has_already_been_won_40_0(self):
        game = Game("A", "B")
        game.increment_player_score("A")
        game.increment_player_score("A")
        game.increment_player_score("A")
        game.increment_player_score("A")
        self.assertRaises(GameHasAlreadyBeenWonError, game.increment_player_score, "B")

    def test_game_has_already_been_won_0_40(self):
        game = Game("B", "A")
        game.increment_player_score("A")
        game.increment_player_score("A")
        game.increment_player_score("A")
        game.increment_player_score("A")
        self.assertRaises(GameHasAlreadyBeenWonError, game.increment_player_score, "B")



