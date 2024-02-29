from player_node import PlayerNode
from player import Player


class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None

    def append_at_beginning(self, player: Player):
        new_player = PlayerNode(player)
        if self.is_empty():
            self._head = new_player
            self._tail = new_player
        else:
            previous_player = self._head
            self._head = new_player
            self._head.next = previous_player
            previous_player.prev = self._head

    def append_at_tail(self, player: Player):
        new_player = PlayerNode(player)
        if self.is_empty():
            self._head = new_player
            self._tail = new_player
        else:
            self._tail.next = new_player
            new_player.prev = self._tail
            self._tail = new_player

    def pop_at_beginning(self):
        if self.is_empty():
            raise ValueError("Player list is empty")
        else:
            current_player = self._head
            self._head = current_player.next
            if self._head is not None:
                self._head.prev = None
            else:
                self._tail = None

    def pop_at_tail(self):
        if self.is_empty():
            raise ValueError("Player list is empty")
        else:
            current_player = self._tail
            self._tail = current_player.prev
            if self._tail is not None:
                self._tail.next = None
            else:
                self._head = None

    def pop_by_key(self, key):
        if self.is_empty():
            raise ValueError("Player list is empty")
        else:
            current_player = self._head
            while current_player is not None:
                if current_player.key == key:
                    if current_player.prev is not None:
                        current_player.prev.next = current_player.next
                    else:
                        self._head = current_player.next
                        if current_player.next is not None:
                            current_player.next.prev = None
                    return "Player removed successfully"
                current_player = current_player.next
            raise ValueError("No player found")

    def is_empty(self):
        return self._head is None


