# Importing the os module
import os

# Get the current directory path
current_dir = os.getcwd()

# List all items (files and directories) in the current directory
all_items = os.listdir(current_dir)

# Start an empty list to store information about files
file_info_list = []

# Loop through the items in the current directory
for item in all_items:
    # Get full path for each item
    full_path = os.path.join(current_dir, item)

    # Check if the item is a file (not a directory)
    if os.path.isfile(full_path):
        # Create a dictionary with the file's path and size
        file_info = {
            'file_path': full_path,
            'file_size': os.path.getsize(full_path)
        }

        # Add file info to the list
        file_info_list.append(file_info)

# Print each file's info
for info in file_info_list:
    print(info)


