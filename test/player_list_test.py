import unittest
from player_list import PlayerList


class TestPlayerList(unittest.TestCase):
    def test_append_at_beginning_when_list_is_empty(self):
        a = PlayerList()
        self.assertEqual(a.is_empty(), True)
        a.append_at_beginning(1, "John")
        self.assertEqual(a.head.player.name, "John")
        self.assertEqual(a.is_empty(), False)

    def test_append_at_beginning_when_list_is_not_empty(self):
        a = PlayerList()
        a.append_at_beginning(1, "John")
        self.assertEqual(a.is_empty(), False)
        a.append_at_beginning(2, "Mary")
        self.assertEqual(a.tail.player.name, "John")
        self.assertEqual(a.head.player.name, "Mary")
