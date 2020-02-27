# How many representatives does each state have in the House?
import sys
import os
dir_path = os.path.dirname(sys.argv[0])
file_path = os.path.join(dir_path, 'data/legislators-current.csv')
# End VS Code Hack:
f = open(file_path, 'r', encoding='utf8', errors='ignore')

def sort_dictionary(d:dict):
    '''
    Helper function to sort a dictionary
    '''
    import collections
    return collections.OrderedDict(
        sorted(d.items(), key=lambda kv: -1 * kv[1])
    )

congress_representatives_by_state = {}
for line in f.readlines():
    cells = line.split(',')
    house_or_senate = cells[8]
    state = cells[9]
    if house_or_senate == 'rep':
        if congress_representatives_by_state.get(state) is None:
            congress_representatives_by_state[state] = 0
        congress_representatives_by_state[state] += 1

congress_representatives_by_state = sort_dictionary(congress_representatives_by_state)
for key in congress_representatives_by_state:
    print(key + ':', congress_representatives_by_state[key])


while True:
    try:
        state = input('Enter a state abbreviation (Q to quit): ')
        if state == 'Q':
            break
        print(state, 'has', congress_representatives_by_state[state], 'representatives.')
    except:
        print(state, 'not found. Please try again.')
    