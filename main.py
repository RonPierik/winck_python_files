__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile
from pickle import TRUE

def clean_cache():
    my_cwd = os.getcwd()
    my_cwd += "\\files"
    if "data.zip" in os.listdir(my_cwd):
        if "cache" not in os.listdir(my_cwd):
            os.makedirs(my_cwd + '\\cache')
            ret_val = True
        else:
            my_cwd += "\\cache"
            for file in os.scandir(my_cwd):
                 os.remove(file.path)
            ret_val = True
    else:
        ret_vcached_fal = False

    return(ret_val)

def cache_zip(my_zipfile_path, my_cache_path):
    # Create a ZipFile Object and load sample.zip in it
    with ZipFile(my_zipfile_path, 'r') as zipObj:
        # Extract all the contents of zip file in different directory
        zipObj.extractall(my_cache_path)

    return

def cached_files():
    file_list = []
    cache_path = 'files/cache'
    cache_path = os.path.abspath(cache_path)
    for file in os.listdir(cache_path):
        file_path = cache_path + "\\" + file
        file_list.append(file_path)
    
    return(file_list)


def find_password(file_list):
    for file in file_list:
        with open(file) as f:
            for line in f:
                if "password: " in line:
                    password = line.replace("password: ", "")
                    password = password.replace("\n", "")
                    break

    return(str(password))

print(find_password(cached_files()))
