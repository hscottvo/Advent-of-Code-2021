from enum import Enum


def add_coords(a, b):
    return [i + j for i, j in zip(a, b)]


if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    # lines = ['up 10']
    aim = 0
    coord = [0, 0]
    dirs = {'forward': [1, 0], 'down': [0, 1], 'up': [0, -1]}
    arr = [i.split() for i in lines]
    for i in arr:
        mag = int(i[1])
        # coord = add_coords([j * mag for j in dirs[i[0]]] , coord)
        # # print(dirs[i[0]])
        if i[0] == 'forward': 
            coord[0] += mag
            coord[1] += mag * aim            
        elif i[0] == 'down':
            aim += mag
        else:
            aim -= mag

    print(coord)
    print(coord[0] * coord[1])
    

    