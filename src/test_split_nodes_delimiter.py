import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode

# See markdown Scenario Table as comment at end of this test file

# node_1 can test these Scenarios:
#     > (1) no delimiter, toggle off
#     > (3) delimiter at start and end, toggle off

node_1_italic = TextNode("Spaghetti is not *Italic* cuisine.","text")
node_1_bold = TextNode("Fortune favors the **bold,** or so they say","text")
node_1_strikethrough = TextNode("Cheddar's Cat ~~Scratch~~ Kitchen Sink","text")

# node_1 expected output:
expected_nodes_1_italic = [
    TextNode("Spaghetti is not ", "text"),
    TextNode("Italic", "italic"), 
    TextNode(" cuisine.", "text")
    ]
expected_nodes_1_bold = [
    TextNode("Fortune favors the ", "text"),
    TextNode("bold,", "bold"), 
    TextNode(" or so they say", "text")
    ]
expected_nodes_1_strikethrough = [
    TextNode("Cheddar's Cat ", "text"),
    TextNode("Scratch", "strikethrough"), 
    TextNode(" Kitchen Sink", "text")
    ]


# node_2 can test these Scenarios:
#     > (5) start delimiter, toggle off
#     > (8) end delimiter, toggle on
#     > (2) no delimiter, toggle on

node_2_italic = TextNode("Spaghetti *is not Italic* cuisine.","text")
node_2_bold = TextNode("Fortune **favors the bold,** or so they say","text")
node_2_strikethrough = TextNode("Cheddar's ~~Cat Scratch Kitchen~~ Sink","text")

# node_2 expected output:
expected_nodes_2_italic = [
    TextNode("Spaghetti ", "text"),
    TextNode("is not Italic", "italic"), 
    TextNode(" cuisine.", "text")
    ]
expected_nodes_2_bold = [
    TextNode("Fortune ", "text"),
    TextNode("favors the bold,", "bold"), 
    TextNode(" or so they say", "text")
    ]
expected_nodes_2_strikethrough = [
    TextNode("Cheddar's ", "text"),
    TextNode("Cat Scratch Kitchen", "strikethrough"), 
    TextNode(" Sink", "text")
    ]


# node_3 can test these Scenarios:
#     > (7) end delimiter, toggle off
#     > (6) start delimiter, toggle on
#     > (1) no delimiter, toggle off
#     > (2) no delimiter, toggle on

node_3_italic = TextNode("Spaghetti is* not Italic *cuisine.","text")
node_3_bold = TextNode("Fortune** favors the bold, **or so they say","text")
node_3_strikethrough = TextNode("Cheddar's~~ Cat Scratch Kitchen ~~Sink","text")

# node_3 expected output:
expected_nodes_3_italic = [
    TextNode("Spaghetti is", "text"),
    TextNode(" not Italic ", "italic"), 
    TextNode("cuisine.", "text")
    ]
expected_nodes_3_bold = [
    TextNode("Fortune", "text"),
    TextNode(" favors the bold, ", "bold"), 
    TextNode("or so they say", "text")
    ]
expected_nodes_3_strikethrough = [
    TextNode("Cheddar's", "text"),
    TextNode(" Cat Scratch Kitchen ", "strikethrough"), 
    TextNode("Sink", "text")
    ]


# node_4 can test these Scenarios:
#     > (4) start and end with delimiters, toggle on
#     > (5) start delimiter, toggle off
#     > (8) end delimiter, toggle on
#     > (2) no delimiter, toggle on

node_4_italic = TextNode("*Spaghetti is not *Italic* cuisine.*","text")
node_4_bold = TextNode("**Fortune favors the **bold,** or so they say**","text")
node_4_strikethrough = TextNode("~~Cheddar's Cat ~~Scratch~~ Kitchen Sink~~","text")

# node_4 expected output:
expected_nodes_4_italic = [
    TextNode("Spaghetti is not ", "italic"),
    TextNode("Italic", "text"), 
    TextNode(" cuisine.", "italic")
    ]
