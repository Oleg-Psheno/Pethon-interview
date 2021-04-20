import os


def get_file_name(file):
    path = os.path.abspath(file)
    name = os.path.basename(path)
    return name.split('.')[:-1]


if __name__ == '__main__':
    print(get_file_name('task1.py'))
