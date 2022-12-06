with open('Day1/number.txt') as f:
    lines = f.readlines()
    elf = []
    somme = 0
    for j in lines:
        if j == "\n":
            elf.append(somme)
            somme = 0
        else:
            somme += int(j.split('\n')[0])
    new_elf_list = []
    number = 0
    for i in range(3):
        number = max(elf)
        new_elf_list.append(int(number))
        elf.remove(number)
    total = sum(new_elf_list)
    print(total)