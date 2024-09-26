import unittest

from textnode import TextNode
from leafnode import LeafNode

from utils import (
    text_node_to_html_node, 
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    text_type_bold, 
    text_type_text, 
    text_type_code, 
    text_type_italic
)
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
    def test_extract_markdown_img(self):
        ex_text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted = extract_markdown_images(ex_text)
        expect = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(expect, extracted)
    def test_extract_empty_string(self):
        ex_text = ""
        extracted = extract_markdown_images(ex_text)
        expect = []
        self.assertEqual(expect, extracted)
    def test_extract_img_missing_url(self):
        ex_text = "This is text with a ![rick roll]"
        expect = Exception("The text string contains missing elements of valid Markdown image syntax")
        with self.assertRaises(Exception) as ctx:
            extract_markdown_images(ex_text)
        self.assertTrue(expect, str(ctx.exception))
    def test_extract_markdown_link(self):
        ex_text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted = extract_markdown_links(ex_text)
        expect = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(expect, extracted)
    def test_extract_link_empty_string(self):
        ex_text = ""
        extracted = extract_markdown_links(ex_text)
        expect = []
        self.assertEqual(expect, extracted)
    def test_extract_link_missing_url(self):
        ex_text = "This is text with a link [to boot dev]"
        expect = Exception("The text string contains missing elements of valid Markdown image syntax")
        with self.assertRaises(Exception) as ctx:
            extract_markdown_links(ex_text)
        self.assertTrue(expect, str(ctx.exception))