expected_nodes_4_bold = [
    TextNode("Fortune favors the ", "bold"),
    TextNode("bold,", "text"), 
    TextNode(" or so they say", "bold")
    ]
expected_nodes_4_strikethrough = [
    TextNode("Cheddar's Cat ", "strikethrough"),
    TextNode("Scratch", "text"), 
    TextNode(" Kitchen Sink", "strikethrough")
    ]   

# node_5 can test these Scenarios:
#     > (9) isolated delimiter, toggle off
#     > (10) isolated delimiter, toggle on

node_5_italic = TextNode('Texas: The Lone * Star * State', "text")
node_5_bold = TextNode('The average distance between ** two stars ** is 5 light years', "text")
node_5_strikethrough = TextNode('Three ~~ strikes ~~ and you\'reeeeee outta here', "text")

# node_5 expected output:
expected_nodes_5_italic = [
    TextNode("Texas: The Lone ", "text"),
    TextNode(" Star ", "italic"), 
    TextNode(" State", "text")
    ]
expected_nodes_5_bold = [
    TextNode("The average distance between ", "text"),
    TextNode(" two stars ", "bold"), 
    TextNode(" is 5 light years", "text")
    ]
expected_nodes_5_strikethrough = [
    TextNode("Three ", "text"),
    TextNode(" strikes ", "strikethrough"), 
    TextNode(" and you'reeeeee outta here", "text")
    ]  

# node_6 can test these Scenarios:
#     > (9) isolated delimiter, toggle off
#     > (8) end delimiter, toggle on 


node_6_italic = TextNode('Texas: The Lone * Star* State', "text")
node_6_bold = TextNode('The average distance between ** two stars** is 5 light years', "text")
node_6_strikethrough = TextNode('Three ~~ strikes~~ and you\'reeeeee outta here', "text")

# node_6 expected output:
expected_nodes_6_italic = [
    TextNode("Texas: The Lone ", "text"),
    TextNode(" Star", "italic"), 
    TextNode(" State", "text")
    ]
expected_nodes_6_bold = [
    TextNode("The average distance between ", "text"),
    TextNode(" two stars", "bold"), 
    TextNode(" is 5 light years", "text")
    ]
expected_nodes_6_strikethrough = [
    TextNode("Three ", "text"),
    TextNode(" strikes", "strikethrough"), 
    TextNode(" and you'reeeeee outta here", "text")
    ]  

# node_7 can test these Scenarios:
#     > (8) start delimiter, toggle off
#     > (10) isolated delimiter, toggle on

node_7_italic = TextNode('Texas: The Lone *Star * State', "text")
node_7_bold = TextNode('The average distance between **two stars ** is 5 light years', "text")
node_7_strikethrough = TextNode('Three ~~strikes ~~ and you\'reeeeee outta here', "text")

# node_7 expected output:
expected_nodes_7_italic = [
    TextNode("Texas: The Lone ", "text"),
    TextNode("Star ", "italic"), 
    TextNode(" State", "text")
    ]
expected_nodes_7_bold = [
    TextNode("The average distance between ", "text"),
    TextNode("two stars ", "bold"), 
    TextNode(" is 5 light years", "text")
    ]
expected_nodes_7_strikethrough = [
    TextNode("Three ", "text"),
    TextNode("strikes ", "strikethrough"), 
    TextNode(" and you'reeeeee outta here", "text")
    ]  

old_italic_nodes = [node_1_italic, node_2_italic, node_3_italic, node_4_italic, node_5_italic, node_6_italic, node_7_italic]
old_bold_nodes = [node_1_bold, node_2_bold, node_3_bold, node_4_bold, node_5_bold, node_6_bold, node_7_bold]
old_strikethrough_nodes = [node_1_strikethrough, node_2_strikethrough, node_3_strikethrough, node_4_strikethrough, node_5_strikethrough, node_6_strikethrough, node_7_strikethrough]

old_nodes_combined = old_italic_nodes + old_bold_nodes + old_strikethrough_nodes

