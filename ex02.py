"""
@author        Shuo Qiu
@date          2021/10/25
"""


def within():
    while True:
        lst = input()
        lst_result = [0, 0]
        try:
            lst_temp = lst.split(',')
        except ValueError:
            print('Input format error, it should be two integers are separated by a comma (e.g. “1,100”), please try '
                  'again.')
            continue
        if len(lst_temp) != 2:
            print('The range should have two numbers, please try again.')
            continue
        else:
            try:
                el1 = int(lst_temp[0])
                el2 = int(lst_temp[1])
            except ValueError:
                print('The type of elements in the list should be int, please try again.')
                continue
            lst_result[0] = el1
            lst_result[1] = el2
        if lst_result[0] >= lst_result[1]:
            print('The second number should be greater than the first one, please try again.')
            continue
        elif lst_result[1] - lst_result[0] > 1000:
            print('The range is too huge, please try again to ensure the game experience.')
            continue
        else:
            return lst_result


def game(lst):
    range_min = lst[0]
    range_max = lst[1]

    print(f'Think of a number between {range_min} and {range_max}!')

    # range_min -= 1
    # range_max += 1

    done = False
    while not done:
        range_avg = (range_max + range_min) // 2
        result = input(f'Is your number greater (>), equal (=), or less (<) than {range_avg}?\n'
                       f'Please answer <,=, or >!')
        if result == '>':
            range_min = range_avg + 1
        elif result == '<':
            range_max = range_avg - 1
        elif result == '=':
            print('I have guessed it!')
            done = True
        else:
            print('The information you entered is incorrect, please answer again.')
            continue
        if range_avg == range_max or range_avg == range_min:
            print('You are lying, please answer again.')
            continue


def main():
    print('Please give me a range, it should be two integers are separated by a comma (e.g. “1,100”).')
    lst_result = within()
    game(lst_result)


main()
