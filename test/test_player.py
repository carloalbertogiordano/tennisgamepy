from unittest import TestCase
from src.player import Player

class TestPlayer(TestCase):

    def test_get_name(self):
        #Arrange
        player1 = Player("Sinner", 0)
        #Act
        name = player1.get_name()
        #Assert
        self.assertEqual("Sinner", name)

    def test_set_name(self):
        player = Player("AAAAAA", 0)

        player.set_name("Sinner")
        name = player.get_name()

        self.assertEqual("Sinner", name)

    def test_get_score(self):
        player1 = Player("Sinner", 2)
        score = player1.get_score()
        self.assertEqual(2, score)

    def test_set_score(self):
        player = Player("Sinner", 4)
        player.set_score(0)
        self.assertEqual(0, player.get_score())

    def test_increment_score(self):
        player = Player("Sinner", 0)
        results = [player.get_score()]

        for i in range(4):
            player.increment_score()
            results.append(player.get_score())

        self.assertListEqual([0, 1, 2, 3, 4], results)

    #Equivalent class testing tecnique
    #Classes are Valid values (0, 1, 2, 3) and invalid values ex:(-1, 4) but we uso only 4 for now
    def test_get_score_as_string_None(self):
        player = Player("Sinner", 4)
        self.assertEqual(None, player.get_score_as_string())

    def test_get_score_as_string_valid(self):
        player = Player("Sinner", 0)
        results = [player.get_score_as_string()]
        for i in range(1, 4):
            player = Player("Sinner", i)
            results.append(player.get_score_as_string())
        self.assertListEqual(["love", "fifteen", "thirty", "forty"], results)

    def test_there_is_tie(self):
        player1 = Player("A", 2)
        player2 = Player("B", 2)
        self.assertTrue(player1.is_tied_with(player2))

    def test_there_is_not_tie(self):
        player1 = Player("A", 2)
        player2 = Player("B", 3)
        self.assertFalse(player1.is_tied_with(player2))

    def test_has_at_least_forty_points(self):
        player = Player("A", 3)
        self.assertTrue(player.has_at_least_forty_points())

    def test_has_not_at_least_forty_points(self):
        player = Player("A", 2)
        self.assertFalse(player.has_at_least_forty_points())
