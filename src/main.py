from generate_pages_recursive import generate_pages_recursive
from move_content import move_content
import os
import shutil
import sys

#TODO: turn your paths into variables at the top of the file.

def main() -> None:
    
    basepath: str = "/"
    if len(sys.argv) > 1:
        basepath: str = sys.argv[1]
    print(basepath)

    if os.path.exists("./docs"):
        shutil.rmtree("./docs")
    os.mkdir("./docs")
    
    move_content("./static", "./docs")

    
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)

main()