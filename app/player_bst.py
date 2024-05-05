from player import Player
from player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = value

    def insert(self, player: Player):
        if not isinstance(player, Player):
            raise ValueError("Enter a valid Player")

        if self.root is None:
            self.root = PlayerBNode(player)
            return

        current_node = self.root
        while current_node:
            if player.name < current_node.player.name:
                if current_node.left is None:
                    current_node.left = PlayerBNode(player)
                    return
                else:
                    current_node = current_node.left
            elif player.name > current_node.player.name:
                if current_node.right is None:
                    current_node.right = PlayerBNode(player)
                    return
                else:
                    current_node = current_node.right
            else:
                # If a node with the same key exists, update its value
                current_node.player = player
                return

    def search(self, name):
        if self.root is None:
            return None

        current_node = self.root
        while current_node is not None:
            if current_node.player.name == name:
                return current_node.player
            elif name < current_node.player.name:
                current_node = current_node.left
            else:
                current_node = current_node.right

    def sort_by_me(self, current_node):
        if current_node is None:
            return []
        left_list = self.sort_by_me(current_node.left)
        right_list = self.sort_by_me(current_node.right)
        sorted_list = left_list + [current_node.player] + right_list
        return sorted_list

    def insert_balanced(self, sorted_list):
        if not sorted_list:
            return None

        mid = len(sorted_list) // 2
        root = PlayerBNode(sorted_list[mid])
        root.left = self.insert_balanced(sorted_list[:mid])
        root.right = self.insert_balanced(sorted_list[mid + 1:])
        return root


