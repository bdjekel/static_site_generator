import os
import shutil

def move_content(src: str, dst: str) -> None | ValueError:

    if not os.path.exists(dst):
        os.mkdir(dst)

#TODO: if you need to maintain permissions for the dst directory, refactor using the below starting block.
    # os.chmod()

    src_tree: list[str] = os.listdir(src)

    for item in src_tree:
        
        item_path: str = os.path.join(src, item)
        new_dir_path: str = os.path.join(dst, item)
        
        if os.path.isfile(item_path):
            shutil.copy(item_path, dst)
        else:
            move_content(item_path, new_dir_path)

