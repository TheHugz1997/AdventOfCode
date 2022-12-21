with open('Day6/text.txt') as f:
    line = f.readline()
    print(line)
    number = 0
    marker = []
    for character in line:
        if len(marker) == 14:
            marker = []
            break
        else:
            if not marker:
                marker.append(character)
            elif character in marker:
                element_index = marker.index(character)
                marker = marker[element_index+1:]
                marker.append(character)
            elif character not in marker and len(marker) < 14:
                marker.append(character)
        print("this is marker : {}".format(marker))
        number += 1
    print(number)