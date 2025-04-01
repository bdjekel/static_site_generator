from generate_pages_recursive import generate_pages_recursive
from move_content import move_content
import os
import shutil

#TODO: incomplete

def main() -> None:
    
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")
    
    move_content("static", "public")
    generate_pages_recursive("content", "template.html", "public")

main()