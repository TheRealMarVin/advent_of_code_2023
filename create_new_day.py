import os
import shutil


def get_highest_day_number(folder_path):
    # Get a list of all directories in the specified folder
    all_folders = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]

    if not all_folders:
        return None  # No folders found

    # Extract numbers from folder names and filter out non-matching folders
    numbers = [int(folder.split('_')[1]) for folder in all_folders if folder.startswith('day_') and folder[4:].isdigit()]

    if not numbers:
        return None  # No matching folders found

    # Find the highest number
    highest_number = max(numbers)

    return highest_number


def copy_folder(source_folder, destination_folder):
    try:
        # Copy the entire contents of the source folder to the destination folder
        shutil.copytree(source_folder, destination_folder)
        print(f"Folder '{source_folder}' successfully copied to '{destination_folder}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def rename_files_with_pattern(folder_path, pattern, replacement):
    try:
        # List all files in the specified folder
        files = os.listdir(folder_path)

        for filename in files:
            # Check if the pattern is present in the filename
            if pattern in filename:
                # Create the new filename by replacing the pattern with an empty string
                new_filename = filename.replace(pattern, replacement)

                # Construct the full paths for the old and new filenames
                old_filepath = os.path.join(folder_path, filename)
                new_filepath = os.path.join(folder_path, new_filename)

                # Rename the file
                os.rename(old_filepath, new_filepath)

                print(f"File '{filename}' renamed to '{new_filename}'.")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    folder_path = "./"
    highest_number = get_highest_day_number(folder_path)

    if highest_number is not None:
        print(f"The highest number in folder names is: {highest_number}")

        source_path = "./day_template"
        fixed_length_string = str(highest_number + 1).zfill(2)
        destination_path = "./day_{}".format(fixed_length_string)

        copy_folder(source_path, destination_path)

        rename_files_with_pattern(destination_path, "XX", fixed_length_string)

    else:
        print("No matching folders found in the specified path.")


if __name__ == "__main__":
    print("Hello")
    main()
    print("Done")

