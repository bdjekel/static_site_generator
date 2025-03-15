

def markdown_to_blocks(markdown: str):
    cleaned_blocks = []

    if markdown == "":
        return ""

    raw_blocks = markdown.split("\n\n")

    for block in raw_blocks:
        stripped_block = block.strip()
        if not stripped_block:
            continue
        block_newlines = [line.strip() for line in stripped_block.split("\n")]
        cleaned_block = "\n".join(block_newlines)

        cleaned_blocks.append(cleaned_block)

    return cleaned_blocks

