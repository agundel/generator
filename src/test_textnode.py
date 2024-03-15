import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test.eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

if__name__ == "__main__":
    unittest.main()
