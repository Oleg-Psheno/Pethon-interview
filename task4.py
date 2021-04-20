import string
import random
import os


def random_word():
    len = random.randint(3, 10)
    word = ''.join([random.choice(string.ascii_letters) for _ in range(len)])
    return word


def read_file(name):
    with open(name, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        for el in lines:
            print(el)


def create_file(name):
    if os.path.exists(name):
        print(f'Файл c именем  {name} существует')
    with open(name, 'w', encoding='UTF-8') as file:
        list1 = [random.randint(1, 1000) for _ in range(100)]
        list12 = [random_word() for _ in range(100)]
        zip_list = zip(list1, list12)
        for el in zip_list:
            file.write(str(el[0]) + ' : ' + el[1] + '\n')
    read_file(name)


if __name__ == '__main__':
    create_file('test.txt')
