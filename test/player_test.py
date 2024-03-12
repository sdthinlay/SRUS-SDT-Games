import unittest

import player
from player import Player


class PlayerTest(unittest.TestCase):
    def test_uid(self):
        my_player = Player(1, "sdt")
        self.assertEqual(1, my_player.uid)

    def test_name(self):
        my_player = Player(1, "sdt")
        self.assertEqual("sdt", my_player.name)

    def test_add_password(self):
        my_player = Player(1, "sdt")
        my_player.add_password("Password1")
        self.assertEqual(my_player.check_password("Password1"), True)

