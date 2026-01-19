import unittest
from leafnode import LeafNode


class TesteLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode('p', 'Hello World!')
        self.assertEqual(node.to_html(), '<p>Hello World!</p>')

    def test_leaf_to_html_a(self):
        node = LeafNode('a', 'Click me!', {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>')
