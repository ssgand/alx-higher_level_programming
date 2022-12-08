#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}
    sum = 0
    y = []
    for k in roman_string:
        y.append(k)
    if len(y) == 1:
        sum += roman_dict[y[0]]
    else:
        for i in range(len(y)):
            if i == 0:
                sum += roman_dict[y[i]]
                continue
            elif roman_dict[y[i]] <= roman_dict[y[i - 1]]:
                sum += roman_dict[y[i]]
            else:
                sum += roman_dict[y[i]] - (roman_dict[y[i - 1]] * 2)
    return sum
