import unittest
from player import Player


class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.player1 = Player(1, "John", 45)
        self.player2 = Player(2, "Jane", 53)
        self.player3 = Player(3, "Mary", 72)

    def test_uid(self):
        self.assertIs(1, self.player1.uid)

    def test_name(self):
        self.assertIs("John", self.player1.name)

    def test_add_password(self):
        self.player1.add_password("Password1")
        self.assertIs(self.player1.verify_password("Password1"), True)

    def test_verify_password_if_correct(self):
        self.player1.add_password("Password1")
        self.assertIs(self.player1.verify_password("Password1"), True)

    def test_verify_incorrect_password(self):
        self.player1.add_password("Password1")
        self.assertIsNot(self.player1.verify_password("Password2"), True)

    def test_verify_password_if_empty(self):
        self.player1.add_password("Password1")
        self.assertIsNot(self.player1.verify_password(""), True)

    def test_equal_operator(self):
        self.assertIs(self.player1.__eq__(self.player1), True)

    def test_greater_than_or_equal_to_operator(self):
        self.assertIs(self.player2.__ge__(self.player1), True)

    def test_less_than_or_equal_to_operator(self):
        self.assertIs(self.player1.__le__(self.player1), True)

    def test_sort_score_by_quicksort(self):
        list_player = [Player(1, "Mary", 100),
                       Player(2, "Yang", 56),
                       Player(3, "Sangay", 97),
                       Player(4, "Abdul", 45)]

        sorted_players = Player.sort_by_quicksort(list_player)
        sorted_scores = [player.player_score for player in sorted_players]
        expected_players = [100, 97, 56, 45]
        self.assertEqual(expected_players, sorted_scores)

