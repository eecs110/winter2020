# write a program that reads the contents of the Trees_data.csv file
# to find out the number of trees of each species...

# Next week: we're going to make a map of them!

# VS Code Hack:
import sys
import os
dir_path = os.path.dirname(sys.argv[0])
file_path = os.path.join(dir_path, 'data', 'Trees_data.csv')
# End VS Code Hack:

def sort_dictionary(d:dict):
    import collections
    return collections.OrderedDict(
        sorted(d.items(), key=lambda kv: -1 * kv[1])
    )


f = open(file_path, 'r', encoding='utf8', errors='ignore')
lines = f.readlines()

# print first 10 lines:
for line in lines[0:10]:
     print(line)