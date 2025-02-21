import re

def extract_markdown_links(raw_markdown_string):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", raw_markdown_string)
    return matches
