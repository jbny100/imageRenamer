# Image File Renamer

This Python program renames image files in a given directory based on a list of predetermined names and the name of the directory itself. Each new filename in the target directory will be unique and will be determined based on the value of that file’s corresponding index position in the `new_filenames` list, plus the name of the folder.

## Features

- Renames image files in a specified directory.
- Uses a list of predetermined names to create new filenames.
- Ensures each filename is unique, even if there are more files than names in the list.
- Appends a unique suffix if necessary to avoid duplicate filenames.
- Adds the name of the directory to the end of each new filename.

## Requirements

- Python 3.x

## Usage

1. Clone or download the script to your local machine.
2. Navigate to the directory containing the script using your terminal or command prompt.
3. Run the script with the path to the directory containing the image files as an argument.

### Example

```bash
python rename_files.py /path/to/your/image_directory
