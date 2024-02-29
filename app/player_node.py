from player import Player


class PlayerNode:
    def __init__(self, player):
        self._player = player
        self._next = None
        self._prev = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, node):
        self._prev = node

    @property
    def player(self):
        return self._player

    @property
    def key(self):
        return self.player.uid

    def __str__(self):
        return f"{self.player.name} {self.player.uid}"
