"""
@author        Shuo Qiu
@date          2021/10/25
@describe
"""


def within():
    while True:  # Loop
        lst = input()  # Input guess range.
        lst_result = [0, 0]  # Create a list in order to store the final result.
        try:
            lst_temp = lst.split(',')  # Splits a string into a list of two elements.
        except ValueError:  # Print error and continue when go wrong.
            print('Input format error, it should be two integers are separated by a comma (e.g. “1,100”), please try '
                  'again.')
            continue
        if len(lst_temp) != 2:  # If the number of elements in the list not equal to 2, continue.
            print('The range should have two numbers, please try again.')
            continue
        else:
            try:
                el1 = int(lst_temp[0])  # Str to int.
                el2 = int(lst_temp[1])
            except ValueError:  # Print error and continue when go wrong.
                print('The type of elements in the list should be int, please try again.')
                continue
            lst_result[0] = el1  # Update the information of lst_result.
            lst_result[1] = el2
        if lst_result[0] >= lst_result[1]:  # If the lower range greater than the upper range, continue.
            print('The second number should be greater than the first one, please try again.')
            continue
        elif lst_result[1] - lst_result[0] > 1000:  # If the range greater than 1000, try again in order to ensure
            # the game experience (This is a personal additional function).
            print('The range is too huge, please try again to ensure the game experience.')
            continue
        else:
            return lst_result  # If all criteria are met, return lst_result.


def game(lst):  # Dichotomy to get the target number.
    range_min = lst[0]  # Get the first element in the list.
    range_max = lst[1]
    count = 0  # Create a pedometer.

    print(f'Think of a number between {range_min} and {range_max}!')

    while True:  # Loop
        range_avg = (range_max + range_min) // 2  # Calculate the middle value of the range, rounded down.
        result = input(f'Is your number greater (>), equal (=), or less (<) than {range_avg}?\n'
                       f'Please answer <,=, or >!')
        if result == '>':  # If the target value greater than the middle value.
            range_min = range_avg + 1  # The lower range equal to the middle value plus one.
            count += 1  # Step plus one.
        elif result == '<':  # If the target value less than the middle value.
            range_max = range_avg - 1  # The upper range equal to the middle value minus one.
            count += 1  # Step plus one.
        elif result == '=':  # If the target value equal to the middle value.
            print('I have guessed it!')
            count += 1  # Step plus one.
            break  # Jump out of the while loop.
        else:  # If the input information isn't '>','<' or '<', continue.
            print('The information you entered is incorrect, please answer again.')
            continue

        if range_min > range_max:  # If the lower range greater than the upper value, it mean there is no
            # target value, the player is lying.
            print('You are lying.')
            break  # Jump out of the while loop.

    return count


def main():  # Program entry.
    print('Please give me a range, it should be two integers are separated by a comma (e.g. “1,100”).')
    lst_result = within()  # Execute within function to get the range of the guess.
    count = str(game(lst_result))  # Execute game function and convert the return value to a string.
    print(f'I needed {count} steps!')  # Print the number of steps.


main()  # Execute main function.
