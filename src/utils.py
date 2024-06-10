import os
import shutil


def clear_folder(folder_path):
    """
    Delete all files in a folder
    :param folder_path: The folder to be cleared
    """
    # Iterate through each file in the folder and delete it
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)


def cleanup_folders(folder_list):
    """
    Delete given folders
    :param folder_list: The folders to be deleted
    """
    # Iterate through each folder in the input and delete it
    for folder in folder_list:
        if os.path.exists(folder):
            shutil.rmtree(folder)
