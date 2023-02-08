"""
задача RLE необязательная. Реализуйте RLE алгоритм: реализуйте модуль сжатия
и восстановления данных (где только буквы присутствуют для простоты).
например декодирование
"""

from random import randint

def main():
    str_coding = ''
    str_init = ''.join([chr(randint(97, 100)) for i in range(10)])
    print(f'Начальная строка:\t', str_init)
    str_list = list(str_init)
    get_str = ''
    counter = 0

    for i in range(len(str_list)):
        if str_list[i] == get_str:
            counter += 1
        else:
            str_coding += f'{counter}{get_str}' if counter > 1 else f'{get_str}'
            counter = 1
        get_str = str_list[i]
        if i == len(str_list) - 1:
            str_coding += f'{counter}{get_str}' if counter > 1 else f'{get_str}'

    print('RLE сжатие:\t\t\t', str_coding)

    str_extr = list(str_coding)
    str_encoding = ''
    idx = 0
    while idx < len(str_extr):
        get_str = str_extr[idx]
        if get_str.isdigit():
            str_encoding += ''.join(str_list[idx + 1] * int(get_str))
            idx += 2
        else:
            str_encoding += get_str
            idx += 1

    print('RLE расжатие:\t\t', str_encoding)

    print('Сравнение строк:', str_init == str_encoding)


main()