import json

# Manual Coverage Tool

# Branches covered dictionary
branches_covered = dict()

# Functions -> Number of branches
func_branches = {
        'polydiv': 4,
        'polyder': 5,
        'polyint': 9,
        'matrix_power': 11,
        'multi_dot': 9
}

# intialy set flags to 'False'
for func, nr_branches in func_branches.items():
    branches_covered[func] = dict()
    for i in range(nr_branches):
        branches_covered[func][f'branch{i+1}'] = False
 
    

