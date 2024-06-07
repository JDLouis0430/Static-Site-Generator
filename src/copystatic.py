import os
import shutil

def copy_files_recursive(source_dir_path, dest_dir_path):
    # Check if the source directory exists
    if not os.path.exists(source_dir_path):
        print(f"Source directory {source_dir_path} does not exist. Skipping copy.")
        return

    # Ensure the destination directory exists
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    # Iterate over the items in the source directory
    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

# Example usage (uncomment the following lines to test the function):
# copy_files_recursive('path_to_source', 'path_to_destination')
