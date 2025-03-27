#TODO: add type hinting to entire file

def markdown_to_blocks(markdown: str) -> list[str]:
    cleaned_blocks: list[str] = []

    if markdown == "":
        return ""

    raw_blocks: list[str] = markdown.split("\n\n")

    for block in raw_blocks:
        stripped_block: str = block.strip()
        if not stripped_block:
            continue
        block_newlines: list[str] = [line.strip() for line in stripped_block.split("\n")]
        cleaned_block: str = "\n".join(block_newlines)

        cleaned_blocks.append(cleaned_block)

    return cleaned_blocks