expected_italic_nodes = expected_nodes_1_italic + expected_nodes_2_italic + expected_nodes_3_italic + expected_nodes_4_italic + expected_nodes_5_italic + expected_nodes_6_italic + expected_nodes_7_italic 

expected_bold_nodes = expected_nodes_1_bold + expected_nodes_2_bold + expected_nodes_3_bold + expected_nodes_4_bold + expected_nodes_5_bold + expected_nodes_6_bold + expected_nodes_7_bold

expected_strikethrough_nodes = expected_nodes_1_strikethrough + expected_nodes_2_strikethrough + expected_nodes_3_strikethrough + expected_nodes_4_strikethrough + expected_nodes_5_strikethrough + expected_nodes_6_strikethrough + expected_nodes_7_strikethrough

expected_nodes_combined = expected_italic_nodes + expected_bold_nodes + expected_strikethrough_nodes

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_singluar_nodes_italic(self):
        resulting_italic_nodes = split_nodes_delimiter([node_1_italic], '*', 'italic')
        self.assertEqual(resulting_italic_nodes, expected_nodes_1_italic)

    def test_singluar_nodes_bold(self):
        resulting_bold_nodes = split_nodes_delimiter([node_1_bold], '**', 'bold')
        self.assertEqual(resulting_bold_nodes, expected_nodes_1_bold)

    def test_singluar_nodes_strikethrough(self):
        resulting_strikethrough_nodes = split_nodes_delimiter([node_1_strikethrough], '~~', 'strikethrough')
        self.assertEqual(resulting_strikethrough_nodes, expected_nodes_1_strikethrough)

    def test_all_scenarios_with_italic(self):
        self.maxDiff = None
        resulting_italic_nodes = split_nodes_delimiter(old_italic_nodes, '*', "italic")
        self.assertEqual(resulting_italic_nodes, expected_italic_nodes)

    def test_all_scenarios_with_bold(self):
        self.maxDiff = None
        resulting_bold_nodes = split_nodes_delimiter(old_bold_nodes, '**', "bold")
        self.assertEqual(resulting_bold_nodes, expected_bold_nodes)

    def test_all_scenarios_with_strikethrough(self):
        self.maxDiff = None
        resulting_strikethrough_nodes = split_nodes_delimiter(old_strikethrough_nodes, '~~', "strikethrough")
        self.assertEqual(resulting_strikethrough_nodes, expected_strikethrough_nodes)


    # def test_all_scenarios_run_all_delimiters(self):
    #     self.maxDiff = None
    #     nodes_with_italics_processed = split_nodes_delimiter(old_nodes_combined, '*', 'italic')
    #     nodes_with_bolds_processed = split_nodes_delimiter(nodes_with_italics_processed, '**', 'bold')
    #     nodes_with_strikethroughs_processed = split_nodes_delimiter(nodes_with_bolds_processed, '~~', 'strikethrough')
    #     self.assertEqual(nodes_with_strikethroughs_processed, expected_nodes_combined)

        
    


if __name__ == "__main__":
    unittest.main()


# | Scenario ID | Example | Toggle |         Action Description              | Test Node Reference
# |:-----------:|:-------:|:------:|:----------------------------------------|:-----------------:|
# |     (1)     |  test   | False  | add this word to normal phrase          | node_1 |
# |     (2)     |  test   |  True  | add this word to delimited phrase       | node_2 |
# |     (3)     |  *test* | False  | add this word to delimited phrase       | node_1 |
# |     (4)     |  *test* |  True  | end first delimited phrase (before this word), add this word to normal phrase, start second delimited phrase (after this word)            | node_4 |
# |     (5)     |  *test  | False  | start delimited phrase (with this word) | node_2 |
# |     (6)     |  *test  |  True  | end delimited phrase (before this word) | node_3 |
# |     (7)     |  test*  | False  | start delimited phrase (with next word) | node_3 |
# |     (8)     |  test*  |  True  | end delimited phrase (after this word)  | node_2 |
