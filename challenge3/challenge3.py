#!/usr/bin/env python3
# coding: utf-8
possible_keys='MA MA# MB MC MC# MD MD# ME MF MF# MG MG# mA mA# mB mC mC# mD mD# mE mF mF# mG mG#'.split()
piano='C;C#;D;D#;E;E#|F;F#;G;G#;A;A#;B;B#|C'.split(';')

def parse_note_2(note):
    # Ugly
    for p_note in piano:
        if note in p_note:
            return p_note

def parse_note(note):
    if 'b' in note:
        note_wo_b = parse_note_2(note[0])
        index = piano.index(note_wo_b)-1
        return piano[piano.index(note_wo_b)-1]
    return parse_note_2(note)

def get_scale(note, major_or_minor):
    note_parsed = parse_note(note)
    note_array = [note_parsed]
    scale = 'wwhwwwh' if major_or_minor == 'M' else 'whwwhww'
    for idx, jump in enumerate(scale):
        note_array.append(which_note_reach(note_array[idx], jump))
    return set(note_array)

def which_note_reach(note, whole_or_half):
    addition = 2 if whole_or_half == 'w' else 1
    index = (piano.index(note)+addition) % (len(piano) - 1)
    return piano[index]

def get_all_keys(song):
    solution = list(filter(lambda key: song.issubset(get_scale(key[1:], key[0])), possible_keys))
    if not solution:
        return 'None'
    else:    
        return ' '.join(solution)

if __name__=='__main__':
    test_or_submit = 'test'
    with open(test_or_submit+'Input') as f:
        with open(test_or_submit+'Output', 'w') as r:
            lines = f.readlines()[1:]
            line_notes = []
            for idx, line in enumerate(lines):
                try:
                    cases= int(line)
                    if cases == 0:
                        value = ' '.join(possible_keys)
                        r.write('Case #{}: {}\n'.format(idx,value))
                except ValueError:
                    for note in line.split():
                        line_notes.append(parse_note(note))
                    value = get_all_keys(set(line_notes))
                    r.write('Case #{}: {}\n'.format(idx,value))
