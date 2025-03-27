import os
import shutil

def move_content(src: str, dst: str) -> None | ValueError:

# Since this is a recursive function, might need to delete or refactor error handling below.    
    if not os.path.exists(src):
        return ValueError("Source path does not exist")
    elif not os.path.exists(dst):
        return ValueError("Destination path does not exist")


    shutil.rmtree(dst)
    os.mkdir(dst)

#TODO: if you need to maintain permissions for the dst directory, refactor using the below starting block.
    # os.chmod()

    src_tree: list[str] = os.listdir(src)
    print("----------")
    print(src, dst)
    print("----------")

    for item in src_tree:
        
        print()
        print(item)

        item_path: str = os.path.join(src, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, dst)
            print("^file^")
        else:
            print("^dir^")
            new_dir_path: str = os.path.join(dst, item)
            os.mkdir(new_dir_path)
            move_content(item_path, new_dir_path)


