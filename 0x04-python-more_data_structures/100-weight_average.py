#!/usr/bin/python3
def weight_average(my_list=[]):
    product = 0
    sum = 0
    if my_list == []:
        return 0
    else:
        for i, j in my_list:
            product += i * j
            sum += j
        return product/sum
