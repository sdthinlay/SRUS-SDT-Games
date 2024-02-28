from player_node import PlayerNode
from player import Player


class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None

    def append_at_beginning(self, player_id, player_name):
        new_player = PlayerNode(Player(player_id, player_name))
        if self.is_empty():
            self._head = new_player
            self._tail = new_player
        else:
            previous_player = self._head
            self._head = new_player
            self._head.next = previous_player
            previous_player.prev = self._head

    def append_at_tail(self, player_id, player_name):
        new_player = PlayerNode(Player(player_id, player_name))
        if self.is_empty():
            self._head = new_player
            self._tail = new_player
        else:
            self._tail.next = new_player
            new_player.prev = self._tail
            self._tail = new_player

    def is_empty(self):
        return self._head is None



