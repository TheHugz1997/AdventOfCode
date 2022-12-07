alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
with open('Day3/puzzle.txt') as f:
    lines = f.readlines()
    somme = 0
    for j in lines:
        j = j.split('\n')[0]
        first_item = j[0:len(j)//2]
        second_item = j[len(j)//2:]
        got_it = 0
        for letter in first_item:
            if letter in second_item and letter in alphabet and got_it == 0:
                somme += alphabet.index(letter) + 1
                got_it = 1
            elif letter in second_item and got_it == 0:
                somme += alphabet.index(letter.lower()) + 27
                got_it = 1
    print(somme)



