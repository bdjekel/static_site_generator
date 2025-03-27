import re

def extract_markdown_links(raw_markdown: str) -> list:
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", raw_markdown)
    return matches
