from generate_page import generate_page
from move_content import move_content
import os
import shutil

#TODO: incomplete

def main() -> None:
    
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")
    
    move_content("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

main()