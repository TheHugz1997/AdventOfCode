"""
    (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won
"""
with open('Day2/rockpaperscissors.txt') as f:
    lines = f.readlines()
    values = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    """

    A = 1 # rock
    B = 2 # paper
    C = 3 # scissors
    X = 1 # rock
    Y = 2 # paper
    Z = 3 # scissors

    """
    player1 = 0
    player2 = 0
    liste = []
    for j in lines:
        response = (j.split('\n')[0]).split(' ')

        p1_resp = response[0]
        p2_resp = response[1]
        

        if values[p1_resp] == values[p2_resp]:
            player1 += values[p1_resp] + 3
            player2 += values[p2_resp] + 3

        else:
            if values[p1_resp] > values[p2_resp]:
                if values[p1_resp] == 2:
                    player1 += values[p1_resp] + 6
                    player2 += values[p2_resp] 
                else:
                    if values[p2_resp] == 1:
                        player1 += values[p1_resp]
                        player2 += values[p2_resp] + 6
                    else:
                        player1 += values[p1_resp] + 6
                        player2 += values[p2_resp] 

            else:
                if values[p2_resp] == 2:
                    player1 += values[p1_resp] 
                    player2 += values[p2_resp] + 6
                else:
                    if values[p1_resp] == 1:
                        player1 += values[p1_resp] + 6
                        player2 += values[p2_resp] 
                    else:
                        player1 += values[p1_resp] 
                        player2 += values[p2_resp] + 6

    print((player2, player1))


    