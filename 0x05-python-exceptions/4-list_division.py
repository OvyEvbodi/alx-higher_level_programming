#!/usr/bin/python3

'''
list_division - divides element by element 2 lists

ARGS:
my_list_1: the first list
my_list_2: the second list
list_length: the number of elements to divide
'''


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        finally:
            new_list.append(result)
    return new_list
