
def check_num_input(n):
    while True:
        try:
            return int(n)
        except:
            print('Введенное число не является int!')
            n = input('Повторите ввод или "Q" для выхода: ')
            if n == 'Q':
                exit('Программа завершена пользователем!')