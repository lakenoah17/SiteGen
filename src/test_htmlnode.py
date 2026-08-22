import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("p", "This is text", [], {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\"")

    def test_props_none(self):
        node = HTMLNode("p", "This is text", [])
        self.assertEqual(node.props_to_html(), "")

    def test_empty(self):
        node = HTMLNode()
        self.assertEqual(node.value, None)

if __name__ == "__main__":
    unittest.main()