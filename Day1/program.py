with open('Day1/number.txt') as f:
    lines = f.readlines()
    elf = []
    sum = 0
    for j in lines:
        if j == "\n":
            elf.append(sum)
            sum = 0
        else:
            sum += int(j.split('\n')[0])
    print(max(elf))