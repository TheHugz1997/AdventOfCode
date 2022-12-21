with open('Day6/text.txt') as f:
    line = f.readline()
    print(line)
    number = 0
    marker = []
    for character in line:
        if len(marker) == 4:
            marker = []
            break
        else:
            if not marker:
                marker.append(character)
            elif character in marker:
                marker = []
                marker.append(character)
            elif character not in marker and len(marker) < 4:
                marker.append(character)
        print("this is marker : {}".format(marker))
        number += 1
    print(number)