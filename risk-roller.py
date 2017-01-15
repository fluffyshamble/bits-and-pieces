import random as rd

def roll_dice(attack_dice, defence_dice):
    for i in range (0, 2):
        attack_dice[i] = rd.randint(1, 6)
        defence_dice[i] = rd.randint(1, 6)


def compare_dice():
