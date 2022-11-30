#!/usr/bin/python3
de remove_char_at(c, n):
    if n < 0:
        return(c)
    return (c[:n] + c[n+1:])
