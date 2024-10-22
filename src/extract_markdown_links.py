import re

def extract_markdown_links(raw_markdown_string):
    matches = re.findall(r'\[([\w\d\s.]+)\]\(([\w\d\s\./]+)\)', raw_markdown_string)
    print(matches)

sb_meme = '../assets/tired_spongebob.webp'
raw_markdown_string = 'Spongebob Squarepants is show about enjoying the [little things](../assets/tired_spongebob.webp) in life.'

extract_markdown_links(raw_markdown_string)