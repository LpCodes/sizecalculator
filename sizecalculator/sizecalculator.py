# filesizecalculator.py

import os


def get_size(path):
    """
      Calculate the total size of the specified file or folder.

      Args:
          path (str): The path to the file or folder.

      Returns:
          int: Total size in bytes.
      """
    total_size = 0

    if os.path.isfile(path):
        total_size = os.path.getsize(path)
    elif os.path.isdir(path):
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)

    return total_size


def print_size(path):
    """
    Print the size of the specified file or folder in bytes, kilobytes, and megabytes.

    Args:
        path (str): The path to the file or folder.
    """
    size_in_bytes = get_size(path)
    size_in_kb = size_in_bytes / 1024
    size_in_mb = size_in_kb / 1024

    print(f"Size in bytes: {size_in_bytes} bytes")
    print(f"Size in kilobytes: {size_in_kb:.4f} KB")
    print(f"Size in megabytes: {size_in_mb:.4f} MB")


if __name__ == "__main__":

    import sys

    if len(sys.argv) != 2:
        print("Usage: python sizecalculator.py <file_or_folder_path>")
    else:
        file_or_folder_path = sys.argv[1]
        print_size(file_or_folder_path)
