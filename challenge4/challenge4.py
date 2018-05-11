#!/usr/bin/env python
# coding: utf-8

def how_many_squares(line):
    n,m = line.split()
    return ((int(n)-1)*(int(m)-1))

if __name__=='__main__':
    test_or_submit = 'test'
    counter = 0
    current_counter = 0
    current_line=2
    with open(test_or_submit+'Input') as f:
        with open(test_or_submit+'Output', 'w') as r:
            lines = f.readlines()[1:]
            for idx, line in enumerate(lines):
                try:
                    n,m = line.split()
                    current_line = idx + 1
                    counter += 1
                    current_counter = counter
                    print('n {} m {} count {}'.format(n,m, counter))
                except ValueError:
                    if counter != current_counter:
                        print(lines[current_line:current_line+int(n)])
                        r.write('Case #{}: {}\n'.format(counter,''))
                    #print('is tabletop')
