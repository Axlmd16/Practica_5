from controls.tda.list.linked_list import Linked_List
from controls.tda.tree.node import Node


class TreeNumber:
    def __init__(self) -> None:
        self.__root = None
        self.__height = 0
        self.__num_nodes = 0
        self.__levels = Linked_List()
        self.__orders = Linked_List()

    @property
    def get_num_nodes(self):
        return self.__num_nodes

    @property
    def get_height(self):
        return self.__height

    @property
    def get_levels(self):
        return self.__levels

    def __calc_height(self, tree):
        if tree is None:
            return 0
        else:
            left_height = self.__calc_height(tree._left)
            right_height = self.__calc_height(tree._right)
            return max(left_height, right_height) + 1

    def __calc_levels(self, tree, level):
        if tree is not None:
            self.__levels.get(level).add(tree)
            self.__calc_levels(tree._left, level + 1)
            self.__calc_levels(tree._right, level + 1)

    def levels(self):
        self.__levels = Linked_List()
        self.__height = self.__calc_height(self.__root)
        for i in range(self.__height):
            self.__levels.add(Linked_List())

        self.__calc_levels(self.__root, 0)

    def insert(self, data):
        if self.__root is None:
            self.__root = Node(data)
            self.__num_nodes += 1
            self.levels()
            return True
        else:
            new = Node(data)
            current = self.__root
            father = None
            while True:
                father = current
                if data == current._data:
                    return False
                elif data < current._data:
                    current = current._left
                    if current is None:
                        new._father = father
                        father._left = new
                        self.__num_nodes += 1
                        self.levels()
                        return True
                else:
                    current = current._right
                    if current is None:
                        new._father = father
                        father._right = new
                        self.__num_nodes += 1
                        self.levels()
                        return True

    def __pre_order(self, tree):
        if tree is not None:
            self.__orders.add(tree)
            self.__pre_order(tree._left)
            self.__pre_order(tree._right)

    def pre_order(self):
        self.__orders = Linked_List()
        self.__pre_order(self.__root)
        return self.__orders

    def __in_order(self, tree):
        if tree is not None:
            self.__in_order(tree._left)
            self.__orders.add(tree)
            self.__in_order(tree._right)

    def in_order(self):
        self.__orders = Linked_List()
        self.__in_order(self.__root)
        return self.__orders

    def __post_order(self, tree):
        if tree is not None:
            self.__post_order(tree._left)
            self.__post_order(tree._right)
            self.__orders.add(tree)

    def post_order(self):
        self.__orders = Linked_List()
        self.__post_order(self.__root)
        return self.__orders

    # def print_tree_levels(self):
    #     if not self.__root:
    #         return "Tree is empty"

    #     self.levels()

    #     tree_str = ""
    #     for i in range(self.__height):
    #         current_level = self.__levels.get(i)
    #         level_nodes = []
    #         current_node = current_level._head
    #         while current_node:
    #             node = current_node._data
    #             if node is not None:
    #                 level_nodes.append(str(node._data))
    #             else:
    #                 level_nodes.append("None")
    #             current_node = current_node._next
    #         tree_str += (
    #             "Level " + str(i) + ":\t" * (i + 1) + "\t".join(level_nodes) + "\n"
    #         )
    #     return tree_str

    # def __str__(self) -> str:
    #     return self.print_tree_levels()

    def print_tree_levels(self):
        if not self.__root:
            return "Tree is empty"

        self.levels()

        tree_str = ""
        for i in range(self.__height):
            current_level = self.__levels.get(i)
            level_nodes = []
            current_node = current_level._head
            while current_node:
                node = current_node._data
                if node is not None:
                    level_nodes.append(str(node._data))
                else:
                    level_nodes.append("None")
                current_node = current_node._next
            tree_str += f"Level {i}: " + "\t".join(level_nodes) + "\n"
        return tree_str

    def __str__(self) -> str:
        return self.print_tree_levels()
