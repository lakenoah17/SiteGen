import unittest
from textnode import TextNode, TextType 
from textnode import text_node_to_html_node
from splitter import split_nodes_delimiter

class TestSplitter(unittest.TestCase):
    def test_split_bold(self):
        node = TextNode("This **is a text node**", TextType.PLAIN)
        node_expected_1 = TextNode("This ", TextType.PLAIN)
        node_expected_2 = TextNode("is a text node", TextType.BOLD)
        results = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(results[0], node_expected_1)
        self.assertEqual(results[1], node_expected_2)

    def test_split_code(self):
        node = TextNode("This `is a text node`", TextType.PLAIN)
        node_expected_1 = TextNode("This ", TextType.PLAIN)
        node_expected_2 = TextNode("is a text node", TextType.CODE)
        results = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(results[0], node_expected_1)
        self.assertEqual(results[1], node_expected_2)

    def test_split_italics(self):
        node = TextNode("This _is a text node_", TextType.PLAIN)
        node_expected_1 = TextNode("This ", TextType.PLAIN)
        node_expected_2 = TextNode("is a text node", TextType.ITALIC)
        results = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(results[0], node_expected_1)
        self.assertEqual(results[1], node_expected_2)

if __name__ == "__main__":
    unittest.main()