# the function for creation the file

def to_create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as fp:
        if text:
            fp.write(text)


# the function for creation the folder
import os


def to_create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('This folder already exists')


# the function fuck knows what it is
def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


# the function to delete folder and file
def to_delete(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


import shutil


# the function to copy folder and file
def to_copy(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('This folder already exists')
    else:
        shutil.copy(name, new_name)


import datetime


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time}-{message}'
    with open('log.txt', 'a', encoding='utf-8') as fp:
        fp.write(result + '\n')
    # print(result)


def change_dir(name):
    os.chdir(name)
    print(os.getcwd())


if __name__ == '__main__':
    to_create_file('file_for_function_to_create_file.txt', 'an unknown shit')
    to_create_folder('folder_for_function_to_create_folder')
    get_list()
    get_list(True)
    to_copy('folder_for_function_to_create_folder', 'qwerty')
    to_delete('qwerty')
    save_info('testing...')
