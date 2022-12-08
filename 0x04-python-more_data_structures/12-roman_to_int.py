#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    y = []
    for i, j in roman_dict.items():
            for k in roman_string:
                if i == k:
                    y.append(i)
    for i in range(len(y)):
        sum += roman_dict[y[i]]
       #if roman_dict[y[i] > roman_dict[y[i - 1]]:
        #sum += roman_dict[y[i]] - roman_dict[y[i - 1]]
    return sum
