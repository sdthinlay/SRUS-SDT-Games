import unittest
from player_list import PlayerList
from player import Player


class TestPlayerList(unittest.TestCase):
    def setUp(self):
        self.playerList = PlayerList()
        self.player1 = Player(1, "John")
        self.player2 = Player(2, "Jane")
        self.player3 = Player(3, "Mary")

    def test_append_at_beginning_when_list_is_empty(self):
        self.assertEqual(self.playerList.is_empty(), True)
        self.playerList.append_at_beginning(self.player1)
        self.assertIs(self.playerList._head.player.name, self.player1.name)
        self.assertIs(self.playerList._tail.player.name, self.player1.name)
        self.assertEqual(self.playerList.is_empty(), False)

    def test_append_at_beginning_when_list_is_not_empty(self):
        self.playerList.append_at_beginning(self.player1)
        self.playerList.append_at_beginning(self.player2)
        self.assertIs(self.playerList._head.player, self.player2)

    def test_append_at_tail_when_list_is_empty(self):
        self.assertEqual(self.playerList.is_empty(), True)
        self.playerList.append_at_tail(self.player1)
        self.assertIs(self.playerList._tail.player, self.player1)
        self.assertEqual(self.playerList.is_empty(), False)

    def test_append_at_tail_when_list_is_not_empty(self):
        self.playerList.append_at_tail(self.player1)
        self.playerList.append_at_tail(self.player2)
        self.assertIs(self.playerList._tail.player, self.player2)

    def test_pop_at_beginning_when_list_is_empty(self):
        self.assertEqual(self.playerList.is_empty(), True)
        with self.assertRaises(ValueError):
            self.playerList.pop_at_beginning()

    def test_pop_at_beginning(self):
        self.playerList.append_at_tail(self.player1)
        self.playerList.append_at_tail(self.player2)
        self.playerList.append_at_tail(self.player3)
        self.playerList.pop_at_beginning()
        self.assertIs(self.playerList._head.player, self.player2)

    def test_pop_at_tail_when_list_is_empty(self):
        self.assertEqual(self.playerList.is_empty(), True)
        with self.assertRaises(ValueError):
            self.playerList.pop_at_tail()

    def test_pop_at_tail(self):
        self.playerList.append_at_tail(self.player1)
        self.playerList.append_at_tail(self.player2)
        self.playerList.append_at_tail(self.player3)
        self.playerList.pop_at_tail()
        self.assertIs(self.playerList._tail.player, self.player2)

    def test_pop_by_key(self):
        self.playerList.append_at_tail(self.player1)
        self.playerList.append_at_tail(self.player2)
        self.playerList.append_at_tail(self.player3)
        self.playerList.pop_by_key(1)
        self.assertIs(self.playerList._head.player, self.player2)
