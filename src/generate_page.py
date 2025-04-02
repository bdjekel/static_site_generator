from extract_title import extract_title
from htmlnode import HTMLNode
from markdown_to_html_node import markdown_to_html_node
import os

def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown_content: str = f.read()

    with open(template_path, "r") as f:
        template_content: str = f.read()

    node_tree: HTMLNode = markdown_to_html_node(markdown_content)

    html_tree: str = node_tree.to_html()

    title: str = extract_title(markdown_content)

    template_content: str = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html_tree)
    template_content = template_content.replace('href="/', 'href="' + basepath)
    template_content = template_content.replace('src="/', 'src="' + basepath)
    dest_dir: str = os.path.dirname(dest_path)

    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template_content)

    