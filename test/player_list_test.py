import unittest
from player_list import PlayerList


class TestPlayerList(unittest.TestCase):
    def setUp(self):
        self.playerList = PlayerList()

    def test_append_at_beginning_when_list_is_empty(self):
        self.assertEqual(self.playerList.is_empty(), True)
        self.playerList.append_at_beginning(1, "John")
        self.assertEqual(self.playerList._head.player.name, "John")
        self.assertEqual(self.playerList._tail.player.name, "John")
        self.assertEqual(self.playerList.is_empty(), False)

    def test_append_at_beginning_when_list_is_not_empty(self):
        self.playerList.append_at_beginning(1, "sangay")
        self.playerList.append_at_beginning(2, "dema")
        self.playerList.append_at_beginning(3, "thinley")
        self.assertEqual(self.playerList._head.player.name, "thinley")
