import os


def list_file_hard_drive():
    directory = '/home/hatrang/Desktop/bt'
    list_files = []
    for path, subdir, files in os.walk(directory):
        print(path)
        for x in files:
            list_files.append(path + '/' + x)
    return list_files
