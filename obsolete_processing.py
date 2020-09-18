import os
import shutil

import colorama
from colorama import Fore, Back, Style

colorama.init()


def get_obsolete_folders(path, search_pattern):
    folders = []
    for root in os.walk(path):
        if root[0].endswith(search_pattern):
            folders.append(root[0])
    return folders


def obsolete_clean(folders, verbose):
    for folder in folders:
        if folder.endswith('obsolete'):
            try:
                shutil.rmtree(folder)
                os.mkdir(folder)

                if verbose:
                    print(f'Cleaning up completed: {folder}')

            except FileNotFoundError:
                pass
            except IOError as message2:
                print(Fore.RED + f'Error occured while cleaning up: {message2} {folder}' + Fore.RESET)

