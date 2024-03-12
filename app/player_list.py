from __future__ import annotations
from player_node import PlayerNode
from player import Player


class PlayerList:
    """
    The class responsible for creating player list
    """
    _head = None
    _tail = None

    def __init__(self):
        """
        Initializes the player list
        """
        self._head = None
        self._tail = None

    def append_at_beginning(self, player: Player) -> None:
        """
        Adds a player to the beginning of the list
        parameter: player - the player added to the list
        """
        new_player = PlayerNode(player)
        if self.is_empty():
            self._head = new_player
            self._tail = new_player
        else:
            previous_player = self._head
            self._head = new_player
            self._head.next = previous_player
            previous_player.prev = self._head

    def append_at_tail(self, player: Player) -> None:
        """
        Adds a player to the end of the list
        parameter: player - the player added to the list
        """
        new_player = PlayerNode(player)
        if self.is_empty():
            self._head = new_player
            self._tail = new_player
        else:
            self._tail.next = new_player
            new_player.prev = self._tail
            self._tail = new_player

    def pop_at_beginning(self):
        """
        Removes the player from the beginning of the list
        """
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
        """
        Removes the player from the end of the list
        """
        if self.is_empty():
            raise ValueError("Player list is empty")
        else:
            current_player = self._tail
            self._tail = current_player.prev
            if self._tail is not None:
                self._tail.next = None
            else:
                self._head = None

    key = int

    def pop_by_key(self, key: int):
        """
        Removes the player by its unique key from the list
        parameter: key - The unique key of each player in the list
        """
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
                    print("Player removed successfully")
                current_player = current_player.next
            raise ValueError("No player found")

    def display_list(self, forward: bool = True) -> None:
        """
        Displays the entire players on the list
        parameter: forward: True to display the list in forward direction and False to display the list in reverse direction
        """
        if forward:
            current_player = self._head
            while current_player is not None:
                print(current_player, end="|")
                current_player = current_player.next
        else:
            current_player = self._tail
            while current_player is not None:
                print(current_player, end="|")
                current_player = current_player.prev

    def is_empty(self) -> bool:
        """
        Checks if the player list is empty or not
        return: True if the player list is empty and False if the player list is not empty
        """
        return self._head is None
