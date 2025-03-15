from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown_block):
    if not markdown_block:
        return
    
    # elected to use re.search and the "^" quantifier to practice regex more broadly. But with Python re, you can start from the beginning using re.match, eliminating the need for "^"
    elif re.search(r"^#{1,6}(?=\s)", markdown_block):
        return BlockType.HEADING
    
    elif re.search(r"^`{3}", markdown_block) and re.search(r"`{3}$", markdown_block):
        return BlockType.CODE
    
    elif all(line.startswith(">") for line in markdown_block.splitlines()):
        return BlockType.QUOTE
    
# TODO: failing test here
    elif all(line.startswith("- ") for line in markdown_block.split()):
        return BlockType.UNORDERED_LIST

# TODO: if for loop starts, but fails...func returns "None". 
    elif markdown_block.startswith("1. "):
        print("oooooooohhhhhh. shit might be ordered")
        list_ordered = True
        list_items = markdown_block.splitlines()
        print(f"LIST ITEMS ==> {list_items}")
        for index, item in enumerate(list_items):
            item_number = index + 1
            if not item.startswith(f"{item_number}. "):
                list_ordered = False
                break
        if list_ordered:
            return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
            
