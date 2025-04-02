from extract_title import extract_title
from generate_page import generate_page
from markdown_to_html_node import markdown_to_html_node
import os
from pathlib import Path

#TODO: consider pulling smaller functions from their individual files and into the files of the larger functions they serve.

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str) -> None:

    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)        
        
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)

        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)

