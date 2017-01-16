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



    for i in range (0, len(attack_dice) - 1):
        attack_dice[i] = rd.randint(1, 6)
    for i in range (0, len(defence_dice) - 1):
        defence_dice[i] = rd.randint(1, 6)
    att_sorted = sorted(attack_dice)
    def_sorted = sorted(defence_dice)
    print "Attack scores: %s, " \
          "defence scores: %s" % (att_sorted, def_sorted)

    for i in range(0, 2):
        if def_sorted[i] >= att_sorted[i]:
            attack_army -= 1
        else:
            defence_army -= 1

roll_dice(5, 5)



