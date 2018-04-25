#!/usr/bin/env python
# coding: utf-8

def how_many_squares(line):
    n,m = line.split()
    return ((int(n)-1)*(int(m)-1))

if __name__=='__main__':
    with open('challenge1/submitInput') as f:
        lines = f.readlines()
        c = map(how_many_squares, lines[1:])
        for idx, value in enumerate(c):
            print('Case #{}: {}'.format(idx+1,value))
