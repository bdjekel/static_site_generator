from generate_pages_recursive import generate_pages_recursive
from move_content import move_content
import os
import shutil
import sys


static_dir_path: str = "./static"
public_dir_path: str = "./docs"
content_dir_path: str = "./content"
template_path: str = "./template.html"
default_basepath: str = "/"

def main() -> None:
    
    basepath: str = default_basepath

    if len(sys.argv) > 1:
        basepath: str = sys.argv[1]

    if os.path.exists(public_dir_path):
        shutil.rmtree(public_dir_path)
    
    move_content(static_dir_path, public_dir_path)

    generate_pages_recursive(content_dir_path, template_path, public_dir_path, basepath)

main()