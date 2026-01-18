import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "A paragraph", None, {"href": "test"})
        print(node.props_to_html())

    def test_neq(self):
        node = HTMLNode("p", "This is a HTML node")
        node2 = HTMLNode("a", "This is other HTML node", None, {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)

    def test_hasprops(self):
        node = HTMLNode("a", "This is a text node", None, {"href": "https://boot.dev"})
        self.assertTrue(node.props is not None)


if __name__ == "__main__":
    unittest.main()
