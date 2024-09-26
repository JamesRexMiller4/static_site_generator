import unittest

from textnode import TextNode
from leafnode import LeafNode

from utils import text_node_to_html_node, split_nodes_delimiter, text_type_bold, text_type_text, text_type_code, text_type_italic

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
    def test_text_split_nodes_delimiter_single_node(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        expect = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ]
        self.assertTrue(expect, new_nodes)
    def test_text_split_nodes_delimiter_multiple(self):
        node_1 = TextNode("I hear in France they write words in *italics*", text_type_text)
        node_2 = TextNode("I am French, *how dare you*", text_type_text)
        new_nodes = split_nodes_delimiter([node_1, node_2], "*", text_type_italic)
        expect = [
            TextNode("I hear in France they write words in ", text_type_text),
            TextNode("italics", text_type_italic),
            TextNode("", text_type_text),
            TextNode("I am French, ", text_type_text),
            TextNode("how dare you", text_type_italic),
            TextNode("", text_type_text)
        ]
        self.assertEqual(expect, new_nodes)
    def test_text_split_nodes_delimiter_text_no_nodes(self):
        new_nodes = split_nodes_delimiter([], "*", text_type_italic)
        expect = []
        self.assertEqual(expect, new_nodes)
    def test_text_split_nodes_delimiter_bold(self):
        node = TextNode("Nothing captivates the mind's ear like **LOUD NOISES** as you read", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        expect = [
            TextNode("Nothing captivates the mind's ear like ", text_type_text),
            TextNode("LOUD NOISES", text_type_bold),
            TextNode(" as you read", text_type_text)
        ]
        self.assertEqual(expect, new_nodes)