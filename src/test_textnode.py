import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("One of these things", TextType.ITALIC)
        node2 = TextNode("Is not like the other ones", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("Lorem ipsum", TextType.PLAIN, "https://bbc.com/news")
        node2 = TextNode("Lorem ipsum", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    def test_text_type(self):
        node = TextNode("Lorem ipsum", TextType.PLAIN)
        node2 = TextNode("Lorem ipsum", TextType.CODE)
        self.assertNotEqual(node, node2)

    


if __name__ == "__main__":
    unittest.main()
