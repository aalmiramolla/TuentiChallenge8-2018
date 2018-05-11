#!/usr/bin/env python3
# coding: utf-8
possible_keys='MA MA# MB MC MC# MD MD# ME MF MF# MG MG# mA mA# mB mC mC# mD mD# mE mF mF# mG mG#'.split()
piano='C;C#;D;D#;E;F;F#;G;G#;A;A#;B;C'.split(';')
translate_notes = {
    'E#': 'F',
    'B#': 'C',
    'Cb': 'B',
    'Db': 'C#',
    'Eb': 'D#',
    'Fb': 'E',
    'Gb': 'F#',
    'Ab': 'G#',
    'Bb': 'A#'
    }

def parse_note(note):
    if note in translate_notes.keys():
        return translate_notes.get(note)
    return note

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
    solution = list(filter(lambda key: 
                           song.issubset(get_scale(key[1:], key[0])),
                           possible_keys))
    return 'None' if not solution else ' '.join(solution)


def is_number_of_notes_or_notes(line):
    try:
        return int(line)
    except ValueError:
        return None
    return None

if __name__=='__main__':
    test_or_submit = 'submit'
    with open(test_or_submit+'Input') as f:
        with open(test_or_submit+'Output', 'w') as r:
            lines = f.readlines()[1:]
            counter = 1
            for line in lines:
                line_notes = []
                n_notes = is_number_of_notes_or_notes(line)
                if n_notes == 0:
                    value = ' '.join(possible_keys)
                    r.write('Case #{}: {}\n'.format(counter,value))
                    counter += 1
                elif not n_notes:
                    for note in line.split():
                        line_notes.append(parse_note(note))
                    line_notes = set(line_notes)
                    value = get_all_keys(line_notes)
                    r.write('Case #{}: {}\n'.format(counter,value))
                    counter += 1
