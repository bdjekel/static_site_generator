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
    
    elif re.search(r"^`{3}", markdown_block) and re.search(r"$`{3}", markdown_block):
        return BlockType.CODE
    
    elif markdown_block.startswith(">"):
        block_lines = 
        return BlockType.HEADING
    
    elif markdown_block.startswith("#"):
        return BlockType.HEADING
    