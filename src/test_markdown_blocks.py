from markdown_blocks import *
import unittest

class TestMarkdownBlocks(unittest.TestCase):


    def test_markdown_to_blocks(self):
        print("testing markdown_to_blocks")
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_paragraphs(self):
        print("testing test_paragraphs")
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_single_heading(self):
        md = "# Hello there\n"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>Hello there</h1></div>")

    def test_single_quote(self):
        md = "> A wise bear\n> speaks softly\n"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><blockquote>A wise bear speaks softly</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """- one
- two with **bold**
- three
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>one</li><li>two with <b>bold</b></li><li>three</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """1. one
2. two with `code`
3. three
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>one</li><li>two with <code>code</code></li><li>three</li></ol></div>",
        )