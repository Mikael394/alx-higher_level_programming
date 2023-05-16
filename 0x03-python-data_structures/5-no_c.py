#!/usr/bin/python3
def no_c(my_string):
    l = list(my_string)
    for x in l:
        if x == 'c':
            l.remove('c')
        elif x == 'C':
            l.remove('C')
    my_string = "".join(l)
    return my_string
