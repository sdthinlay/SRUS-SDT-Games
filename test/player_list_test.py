import unittest
from player_list import PlayerList
from player import Player
from player_node import PlayerNode


class TestPlayerList(unittest.TestCase):
    def setUp(self):
        self.playerList = PlayerList()
        self.player1 = PlayerNode(Player(1, "John", 45))
        self.player2 = PlayerNode(Player(2, "Jane", 53))
        self.player3 = PlayerNode(Player(3, "Mary", 72))

    def test_append_at_beginning_when_list_is_empty(self):
        self.assertEqual(self.playerList.is_empty(), True)
        self.playerList.append_at_beginning(self.player1)
        self.assertIs(self.playerList._head.player.name, self.player1.player.name)
        self.assertIs(self.playerList._tail.player.name, self.player1.player.name)
        self.assertIs(self.playerList.is_empty(), False)

    def test_append_at_beginning_when_list_is_not_empty(self):
        self.playerList.append_at_beginning(self.player1)
        self.playerList.append_at_beginning(self.player2)
        self.assertIs(self.playerList._head, self.player2)

    def test_append_at_tail_when_list_is_empty(self):
        self.assertIs(self.playerList.is_empty(), True)
        self.playerList.append_at_tail(self.player1)
        self.assertIs(self.playerList._tail, self.player1)
        self.assertIs(self.playerList.is_empty(), False)

    def test_append_at_tail_when_list_is_not_empty(self):
        self.playerList.append_at_tail(self.player1)
        self.playerList.append_at_tail(self.player2)
        self.assertIs(self.playerList._tail, self.player2)

    def test_pop_at_beginning_when_list_is_empty(self):
        self.assertIs(self.playerList.is_empty(), True)
        with self.assertRaises(ValueError):
            self.playerList.pop_at_beginning()

    def test_pop_at_beginning(self):
        self.playerList.append_at_tail(self.player1)
        self.playerList.append_at_tail(self.player2)
        self.playerList.append_at_tail(self.player3)
        self.playerList.pop_at_beginning()
        self.assertIs(self.playerList._head, self.player2)

    def test_pop_at_tail_when_list_is_empty(self):
        self.assertIs(self.playerList.is_empty(), True)
        with self.assertRaises(ValueError):
            self.playerList.pop_at_tail()

    def test_pop_at_tail(self):
        self.playerList.append_at_tail(self.player1)
        self.playerList.append_at_tail(self.player2)
        self.playerList.append_at_tail(self.player3)
        self.playerList.pop_at_tail()
        self.assertIs(self.playerList._tail, self.player2)

    def test_pop_by_key(self):
        self.playerList.append_at_tail(self.player1)
        self.playerList.append_at_tail(self.player2)
        self.playerList.append_at_tail(self.player3)
        self.playerList.pop_by_key(1)
        self.assertIs(self.playerList._tail, self.player3)
