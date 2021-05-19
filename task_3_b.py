def first_repeating_element(symbols):
    x = 0
    y = 0
    for i in symbols:
        x = x + 1
        for j in symbols[x:]:
            if i == j:
                print(f'first_repeating_element - {i}')
                y = 1
                break
        if y == 1:
            break
    if y == 0:
        print('no match')


a = input('Enter the symbols, separated by a space:').split(" ")
a = list(a)

first_repeating_element(a)
