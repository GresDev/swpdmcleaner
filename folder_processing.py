import os


def get_folderset_params(folder_list):
    total_size = 0
    total_files = 0
    for folder in folder_list:
        result = get_folder_params(folder)
        total_size += result[0]
        total_files += result[1]
    return [total_size, total_files]


def get_folder_params(path):
    total_size = 0
    total_files = 0
    for folders, _, files in os.walk(path):
        for file in files:
            total_size += os.path.getsize(os.path.join(folders, file))
            total_files +=1
    return [total_size, total_files]


def check_for_vault_folder(path):
    if os.path.exists(path + '\\pdmrc') and os.path.exists(path + '\\projects') and os.path.exists(path + '\\data') and os.path.exists(path + '\\obsolete'):
        return True
    else:
        return False

