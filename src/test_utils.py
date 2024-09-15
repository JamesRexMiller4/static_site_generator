import unittest

from textnode import TextNode
from leafnode import LeafNode

from utils import text_node_to_html_node

class TestUtils(unittest.TestCase):
    def test_text_node_to_html_text(self):
        text_node = TextNode("coffee", "text")
        expect = LeafNode("coffee")
        result = text_node_to_html_node(text_node)
        self.assertEqual(expect, result)
    def test_text_node_to_html_bold(self):
        text_node = TextNode("loud noises", "bold")
        expect = LeafNode("b", "loud noises")
        result = text_node_to_html_node(text_node)
        self.assertEqual(expect, result)
    def test_text_node_to_html_italic(self):
        text_node = TextNode("fancy", "italic")
        expect = LeafNode("i", "fancy")
        result = text_node_to_html_node(text_node)
        self.assertEqual(expect, result)
    def test_text_node_to_html_code(self):
        text_node = TextNode("print('World, hold on')", "code")
        expect = LeafNode("code", "print('World, hold on')")
        result = text_node_to_html_node(text_node)
        self.assertEqual(expect, result)
    def test_text_node_to_html_link(self):
        text_node = TextNode("Link to the unknown", "link", 'https://wikipedia.org')
        expect = LeafNode("a", "Link to the unknown", { "href": "https://wikipedia.org"})
        result = text_node_to_html_node(text_node)
        self.assertEqual(expect, result)
    def test_text_node_to_html_image(self):
        text_node = TextNode('Blue whale', "image", "https://en.wikipedia.org/wiki/File:Southern_right_whale.jpg")
        expect = LeafNode("img", "", { "src": "https://en.wikipedia.org/wiki/File:Southern_right_whale.jpg", "alt": "Blue whale" })
        result = text_node_to_html_node(text_node)
        self.assertEqual(expect, result)
    def test_text_node_to_html_no_match(self):
        text_node = TextNode("New frontiers", "bussin")
        expect = Exception("No matching text node type")
        with self.assertRaises(Exception) as ctx:
            text_node_to_html_node(text_node)
        self.assertTrue(expect, str(ctx.exception))