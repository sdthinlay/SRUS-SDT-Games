
class PlayerNode:
    """
    The class responsible for creating player node
    """
    def __init__(self, player):
        """
        Initializes the player node
        parameter: player - The player object in the node
        """
        self._player = player
        self._next = None
        self._prev = None

    @property
    def next(self):
        """
        The next player node
        return: next player node
        """
        return self._next

    @next.setter
    def next(self, node):
        """
        Sets the next player
        parameter: node - next player node
        """
        self._next = node

    @property
    def prev(self):
        """
        The previous player node
        return: previous player node
        """
        return self._prev

    @prev.setter
    def prev(self, node):
        """
        Sets the previous player
        parameter node - previous player node
        """
        self._prev = node

    @property
    def player(self):
        """
        The player object in the node
        return: player - player object
        """
        return self._player

    @property
    def key(self):
        """
        The unique key of the player in the node
        return: player uid - unique key of the player in the node
        """
        return self.player.uid

    def __str__(self):
        """
        String representation of the player node
        return: - player name and node
        """
        return f"{self.player.name} {self.player.uid}"
