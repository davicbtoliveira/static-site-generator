import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "A paragraph", None, {"href": "test"})
        print(node.props_to_html())

    def test_neq(self):
        node = HTMLNode("p", "This is a HTML node")
        node2 = HTMLNode("a", "This is other HTML node", None,
                         {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)

    def test_hasprops(self):
        node = HTMLNode("a", "This is a text node", None,
                        {"href": "https://boot.dev"})
        self.assertTrue(node.props is not None)

    def test_leaf_to_html_p(self):
        node = LeafNode('p', 'Hello World!')
        self.assertEqual(node.to_html(), '<p>Hello World!</p>')

    def test_leaf_to_html_a(self):
        node = LeafNode('a', 'Click me!', {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
