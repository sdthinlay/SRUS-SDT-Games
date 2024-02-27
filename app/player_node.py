from player import Player


class PlayerNode:
    def __init__(self, player):
        self._player = player
        self.next = None
        self.prev = None

    @property
    def player(self):
        return self._player

    @property
    def key(self):
        return self.player.uid

    def __str__(self):
        return f"{self.player.name} {self.player.uid}"
