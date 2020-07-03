if __name__ == '__main__':
    food = ['rice', 'beans']
    food.append('broccoli')

    food.extend(['bread', 'pizza'])

    print(food[:2])

    print(food[-1])

    breakfast_string = 'eggs,fruit,orange juice'
    breakfast = breakfast_string.split(',')

    len(breakfast)

    floating_point_list = []
    while True:
        inp = input('Enter a floating-point number: ')
        if inp == 'stop':
            break
        value = float(inp)
        floating_point_list.append(value)

    avg_value = sum(floating_point_list) / len(floating_point_list)
    min_value = min(floating_point_list)
    max_value = max(floating_point_list)
    print(f'Average: {avg_value}, min: {min_value}, max: {max_value}')
