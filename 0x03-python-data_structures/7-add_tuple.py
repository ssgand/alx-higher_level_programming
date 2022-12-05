#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    lst_a = []
    lst_b = []
    lst_c = []
    for i in tuple_a:
        lst_a.append(i)
    for i in tuple_b:
        lst_b.append(i)

    if len(lst_a) == len(lst_b):
        for i in range(len(lst_a)):
            lst_c.append(lst_a[i] + lst_b[i])
    


    #elif len(lst_a) > len(lst_b):
     #   for 






    #return lst_a 
