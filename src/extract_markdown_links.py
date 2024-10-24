import re

def extract_markdown_links(raw_markdown_string):
    matches = re.findall(r'\s\[([\w\d\s\.\:\\\/\@\=\&\%\$\+]+)\]\(([\w\d\s\.\:\\\/\@\=\&\%\$\+]+)\)', raw_markdown_string)
    # print(raw_markdown_string)
    print(matches)
    return matches


sb_meme = '../assets/tired_spongebob.webp'
raw_md_link_string = f'Spongebob Squarepants is a show about enjoying the [little things]({sb_meme}) in life.'
raw_md_image_string = f'Spongebob Squarepants is a show about enjoying the ![little things]({sb_meme}) in life.'

# extract_markdown_links(raw_md_link_string)