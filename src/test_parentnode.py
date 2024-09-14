import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
        p_node = ParentNode("section", children)
        p_node1 = ParentNode("section", children)
        self.assertEqual(p_node, p_node1)
    def test_not__eq__(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
        children1 = [
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            LeafNode("b", "Bold text"),
        ]

        p_node = ParentNode("section", children)
        p_node1 = ParentNode("section", children1)
        self.assertFalse(p_node.__eq__(p_node1))
    def test__repr__(self):
        TAG = "section"
        CHILDREN = "[LeafNode('b', 'Bold text'), LeafNode(None, 'Normal text'), LeafNode('i', 'italic text'), LeafNode(None, 'Normal text')]"
        PROPS = None
        expect = f"ParentNode({TAG}, {CHILDREN}, {PROPS})"
        p_node = ParentNode("section", CHILDREN)
        self.assertEqual(expect, p_node.__repr__())
    def test_missing_tag_to_html(self):
        p_node = ParentNode()
        expect = "Instance has no tag value assigned"
        with self.assertRaises(ValueError) as ctx:
            p_node.to_html()
        self.assertTrue(expect in str(ctx.exception))
    def test_missing_children_to_html(self):
        p_node = ParentNode("section")
        expect = "Instance has no children"
        with self.assertRaises(ValueError) as ctx:
            p_node.to_html()
        self.assertTrue(expect in str(ctx.exception))
    def test_to_html_one_child(self):
        p_node = ParentNode("section", [LeafNode("p", "Hello world")])
        expect = "<section><p>Hello world</p></section>"
        self.assertEqual(expect, p_node.to_html())
    def test_to_html_multiple_children(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ]
        p_node = ParentNode("span", children)
        expect = "<span><b>Bold text</b>Normal text<i>italic text</i>Normal text</span>"
        self.assertEqual(expect, p_node.to_html())
    def test_to_html_with_props(self):
        children = [LeafNode("a", "Click me!", {"href": "https://boot.dev", "title": "To knowledge"})]
        p_node = ParentNode("button", children)
        expect = "<button><a href='https://boot.dev' title='To knowledge'>Click me!</a></button>"
        self.assertEqual(expect, p_node.to_html())
    def test_parent_node_inside_parent_node(self):
        children = [ParentNode("p", [LeafNode("b", "Bold text")])]
        p_node = ParentNode("section", children)
        expect = "<section><p><b>Bold text</b></p></section>"
        self.assertEqual(expect, p_node.to_html())
