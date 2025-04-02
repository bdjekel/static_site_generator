from generate_pages_recursive import generate_pages_recursive
from move_content import move_content
import os
import shutil
import sys

#TODO: turn your paths into variables at the top of the file.

static_dir_path = "./static"
public_dir_path = "./docs"
content_dir_path = "./content"
template_path = "./template.html"
basepath: str = "/"

def main() -> None:
    
    if len(sys.argv) > 1:
        basepath: str = sys.argv[1]
    print(basepath)

    if os.path.exists(public_dir_path):
        shutil.rmtree(public_dir_path)
    # os.mkdir("./docs")
    
    move_content(static_dir_path, public_dir_path)

    generate_pages_recursive(content_dir_path, template_path, public_dir_path, basepath)

main()