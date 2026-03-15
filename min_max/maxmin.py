
import random


def maxmin(lst):
    if all([isinstance(num, int) for num in lst]):
        # using first element rather than setting to zero in case of all negative element list
        max_num = lst[0]
        min_num = lst[0]

        for num in lst:
            if num >= max_num:
                max_num = num

            if num <= min_num:
                min_num = num

        return [min_num, max_num]

    else:
        raise Exception("Invalid list. Ensure all elements are type int")


def get_prompt():
    while True:
        user_prompt = input("Enter a list of numbers (separate by spaces): ")
        try:
            return [int(num) for num in user_prompt.split()]
        except:
            print("Invalid entry. Ensure all elements are type int")


print(maxmin(get_prompt()))
