def multiplication(a,b):
    for x in range(1,a+1):
        for y in range(1,b+1):
            print(f'{x} * {y} = {x*y}')

if __name__ == '__main__':
    multiplication(3,4)