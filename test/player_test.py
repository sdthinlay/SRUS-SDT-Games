import unittest
from player import Player


class PlayerTest(unittest.TestCase):
    def test_uid(self):
        my_player = Player(1, "sdt")
        self.assertEqual(1, my_player.uid)

    def test_name(self):
        my_player = Player(1, "sdt")
        self.assertEqual("sdt", my_player.name)


if __name__ == '__main__':
    unittest.main()
