alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
with open('Day3/puzzle.txt') as f:
    lines = f.readlines()
    somme = 0
    group_list = []
    i = 0
    while i < len(lines):
        group = []
        group.append(lines[i].split('\n')[0])
        group.append(lines[i+1].split('\n')[0])
        group.append(lines[i+2].split('\n')[0])
        group_list.append(group)
        i += 3
    for item in group_list:
        first = item[0]
        second = item[1]
        third = item [2]
        got_it = 0
        for letter in first:
            if letter in second and letter in third and letter in alphabet and got_it == 0:
                somme += alphabet.index(letter) + 1
                got_it = 1
            elif letter in second and letter in third and got_it == 0:
                somme += alphabet.index(letter.lower()) + 27
                got_it = 1
    print(somme)
    