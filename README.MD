# Size Calculator

Size Calculator is a Python package that calculates the size of a file or folder and prints it in bytes, kilobytes, and megabytes.

## Installation

You can install the package using pip:

```bash
pip install sizecalculator
```

## Usage

Once installed, you can use the `sizecalculator` command from the command line:

```bash
sizecalculator /path/to/your/file_or_folder
```

Replace `/path/to/your/file_or_folder` with the actual path of the file or folder you want to analyze.

### Using `print_size` in Your Python Script

You can also use the `print_size` function in your Python scripts or projects. Here's an example:

```python
from sizecalculator import print_size

file_or_folder_path = "/path/to/your/file_or_folder"
print_size(file_or_folder_path)
```

Replace `/path/to/your/file_or_folder` with the actual path of the file or folder you want to analyze.

## Example

```bash
sizecalculator /path/to/your/file_or_folder
```

This will print the size of the specified file or folder in bytes, kilobytes, and megabytes.




The size information will be displayed in human-readable format, including bytes, kilobytes, and megabytes.


