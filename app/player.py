class Player:
    """
    The class responsible for creating player
    """
    _player_id = int
    _player_name = str

    def __init__(self, player_id:int, player_name:str) -> None:
        """
        Initialize the player object with ID and name
        parameter: player_id - The id of the player
        parameter: player_name -  The name of the player
        """
        self._player_name = player_name
        self._player_id = player_id

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

    def __str__(self) -> str:
        """
        String representation of the player
        return: uid and name - Player's unique id and name
        """
        return f'{self.uid} {self.name}.'
