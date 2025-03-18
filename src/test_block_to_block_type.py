import unittest
from block_to_block_type import BlockType, block_to_block_type

class TestMarkdownToBlocks(unittest.TestCase):
    def test_heading1(self):
        heading = "# This is a heading"
        self.assertEqual(block_to_block_type(heading), BlockType.HEADING1)
    
    def test_heading2(self):
        heading = "## This is a heading"
        self.assertEqual(block_to_block_type(heading), BlockType.HEADING2)
    
    def test_heading3(self):
        heading = "### This is a heading"
        self.assertEqual(block_to_block_type(heading), BlockType.HEADING3)

    def test_heading4(self):
        heading = "#### This is a heading"
        self.assertEqual(block_to_block_type(heading), BlockType.HEADING4)

    def test_heading5(self):
        heading = "##### This is a heading"
        self.assertEqual(block_to_block_type(heading), BlockType.HEADING5)

    def test_heading6(self):
        heading6 = "###### This is a heading"
        self.assertEqual(block_to_block_type(heading6), BlockType.HEADING6)

    def test_code_no_newline(self):
        code = "``` This is code```"
        self.assertEqual(block_to_block_type(code), BlockType.CODE)

    def test_code_with_newlines(self):
        code = "```\nThis is code\n\nif not code:\nquestion.ask(why is it in backticks then?)\n```"
        self.assertEqual(block_to_block_type(code), BlockType.CODE)
    
    def test_quote(self):
        quote = "> Craig was held back in 3rd grade\n> but started Kindergarten at 3 years old.\n>What grade is Craig when he gets his driver's license at 16?"
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)

    def test_unordered_list(self):
        u_list = "- this could be the last\n- or the first\n- bullet point.\n- disorder is chaos\n- but unorder is flexibility."
        self.assertEqual(block_to_block_type(u_list), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        o_list = "1. snow shovel belongs to Old Man Marley.\n2. turtle doves for the crazy bird lady.\n3. Home Alone's is one too many.\n4. Ran out of steam trying to be clever."
        self.assertEqual(block_to_block_type(o_list), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        paragraph = "29 Kids go into the water, 22 Kids come out of the water. The Ice Cream Man, He gets the rest. April the 9th, Half past four P.M."
        self.assertEqual(block_to_block_type(paragraph), BlockType.PARAGRAPH)

# TODO: write failing examples for each case above.
    def test_empty_string(self):
        pass

    def test_non_string(self):
        pass
    