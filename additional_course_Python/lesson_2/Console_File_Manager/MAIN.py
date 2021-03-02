from Core import to_create_file, to_create_folder, get_list, to_delete, to_copy, save_info, change_dir
import sys
from practical_task_6_2 import game_reverse

save_info('Start')
try:
    command = sys.argv[1]
except IndexError:
    print('You must select the command. for information enter "help".')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('enter the file name')
        else:
            to_create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('enter the folder name')
        else:
            to_create_file(name)
    elif command == 'ch':
        try:
            name = sys.argv[2]
        except IndexError:
            print('enter the folder name')
        except FileNotFoundError:
            print("you entered a folder name that doesn't exist")
        else:
            change_dir(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('enter the file/folder name')
        else:
            to_delete(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('enter the name folder and name new folder')
        else:
            to_copy(name, new_name)
    elif command == 'help':
        print('list - list of files and folders')
        print('create file - creating a file')
        print('create_folder - creating a folder')
        print('delete - delete file or folder')
        print('copy - copy file or folder')
        print('ch - change folder')
        print('game - if you want to play')
    elif command == 'game':
        game_reverse()

save_info('The End')
