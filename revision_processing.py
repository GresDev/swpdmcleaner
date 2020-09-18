import os
import shutil
from folder_processing import *


def get_revision_folders(path):
    folders = []
    for root in os.walk(path):
        for folder in root:
            for file in folder:
                if file == 'revisions.pdmw':
                    folders.append(root[0])
    return folders


def update_revision(path):
    file_name = path + '\\revisions.pdmw'
    file_content_new = []

    with open(file_name, mode='r', encoding='utf16') as revisions:

        file_content = revisions.readlines()

        if len(file_content) < 3:
            return [0, 0]

        folders_to_delete = get_folders_to_delete(file_content, path)

        folders_to_delete_params = get_folders_to_delete_params(folders_to_delete)

        total_folder_to_delete_size = folders_to_delete_params[0]
        total_folder_to_delete_files = folders_to_delete_params[1]


        for folder in folders_to_delete:
            try:
                shutil.rmtree(folder)
            except IOError as message:
                print(f'Error occured while deleting : {message} {folder}')


        index = file_content[0].find(f'\t')

        if index > 0:
            first_string = '#D1' + file_content[0][index:]

        file_content_new.append(first_string)

        count = len(file_content) - 1

        while count > 0:
            if len(file_content[count]) > 20:
                file_content_new.append(file_content[count])
                break
            count -= 1

    with open(file_name, mode='w', encoding='utf16') as revisions_updated:
        revisions_updated.writelines(file_content_new)

    return [total_folder_to_delete_size, total_folder_to_delete_files]


def get_folders_to_delete(file_content, path):
    result = []
    i =1
    while i < len(file_content) - 1:
        index = file_content[i].find(f'\t')
        folder_to_delete = path + '\\' + file_content[i][:index]
        result.append(folder_to_delete)
        i += 1
    return result


def get_folders_to_delete_params(folder_list):

    total_size =0
    total_files =0

    for folder in folder_list:
        folder_params = get_folder_params(folder)
        total_size += folder_params[0]
        total_files += folder_params[1]

    return [total_size, total_files]
