from player_node import PlayerNode
from player import Player


class PlayerList:
    def __init__(self):
        self.head = None
        self.tail = None

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

    