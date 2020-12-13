import os
from pprint import pprint

import reusables

import create_filesystem

# reusables.find_files(ext=reusables.exts)
disk_files = reusables.find_files_list('./Data', ext=('.py', '.java'), abspath=True, disable_pathlib=True)


# print(len(file_list))

def get_all_path(json, p):
    if not isinstance(json, dict):
        return

    if len(json) == 0:
        return

    if 'path' in json.keys():  # and json['path'] != ''
        p.append(json['path'])

    for v in json.values():
        get_all_path(v, p)

    if 'sub_questions' in json.keys():
        for v in json['sub_questions']:
            get_all_path(v, p)


config_files = []
# print(create_filesystem.get_data())
# print(type(create_filesystem.get_data()))
get_all_path(create_filesystem.get_data(), config_files)
# pprint(disk_files[:10])
# pprint(config_files[:10])
# config_files = set(config_files)

pprint(len(set(disk_files) - set(config_files)))
for file in disk_files:
    if str(file) not in config_files:  # if config file is no longer in disk file then remove
        print('removed', file)
        os.remove(file)
    # break
