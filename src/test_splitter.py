import unittest
from textnode import TextNode, TextType 
from textnode import text_node_to_html_node
from splitter import split_nodes_delimiter
from splitter import split_nodes_image
from splitter import split_nodes_link
from splitter import extract_markdown_images
from splitter import extract_markdown_links

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

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [link](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()