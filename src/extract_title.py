import re

def extract_title(markdown):
    markdown_lines = markdown.splitlines()

    for line in markdown_lines:
        stripped_line = line.lstrip()
        title = re.search(r"^#\s(.+)", stripped_line)
        if title:
            return title.group(1)

    raise ValueError("String must start with title as h1 Heading")
    