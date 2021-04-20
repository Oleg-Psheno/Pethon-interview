keys = ['1', 'two', 'tree', 'fous', 5, 6]
values = ['первое', 'второе', 'третье', 'четвертое', 'пятое', 6, 7, 8]


def get_dict(keys, values):
    result = {}
    for i, k in enumerate(keys):
        try:
            result[k] = values[i]
        except IndexError:
            result[k] = None
    return result


if __name__ == "__main__":
    print(get_dict(keys, values))
