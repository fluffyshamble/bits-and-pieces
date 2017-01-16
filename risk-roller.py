import random as rd


def roll_dice(attack_army, defence_army):
    # roll dice
    if attack_army > 3:
        attack_dice = [None] * 3
    elif attack_army == 3:
        attack_dice = [None] *2
    elif attack_army == 2:
        attack_dice = [None]
    else:
        print "You can't attack, invalid number of armies!"

    if defence_army >= 3:
        defence_dice = [None] * 3
    elif defence_army == 2:
        defence_dice = [None] * 2
    elif defence_army == 1:
        defence_dice = [None]
    else:
        print "Invalid number of defence armies!"

    for i in range (0, len(attack_dice)):
        attack_dice[i] = rd.randint(1, 6)
    for i in range (0, len(defence_dice)):
        defence_dice[i] = rd.randint(1, 6)
    att_sorted = sorted(attack_dice, reverse=True)
    def_sorted = sorted(defence_dice, reverse=True)
    print "Attack scores: %s, " \
          "defence scores: %s" % (att_sorted, def_sorted)

    while attack_army > 0 or defence_army >= 0:
        if attack_army > defence_army:
            compare_length = len(defence_dice)
        else:
            compare_length = len(attack_dice)
        for i in range(0, compare_length):
            if def_sorted[i] >= att_sorted[i]:
                attack_army -= 1
            else:
                defence_army -= 1
    if attack_army > defence_army:
        print "Attacker wins!"
    else:
        print "Defender wins!"


roll_dice(2, 5)



