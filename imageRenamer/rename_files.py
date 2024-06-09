import os
import sys
from pathlib import Path

def rename_files(directory, new_filenames):
    """Rename image files in a specified directory based on list of new filenames
    and the directory name."""
    dir_path = Path(directory)  # Convert directory to Path object
    if not dir_path.is_dir():
        print("The specified directory does not exist.")

    dir_name = dir_path.name  # Get the name of the directory

    # List all files in the directory
    files = [f for f in dir_path.iterdir() if f.is_file()]

    # Initialize counters for suffixes to ensure unique filenames
    counters = {name: 0 for name in new_filenames}

    for i, file in enumerate(files):
        name_index = i % len(new_filenames)  # Calculate index in the new_filenames list
        base_name = new_filenames[name_index]
        suffix = counters[base_name]

        # Form the new name with a suffix if needed
        if suffix > 0:
            new_name = f"{base_name}{dir_name}-{suffix}{file.suffix}"
        else:
            new_name = f"{base_name}{dir_name}{file.suffix}"

        counters[base_name] += 1  #  Increment the counter for the current base name
        new_file_path = dir_path / new_name  # Form the new file path

        # Rename the file
        file.rename(new_file_path)
        print(f"Renamed {file} to {new_file_path}")

if __name__ == "__main__":
    # Check if the script is run with the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python rename_files.py <directory>")
    else:
        directory = sys.argv[1]  # Get the directory from the command-line argument
        # List of new filenames
        new_filenames = [
            'office_space_', 'coworking_', 'office_for_rent_', 'furnished_office_',
            'conference_rooms_', 'executive_suites_', 'serviced_office_',
            'meeting_room_', 'shared_office_space_'
        ]
        # Call the rename_files function with the provided directory and filenames
        rename_files(directory, new_filenames)




