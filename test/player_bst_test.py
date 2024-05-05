import unittest
from player_bst import PlayerBST
from player_bnode import PlayerBNode
from player import Player


class TestPlayerBST(unittest.TestCase):
    def test_insert(self):
        bst = PlayerBST()
        # player_list = [Player(6, "Trish", 67),
        #                Player(3, "Josh", 89),
        #                Player(10, "Nita", 54),
        #                Player(67, "Yanday", 56),

        bst.insert(Player(6, "Trish", 67))
        bst.insert(Player(3, "Nita", 78))
        bst.insert(Player(5, "Yanday", 54))

        self.assertIs(bst.root.player.name, "Trish")
        self.assertIs(bst.root.right.player.name, "Yanday")
        self.assertIs(bst.root.left.player.name, "Nita")

    def test_search(self):
        bst = PlayerBST()
        bst.insert(Player(6, "Trish", 67))
        bst.insert(Player(3, "Nita", 78))
        bst.insert(Player(5, "Yanday", 54))
        player_name_to_search = "Nita"
        result_node = bst.search(player_name_to_search)
        self.assertTrue(result_node, True)
