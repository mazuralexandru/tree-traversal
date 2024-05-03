from node import Node

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    """ Tree class for binary tree """

    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    def getRoot(self):
        """ Method for get root of the tree """
        return self.root

    def add(self, data):
        """ Method for add data to the tree """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """Method for add data to the tree

        Args:
            data (int): data to add

        Returns:
            None
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        """ Method to clear the entire tree, removing all nodes.
        
        This sets the root to None, effectively deleting all references to the nodes.
        """
        self.root = None

    def printTree(self):
        """ Print the entire tree in an inorder traversal.

        This method serves as a wrapper to initiate the inorder traversal print starting from the root.
        """
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        """ Recursive method to print the tree's data in an inorder manner.

        Args:
            node (Node): The current node to process.

        This method recursively visits the left child, prints the current node's data, then visits the right child.
        """
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        """ Recursive method to print the tree's data in a preorder manner. """
        if node is not None:
            print(str(node.data) + ' ', end='')
            self._printPreorderTree(node.left)
            self._printPreorderTree(node.right)

    def _printPostorderTree(self, node):
        """ Recursive method to print the tree's data in a postorder manner. """
        if node is not None:
            self._printPostorderTree(node.left)
            self._printPostorderTree(node.right)
            print(str(node.data) + ' ', end='')

import unittest


class TestTreeFindMethod(unittest.TestCase):

    def test_find_existing_data(self):
        tree = Tree()
        values = [20, 10, 30, 5, 15]
        for value in values:
            tree.add(value)
        result = tree.find(15)
        self.assertIsNotNone(result)
        self.assertEqual(result.data, 15)

    def test_find_non_existing_data(self):
        tree = Tree()
        values = [20, 10, 30, 5, 15]
        for value in values:
            tree.add(value)
        result = tree.find(100)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()