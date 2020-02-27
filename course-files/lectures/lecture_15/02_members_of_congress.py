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

lines = f.readlines()
for line in lines[0:10]:
    print(line)