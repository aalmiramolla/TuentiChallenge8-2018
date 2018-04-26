#!/usr/bin/env python
# coding: utf-8

def how_many_squares(line):
    n,m = line.split()
    return ((int(n)-1)*(int(m)-1))

if __name__=='__main__':
    test_or_submit = 'submit'
    with open('challenge1/'+test_or_submit+'Input') as f:
        lines = f.readlines()
        c = map(how_many_squares, lines[1:])
        with open('challenge1/'+test_or_submit+'Output', 'w') as r:
            for idx, value in enumerate(c):
                  r.write('Case #{}: {}\n'.format(idx+1,value))
