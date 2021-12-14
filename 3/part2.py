if __name__ == '__main__':
    with open('input') as f:
        lines = [[j for j in (i.strip('\n'))] for i in f.readlines()]

    # for i in lines:
    #     i[1] = int(i[1])
    in_arr = [0] * len(lines[0])

    first_bit = [int(i[0]) for i in lines]
    for i in lines:
        for index, bit in enumerate(i):
            num = int(bit)
            if num == 1:
                in_arr[index] += 1
            else:
                in_arr[index] -= 1
        print(in_arr)
    
    gamma = [0] * len(lines[0])
    for index, bit in enumerate(in_arr):
        if bit > 0:
            gamma[index] = 1
    
    # gamma = [0, 0, 1]

    print(f'Gamma: {gamma}')
    gamma_rate = 0
    epsilon_rate = 0


    for i , j in enumerate(gamma):
        power = 2**(len(gamma)-i-1)
        if j == 1: 
            gamma_rate += power
        else: 
            epsilon_rate += power
    print(f'Gamma: {gamma_rate}')
    print(f'Epsilon: {epsilon_rate}')
    print(f'Power Consumption: {gamma_rate * epsilon_rate}')

    print('first bits:')
    print(first_bit)

