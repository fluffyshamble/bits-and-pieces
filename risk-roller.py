import random as rd

def roll_dice(attack_army, defence_army):
    # roll dice
    attack_dice, defence_dice = []
    for i in range (0, 2):
        attack_dice[i] = rd.randint(1, 6)
        defence_dice[i] = rd.randint(1, 6)
    att_sorted = sorted(attack_dice)
    def_sorted = sorted(defence_dice)

    for i in range(0, 2):
        if def_sorted[i] >= att_sorted[i]:
            attack_army -= 1
        else:
            defence_army -= 1

# read in attack and defence armies



