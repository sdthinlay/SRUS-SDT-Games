class Player:
    def __init__(self, player_id, player_name):
        self._player_name = player_name
        self._player_id = player_id

    @property
    def uid(self):
        return self._player_id

    @property
    def name(self):
        return self._player_name

    def __str__(self):
        return f'{self.uid} {self.name}.'


