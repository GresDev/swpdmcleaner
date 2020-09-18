import locale
import sys
from obsolete_processing import *
from revision_processing import *
import colorama
from colorama import Fore, Back, Style

colorama.init()



locale.setlocale(locale.LC_ALL, '')

print(100*'-')
print(Fore.YELLOW + 'Before proceeding, make sure that you have backed up the target folder!' + Fore.RESET)
print(100*'-')

vault_folder = input('\nPlease, enter path to SolidWorks Workgroup PDM directory: ')

# os.chdir("f:/testvault")

if not check_for_vault_folder(vault_folder):
    print('There is no SolidWorks Workgroup PDM data on specified path!')
    print('Exiting...')
    sys.exit()

question = input('Are you sure that you clearly understand what exactly you are going to do? (type Yes/No): ')

if question != 'Yes':
    print('Good choice!')
    print('Exiting...')
    sys.exit()

print(Fore.YELLOW + 'You have chosen to delete redundant file revisions from the SolidWorks Workgroup PDM folder.' +
      Fore.RESET)

os.chdir(vault_folder)

# clean all obsolete folders
print(100*'-')
obsolete_folders = get_obsolete_folders(os.getcwd(), 'obsolete')

total_obsolete_params = get_folderset_params(obsolete_folders)


print(Fore.LIGHTBLUE_EX + 'Obsolete folders processing:' + Fore.RESET)

if total_obsolete_params[0] > 0:
    try:
        print(f'Total size of obsolete folders: ' + locale.format_string('%d',
                                                                         total_obsolete_params[0],
                                                                         grouping=True) + ' bytes in ' +
              locale.format_string(
            '%d', total_obsolete_params[1],
            grouping=True) + ' files.')

        obsolete_clean(obsolete_folders, False)
        print('Obsolete folders cleaned up.')
    except:
        print('Unknown error occured while cleaning up obsolete folders.')
else:
    print('Nothing to clean!')

print(100*'-')

# clean all obsolete revisions
print(Fore.LIGHTBLUE_EX + 'Redundant revisions processing:' + Fore.RESET)

revision_folders = get_revision_folders(os.getcwd())

# update_revision(revision_folders[2])
total_revision_files_size = 0
total_revision_files_count = 0

for folder in revision_folders:
    total_revision_files_params = update_revision(folder)
    total_revision_files_size += total_revision_files_params[0]
    total_revision_files_count += total_revision_files_params[1]

if total_revision_files_size > 0:
    print(f'Total size of redundant revision files: ' + locale.format_string('%d', total_revision_files_size,
                               grouping=True) + ' bytes in ' + locale.format_string('%d', total_revision_files_count,
                               grouping=True) + ' files.')
    print('Redundant revision files deleted')
else:
    print('There is no redundant revisions. Nothing to delete!')

print(100*'-')

input('\nPress Enter to exit...')