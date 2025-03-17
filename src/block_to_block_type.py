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
    elif all(line.startswith("- ") for line in markdown_block.splitlines()):
        return BlockType.UNORDERED_LIST

# TODO: if for loop starts, but fails...func returns "None". 
    elif markdown_block.startswith("1. "):
        print(f"oooooooohhhhhh. shit might be ordered\n{markdown_block}")
        is_ordered = True
        for i, line in enumerate(markdown_block.splitlines()):
            if not line.startswith(f"{i + 1}. "):
                is_ordered = False
                print(f"is_ordered = {is_ordered}")
                break
            else:
                print("CONTINUING")
        print("we are out of the for loop")
        if is_ordered: return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
            
