import os
import shutil


def clear_folder(folder_path):
    """
    Delete all files in a folder
    :param folder_path: The folder to be cleared
    :return: True if the folder is now empty
    """
    # Iterate through each file in the folder and delete it
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    return len(os.listdir(folder_path))


def cleanup_folders(folder_list):
    """
    Delete given folders
    :param folder_list: The folders to be deleted
    :return: True if all folders in folder_list have been deleted
    """
    # Iterate through each folder in the input and delete it
    for folder in folder_list:
        if os.path.exists(folder):
            shutil.rmtree(folder)

    # Iterate through each folder again, returning False if any still exists
    for folder in folder_list:
        if os.path.exists(folder):
            return False
    return True
