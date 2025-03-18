from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "p"
    HEADING1 = "h1"
    HEADING2 = "h2"
    HEADING3 = "h3"
    HEADING4 = "h4"
    HEADING5 = "h5"
    HEADING6 = "h6"
    CODE = "code"
    QUOTE = "q"
    UNORDERED_LIST = "ul"
    ORDERED_LIST = "ol"


def block_to_block_type(markdown_block):
    if not markdown_block:
        return
    
    # elected to use re.search and the "^" quantifier to practice regex more broadly. But with Python re, you can start from the beginning using re.match, eliminating the need for "^"
    elif re.search(r"^#{1,6}(?=\s)", markdown_block):
        if re.search(r"^#{6}(?=\s)", markdown_block):
            return BlockType.HEADING6
        elif re.search(r"^#{5}(?=\s)", markdown_block):
            return BlockType.HEADING5
        elif re.search(r"^#{4}(?=\s)", markdown_block):
            return BlockType.HEADING4
        elif re.search(r"^#{3}(?=\s)", markdown_block):
            return BlockType.HEADING3
        elif re.search(r"^#{2}(?=\s)", markdown_block):
            return BlockType.HEADING2
        elif re.search(r"^#{1}(?=\s)", markdown_block):
            return BlockType.HEADING1
        
    elif re.search(r"^`{3}", markdown_block) and re.search(r"`{3}$", markdown_block):
        return BlockType.CODE
    
    elif all(line.startswith(">") for line in markdown_block.splitlines()):
        return BlockType.QUOTE
    
    elif all(line.startswith("- ") for line in markdown_block.splitlines()):
        return BlockType.UNORDERED_LIST

    elif markdown_block.startswith("1. "):
        is_ordered = True
        for i, line in enumerate(markdown_block.splitlines()):
            if not line.startswith(f"{i + 1}. "):
                is_ordered = False
                break
            else:
                continue
        if is_ordered: return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
            
