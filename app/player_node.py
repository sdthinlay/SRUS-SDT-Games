from player import Player


class PlayerNode:
    def __init__(self, player):
        self._player = player
        self._next = None
        self._prev = None

    @property
    def player(self):
        return self._player

    @property
    def next(self):
        return self._next

    @property
    def prev(self):
        return self._prev

    @property
    def key(self):
        return self.player.uid

    def __str__(self):
        return f"{self.player.uid},{self.player.name}"
