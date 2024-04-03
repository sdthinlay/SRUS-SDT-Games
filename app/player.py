from __future__ import annotations
from argon2 import PasswordHasher
from typing import Any


class Player:
    """
    The class responsible for creating player
    """
    _player_id = int
    _player_name = str
    _score = int

    def __init__(self, player_id: int, player_name: str, score: int) -> None:
        """
        Initialize the player object with ID and name
        parameter: player_id - The id of the player
        parameter: player_name -  The name of the player
        """
        self._player_name = player_name
        self._player_id = player_id
        self._player_password = None
        self._score = score

    @property
    def player_score(self) -> int:
        return self._score

    @player_score.setter
    def player_score(self, score: int) -> None:
        self._score = score

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Player):
            return self.player_score == other.player_score

        return False

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Player):
            return self.player_score >= other.player_score

        return False

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Player):
            return self.player_score <= other.player_score

        return False

    @staticmethod
    def sort_by_quicksort(player_list: list) -> list:
        if len(player_list) == 0:
            return player_list
        pivot = player_list[0]
        left = []
        right = []
        for i in player_list[1:]:
            if i <= pivot:
                left.append(i)
            elif i >= pivot:
                right.append(i)
        return Player.sort_by_quicksort(right) + [pivot] + Player.sort_by_quicksort(left)

    @property
    def uid(self) -> int:
        """
        Gets the unique id of the player
        return: player_id - Player's unique id
        """
        return self._player_id

    @property
    def name(self) -> str:
        """
        Gets the name of the player
        return: player_name - Player's name
        """
        return self._player_name

    def add_password(self, password: str) -> None:
        """
        Add password to the player
        :parameter password: The password to be added
        """
        password_hasher = PasswordHasher()
        hashed_password = password_hasher.hash(password)
        self._player_password = hashed_password

    def verify_password(self, password: str) -> bool:
        """
        Verifies the password against the player's password
        :parameter password:  The password to be verified
        """
        if self._player_password is None:
            return False
        password_hasher = PasswordHasher()
        try:
            password_hasher.verify(self._player_password, password)
            return True
        except Exception as e:
            e = "Wrong password"
            print(e)
            return False

    def __str__(self) -> str:
        """
        String representation of the player
        return: uid and name - Player's unique id and name
        """
        return f'{self.uid} {self.name}.'



