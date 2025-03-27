from block_to_block_type import block_to_block_type, BlockType
from leafnode import LeafNode
from markdown_to_blocks import markdown_to_blocks
from parentnode import ParentNode
from text_to_children import text_to_children

#TODO: add type hinting to entire file
#TODO: Add feature to allow for markdown within blockquotes

def markdown_to_html_node(markdown):
    wrapper_div = ParentNode("div", children=[])
    markdown_blocks = markdown_to_blocks(markdown)
    
    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.HEADING1 | BlockType.HEADING2 | BlockType.HEADING3 | BlockType.HEADING4 | BlockType.HEADING5 | BlockType.HEADING6:
                block = block.strip("#")
                block = block.strip()
                heading_node = LeafNode(block_type.value, block)
                wrapper_div.children.append(heading_node)
            case BlockType.CODE:
                block = block.strip("`")    # Since "`" is both a block level and inline level delimiter, must be stripped to avoid throwing error
                code_node = LeafNode(block_type.value, block)
                wrapper_div.children.append(code_node)
            case BlockType.QUOTE:
                block = block.strip("> ")
                quote_node = LeafNode(block_type.value, block)
                wrapper_div.children.append(quote_node)
            case BlockType.UNORDERED_LIST:
                ul_node = list_to_nodes(block, block_type.value)
                wrapper_div.children.append(ul_node)
            case BlockType.ORDERED_LIST:
                ol_node = list_to_nodes(block, block_type.value)
                wrapper_div.children.append(ol_node)
            case _:
                other_node = ParentNode(block_type.value, children=[])
                children = text_to_children(block)
                other_node.children = children
                wrapper_div.children.append(other_node)
    return wrapper_div

def list_to_nodes(block, tag):
    list_node = ParentNode(tag, children=[])
    leaf_nodes = []
    list_items = block.splitlines()
    for item in list_items:
        children = text_to_children(item)
        if len(children) == 0:
            leaf_nodes.append(LeafNode("li", item))
        else:
            leaf_nodes.append(ParentNode("li", children))
    list_node.children = leaf_nodes
    return list_node





















