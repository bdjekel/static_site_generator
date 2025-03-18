from htmlnode import HTMLNode
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType

def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    print(f"markdown_blocks => {markdown_blocks}")
    for block in markdown_blocks:
        print(f"block => {block}")   
        block_type = block_to_block_type(block)
        print(f"block_type => {block_type.value}")   
        block_html_node = HTMLNode(block_type.value, block)
        print(f"block_html_node => {block_html_node}")   
    return 0


# Split the markdown into blocks (you already have a function for this)
# Loop over each block:
    # Determine the type of block (you already have a function for this)
    # Based on the type of block, create a new HTMLNode with the proper data
    # Assign the proper child HTMLNode objects to the block node. I created a shared text_to_children(text) function that works for all block types. It takes a string of text and returns a list of HTMLNodes that represent the inline markdown using previously created functions (think TextNode -> HTMLNode).
    # The "code" block is a bit of a special case: it should not do any inline markdown parsing of its children. I didn't use my text_to_children function for this block type, I manually made a TextNode and used text_node_to_html_node.
# Make all the block nodes children under a single parent HTML node (which should just be a div) and return it.
md1 = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""


md2 = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

markdown_to_html_node(md1)