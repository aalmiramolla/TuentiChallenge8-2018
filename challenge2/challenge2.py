#!/usr/bin/env python3
# coding: utf-8

max_number = 'PONMLKJIHGFEDCBA9876543210'
min_mumber = '1023456789ABCDEFGHIJKLMNOP'

def difference(line):
    base = len(line)-1

    _max_number = max_number[-base:]
    _min_number = min_mumber[:base]

    decimal_max_number = int(_max_number, base)
    decimal_min_number = int(_min_number, base)

    return decimal_max_number - decimal_min_number


if __name__=='__main__':
    test_or_submit = 'submit'
    with open(test_or_submit+'Input') as f:
        lines = f.readlines()
        c = map(difference, lines[1:])
        with open(test_or_submit+'Output', 'w') as r:
            for idx, value in enumerate(c):
                r.write('Case #{}: {}\n'.format(idx+1,value))
