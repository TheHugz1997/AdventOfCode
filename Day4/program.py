import re
with open('Day4/pairs.txt') as f:
    lines = f.readlines()
    liste = []
    doublons = 0
    for j in lines:
        res = re.split('-|,', j.split('\n')[0])
        liste.append(res)
    for k in liste:
        # premier cas a-b contient c-d
        if int(k[0]) <= int(k[2]) and int(k[1]) >= int(k[3]):
            doublons += 1

        # deuxième cas a-b contenu dans c-d
        elif int(k[0]) >= int(k[2]) and int(k[1]) <= int(k[3]):
            doublons += 1

    print(doublons)