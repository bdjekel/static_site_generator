

def markdown_to_blocks(markdown: str):
    cleaned_blocks = []
    if markdown == "":
        print("EMPTY STRING")
        return ""

    raw_blocks = markdown.split("\n\n")
    print(f"RAW_BLOCKS ==> {raw_blocks}")
    for block in raw_blocks:
        stripped_block = block.strip()
        if not stripped_block:
            print(f"BLOCK EMPTY")
            continue
        print(f"STRIPPED_BLOCK ==> {stripped_block}")        
        block_newlines = [line.strip() for line in stripped_block.split("\n")]
        print(f"BLOCK_NEWLINES ==> {block_newlines}")
        cleaned_block = "\n".join(block_newlines)
        print(f"CLEANED_BLOCK ==> {cleaned_block}")

        cleaned_blocks.append(cleaned_block)
        print(f"CLEANED_BLOCKS ==> {cleaned_blocks}")

    return cleaned_blocks

