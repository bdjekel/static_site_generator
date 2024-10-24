import re

def extract_markdown_images(raw_markdown_string):
    matches = re.findall(r'\!\[([\w\d\s\.\:\\\/\@\=\&\%\$\+]+)\]\(([\w\d\s\.\:\\\/\@\=\&\%\$\+]+)\)', raw_markdown_string)
    print(matches)

    return matches