# write a program that reads the contents of the Food_Establishment_Violations
# for the City of Evanston and counts the number of violations that have occurred
# for each restaurant code. The, print out the restaurant code and the number of violations

# VS Code Hack:
import sys
import os
dir_path = os.path.dirname(sys.argv[0])
file_path = os.path.join(dir_path, 'data', 'Trees_data.csv')
# End VS Code Hack:

def sort_dictionary(d:dict):
    '''
    Helper function to sort a dictionary
    '''
    import collections
    return collections.OrderedDict(
        sorted(d.items(), key=lambda kv: -1 * kv[1])
    )


f = open(file_path, 'r', encoding='utf8', errors='ignore')
lines = f.readlines()

# let's print all of the column headers:
header = lines[0]
cells = header.split(',')
i = 0
for cell in cells:
    print(i, '->', cell)
    i += 1

types_of_trees = {}
for line in lines:
    cells = line.split(',')
    common_name = cells[39].replace('"', '').lower()
    condition = cells[16].replace('\n', '').lower()
    if common_name in types_of_trees:
        # add one to existing entry:
        types_of_trees[common_name] += 1
    else:
        # add new entry to the dictionary:
        types_of_trees[common_name] = 1

types_of_trees_sorted = sort_dictionary(types_of_trees)
for key in types_of_trees_sorted:
    print(types_of_trees_sorted[key], '\t', key)