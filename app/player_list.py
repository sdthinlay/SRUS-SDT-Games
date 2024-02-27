from player_node import PlayerNode
from player import Player


class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, node):
        self._head = node

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, node):
        self._tail = node

    def append_at_beginning(self, player_id, player_name):
        new_player = PlayerNode(Player(player_id, player_name))
        if self.is_empty():
            self.head = new_player
            self.tail = new_player
        else:
            previous_player = self.head
            self.head = new_player
            self.head.next = previous_player
            previous_player.prev = self.head

    def is_empty(self):
        return self.head is None
