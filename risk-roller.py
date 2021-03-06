import random as rd


def roll_dice(attack_dice, defence_dice):
    for j in range(0, len(attack_dice)):
        attack_dice[j] = rd.randint(1, 6)
    for j in range(0, len(defence_dice)):
        defence_dice[j] = rd.randint(1, 6)
    att_sorted = sorted(attack_dice, reverse=True)
    def_sorted = sorted(defence_dice, reverse=True)
    print "Attack scores: %s, " \
          "defence scores: %s" % (att_sorted, def_sorted)
    return att_sorted, def_sorted

attack_army = int(raw_input("How many attacking armies are there?\n"))
defence_army = int(raw_input("How many defending armies are there?\n"))

while attack_army > 1 and defence_army > 0:
    if attack_army > 3:
        attack_dice = [None] * 3
    elif attack_army == 3:
        attack_dice = [None] * 2
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

    att_sorted, def_sorted = roll_dice(attack_dice, defence_dice)

    if attack_army > defence_army:
        compare_length = len(def_sorted)
    else:
        compare_length = len(att_sorted)
    for i in range(0, compare_length):
        if def_sorted[i] >= att_sorted[i]:
            attack_army -= 1
            print "Attack army: %s" % attack_army
        else:
            defence_army -= 1
            print "Defence army: %s" % defence_army


if attack_army > defence_army:
    print "Attacker wins!"
else:
    print "\nDefender wins!\n"