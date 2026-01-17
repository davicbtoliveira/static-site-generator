import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is other text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_hasurl(self):
        node = TextNode("This is a text node", TextType.BOLD, url="https://boot.dev")
        self.assertTrue(node.url is not None)


if __name__ == "__main__":
    unittest.main()
