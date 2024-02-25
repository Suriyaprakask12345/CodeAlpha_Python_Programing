import os
from shutil import move

# Path to the directory to be organized
download_folder = 'D:\dummy'

# File type categorization
file_types = {
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Compressed': ['.zip','.rar'],
    'software': ['.exe']
}

# Create subfolders if they don't exist
for folder in file_types.keys():
    folder_path = os.path.join(download_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files to their respective folders
for file in os.listdir(download_folder):
    file_path = os.path.join(download_folder, file)
    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if any(file.endswith(ext) for ext in extensions):
                dest_path = os.path.join(download_folder, folder, file)
                move(file_path, dest_path)
                break

print("Files organized successfully.")
