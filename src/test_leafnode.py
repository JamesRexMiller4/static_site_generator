import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        leafnode = LeafNode("p", "This is a paragraph")
        leafnode1 = LeafNode("p", "This is a paragraph")
        self.assertEqual(leafnode, leafnode1)
    def test_repr(self):
        TAG = "p"
        VALUE = "This is a paragraph"
        PROPS = None
        expect = f"LeafNode({TAG}, {VALUE}, {PROPS})"
        leafnode = LeafNode("p", "This is a paragraph")
        self.assertEqual(expect, leafnode.__repr__())
    def test_eq(self):
        leafnode = LeafNode("a", "Click Me!", {"href": "https://boot.dev"})
        leafnode1 = LeafNode("a", "Click Me!", {"href": "https://boot.dev"})
        self.assertTrue(leafnode.__eq__(leafnode1))
    def test_requires_value(self):
        leafnode = LeafNode("a")
        expect = ValueError
        self.assertEqual(expect, leafnode.to_html())
    def test_missing_tag(self):
        leafnode = LeafNode(None, "I'm a dawg")
        expect = "I'm a dawg"
        self.assertEqual(expect, leafnode.to_html())
    def test_to_html(self):
        leafnode = LeafNode("a", "Click Me!", {"href": "https://boot.dev"})
        expect = "<a href='https://boot.dev'>Click Me!</a>"
        self.assertEqual(expect, leafnode.to_html())