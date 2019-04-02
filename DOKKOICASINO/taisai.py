def judge_game(sai, your_ex):	# your_ex=[position, value, bet]
    winrate = 0
    if ((your_ex[0] == "big" and sai[0]+sai[1]+sai[2] >=11) or (your_ex[0] == "small" and sai[0]+sai[1]+sai[2] <=10)) and (not (sai[0]==sai[1] and sai[1]==sai[2] and sai[2] == sai[0])):
        winrate = 2

    elif your_ex[0] == "in" and your_ex[1] in sai:
        winrate = sai.count(your_ex[1])+1

    elif your_ex[0] == "sum" and sai[0]+sai[1]+sai[2] == your_ex[1]:
        if 9<=your_ex[1]<=12:
            winrate = 7
        elif your_ex[1] == 8 or your_ex[1] == 13:
            winrate = 9
        elif your_ex[1] == 7 or your_ex[1] == 14:
            winrate = 13
        elif your_ex[1] == 6 or your_ex[1] == 15:
            winrate = 18
        elif your_ex[1] == 5 or your_ex[1] == 16:
            winrate = 32
        elif your_ex[1] == 4 or your_ex[1] == 17:
            winrate = 64

    elif your_ex[0] == "combi":
        num1 = your_ex[1]//10
        num2 = your_ex[1]%10
        if (num1 in sai) and (num2 in sai):
            winrate = 6

    elif your_ex[0] == "double" and sai.count(your_ex[1])>=2:
        winrate = 8

    elif your_ex[0] == "anytriple" and sai[0]==sai[1] and sai[1]==sai[2] and sai[2] == sai[0]:
        winrate = 24

    elif your_ex[0] == "triple" and sai.count(your_ex[1])==3:
        winrate = 126

    return your_ex[2]*(winrate-1)
