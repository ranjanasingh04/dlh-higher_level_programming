#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    seen = []

    for item in my_list:
        if item not in seen:
            sum += item
            seen.append(item)
    return sum
