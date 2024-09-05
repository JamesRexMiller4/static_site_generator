import unittest

from textnode import TextNode

class TestTestNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_uneq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a different text node", "italic", "https://bing.com")
        self.assertNotEqual(node, node2)
    def test__eq__(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertTrue(node.__eq__(node2))
    def test_not__eq__(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a different text node", "italic", "https://bing.com")
        self.assertFalse(node.__eq__(node2))
    def test__repr__(self):
        TEXT = "This is a text node"
        TEXT_TYPE = "italic"
        URL = "https://bing.com"

        node = TextNode(TEXT, TEXT_TYPE, URL)
        self.assertEqual(f"TextNode({TEXT}, {TEXT_TYPE}, {URL})", node.__repr__())



if __name__ == "__main__":
    unittest.main()