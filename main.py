import os
import re
import shutil
import tkinter as tk
from tkinter import filedialog


def organize_files(src_dir, dest_dir):
    """
    Organizes wavfiles in the source directory into subdirectories based on the specified naming format
    and copies them to the destination directory. The format is *_##_#####.wav where * = BirdID, ## = relative recording day,
    ##### = serial number.

    A BirdID-named directory and recording day subdirectories are created. Wav files are then copied into appropriate
    subdirectories.

    Parameters:
        src_dir (str): Path to the source directory containing the files to be organized.
        dest_dir (str): Path to the destination directory where organized folders will be created.
        BirdID is prompted for at the command line.
    """

    # Get all files in the source directory
    files = os.listdir(src_dir)

    # Define the regex pattern to match the files
    pattern = re.compile(r'^(.*)_([0-9]{2})_([0-9]{5})\.wav$')

    for file in files:
        match = pattern.match(file)
        if match:
            bird_id, day, serial_number = match.groups()

            # Create a folder for the bird ID if it doesn't exist
            bird_dir = os.path.join(dest_dir, bird_id)
            if not os.path.exists(bird_dir):
                os.makedirs(bird_dir)

            # Create a subdirectory for the day if it doesn't exist
            day_dir = os.path.join(bird_dir, day)
            if not os.path.exists(day_dir):
                os.makedirs(day_dir)

            # Copy the file to the appropriate subdirectory
            src_file_path = os.path.join(src_dir, file)
            dest_file_path = os.path.join(day_dir, file)
            shutil.copy(src_file_path, dest_file_path)
            print(f'Copied {file} to {dest_file_path}')


def get_directory_path(title):
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title=title)
    return folder_path


def main():
    print("Welcome to the File Organizer!")
    print(
        "This script will organize files in a source directory into subdirectories based on a specified naming format.")

    # Get source directory path using dialog box
    source_directory = get_directory_path("Select Source Directory")
    if not source_directory:
        print("Source directory selection canceled. Exiting...")
        return

    # Get destination directory path using dialog box
    destination_directory = get_directory_path("Select Destination Directory")
    if not destination_directory:
        print("Destination directory selection canceled. Exiting...")
        return

    # Call the function to organize files
    organize_files(source_directory, destination_directory)
    print("File organization completed successfully!")


if __name__ == "__main__":
    main()
