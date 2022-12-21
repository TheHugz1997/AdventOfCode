import re
# {1: '1', 5: '2', 9: '3', 13: '4', 17: '5', 21: '6', 25: '7', 29: '8', 33: '9'}
"""

['V', 'J', 'B', 'D']
['F', 'D', 'R', 'W', 'B', 'V', 'P']
['Q', 'W', 'C', 'D', 'L', 'F', 'G', 'R']
['B', 'D', 'N', 'L', 'M', 'P', 'J', 'W']
['Q', 'S', 'C', 'P', 'B', 'N', 'H']
['G', 'N', 'S', 'B', 'D', 'R']
['H', 'S', 'F', 'Q', 'M', 'P', 'B', 'Z']
['F', 'L', 'W']
['R', 'M', 'F', 'V', 'S']

['F', 'N', 'B', 'G', 'B']
['B', 'S', 'G', 'S']
['V', 'M', 'B', 'D', 'Z', 'W', 'R', 'D']
['R', 'W', 'M']
['F', 'P', 'V', 'W', 'Q']
['H', 'J', 'L', 'R', 'D', 'P', 'F', 'S', 'P', 'J', 'V', 'D', 'N', 'D', 'C', 'F', 'F']
['N', 'L']
['S']
['B', 'C', 'R', 'H', 'W', 'L', 'B', 'Q', 'M', 'Q', 'P']

"""

"""

move 1 from 4 to 1
move 2 from 4 to 8
move 5 from 9 to 6
move 1 from 1 to 3
move 5 from 8 to 3
move 1 from 1 to 5
move 4 from 3 to 6
move 14 from 6 to 2
move 5 from 4 to 5

"""

with open('Day5/crane.txt') as f:
    lines = f.readlines()
    stacks = []
    dico = {}
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Creation of an array of 9 arrays
    for i in range(9):
        stacks.append([])

    # Creation of a dictionnary to know the index of the numbers in the lines
    # and thus to know the index of the letters
    new_lines = re.split('', lines[8].split('\n')[0])
    new_lines = new_lines[1:-1]
    for item in range(len(new_lines)):
        if new_lines[item] != ' ':
            dico[item] = int(new_lines[item])
    
    # Filling the array of arrays with the input letters
    for l in range(8):
        new_lines = re.split('', lines[l].split('\n')[0])
        new_lines = new_lines[1:-1]
        for element in range(len(new_lines)):
            if new_lines[element] in alphabet:
                stacks[dico[element]-1].append(new_lines[element])
    
    for elements in range(len(stacks)):
        stacks[elements].reverse()
    
    print(stacks)

    for m in lines:
        if m[0] == 'm':
            m = re.findall(r'\d+', m)
            where_to_take = stacks[int(m[1])-1]
            where_to_add = stacks[int(m[2])-1]
            test = []
            for numbers in range(int(m[0])):
                if len(where_to_take) == 0:
                    pass
                else:        
                    items_to_move = where_to_take.pop()
                    test.append(items_to_move)

            test.reverse()
            for element in test:
                where_to_add.append(element)
                
            stacks[int(m[1])-1] = where_to_take
            stacks[int(m[2])-1] = where_to_add

    for elements in stacks:
        print(elements)