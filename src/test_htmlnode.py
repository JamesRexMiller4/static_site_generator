import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        html_node = HTMLNode("p", "This is an html node", "<span>shiny</span>", {})
        html_node1 = HTMLNode("p", "This is an html node", "<span>shiny</span>", {})
        self.assertEqual(html_node, html_node1)
    def test_empty(self):
        html_node = HTMLNode()
        html_node1 = HTMLNode(None, None, None, None)
        self.assertEqual(html_node, html_node1)
    def test_not__eq__(self):
        html_node = HTMLNode("p", "This is an html node", "<span>shiny</span>", {})
        html_node1 = HTMLNode(None, None, None, None)
        self.assertFalse(html_node.__eq__(html_node1))
    def test__repre__(self):
        TAG = "a"
        VALUE = "Click Me!"
        CHILDREN = None
        PROPS = {"href": "https://boot.dev", "title": "shiny"}
        html_node = HTMLNode(TAG, VALUE, CHILDREN, PROPS)
        expect = f"HTMLNode({TAG}, {VALUE}, {CHILDREN}, {PROPS})"
        self.assertEqual(expect, html_node.__repr__())
    def test_props_to_html(self):
        expect = " href='https://boot.dev' title='shiny'"
        html_node = HTMLNode("a", 'Click Me', None, {"href": "https://boot.dev", "title": "shiny"})
        self.assertEqual(expect, html_node.props_to_html())