import os
import shutil

def move_content(src: str, dst: str) -> None | ValueError:

    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)

#TODO: if you need to maintain permissions for the dst directory, refactor using the below starting block.
    # os.chmod()

    src_tree: list[str] = os.listdir(src)

    for item in src_tree:
        
        print()
        print(item)

        item_path: str = os.path.join(src, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, dst)
        else:
            new_dir_path: str = os.path.join(dst, item)
            os.mkdir(new_dir_path)
            move_content(item_path, new_dir_path)

