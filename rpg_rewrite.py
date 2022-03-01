import random, pickle, os
# "random" is used for many things, mainly used in battles to determine if you've hit the enemy and for how much damage.
# "pickle" is used for saving and loading statistics/equipment from files.
# "os" is for finding the files that you save/load into/from.

class Character:
    def __init__(self, classname, lvl, exp, gold, hp, atkrange, defrange, hitchance):
        self.classname = classname  # Name of the character's class. 
        self.lvl = lvl              # Character's level, formula for a level up is: exp needed = (lvl * 27).
        self.exp = exp              # Experienced gained from battles, and used to get a level up.
        self.gold = gold            # Currency gained from battles (TODO add more forms of gaining money), used to buy things from the store (TODO).
        self.hp = hp                # Maximum Health Points of the character, used before battles to default your fight hp.
        self.atkrange = atkrange    # List containing a minimum and a maximum value of your damage.
        self.defrange = defrange    # List containing a minimum and a maximum value of your defense (value nullifies enemy damage 1:1).
        self.hitchance = hitchance  # Character's hitchance, default is 75 (TODO hitchance should be a weapon value, not the character one).



def characterChoice():  # Function for choosing a character.
    print('Choose your character class, use the letters put in brackets.')
    classinfo = '(B)ERSERKER (ATK = 4, DEF = 3, HP = 45)\n(P)ROTECTOR (ATK = 3, DEF = 4, HP = 60)'
    print(classinfo)
    # TODO Make the character list read from some file or something.
    while True:
        match input().lower(): # Switch case, setting a character class based on a letter put in brackets.
            case 'b':
                return Character('Berserker', 1, 0, 0, 45, (3, 4), (0, 0), 75)
            case 'p':
                return Character('Protector', 1, 0, 0, 60, (1, 2), (0, 2), 80)
            case _:
                print('Please input an available class letter:')
                print(classinfo)
    # TODO Add starting weapons for each class.


def badcharSpecifier(atkvalue, hpvalue, expvalue, ename, goldvalue, ehitchance):
    badchardict = {
    'eatk' : atkvalue,
    'ehp' : hpvalue,
    'expgain' : expvalue,
    'ename' : ename,
    'goldgain' : goldvalue,
    'ehitchance' : ehitchance
    }
    return badchardict


def badplayerChoice():
    print('Choose an enemy to fight: (or (E)XIT)')
    badcharinfochoice = '(R)at (ATK = 3, HP = 21, EXP = 5, GOLD = 2, Hitchance = 50)\n(G)oblin (ATK = 6, HP = 36, EXP = 10, GOLD = 5, Hitchance = 60)\n(T)hief (ATK = 9, HP = 45, EXP = 11, GOLD = 10, Hitchance = 80)'
    print(badcharinfochoice)
    # TODO Make the enemy list read from some file or something.
    while True:
        match input().lower():
            case 'r':
                return badcharSpecifier(3, 21, 5, 'Rat', 2, 50)
            case 'g':
                return badcharSpecifier(6, 36, 10, 'Goblin', 5, 60)
            case 't':
                return badcharSpecifier(9, 45, 11, 'Thief', 10, 80)
            case 'e':
                raise Exception('TODO for when I add the menu')
            case _:
                print('Please input an available enemy letter: (or (E)XIT)')
                print(badcharinfochoice)


def fightPhase(player, enemy):
    activehp = player.hp
    while enemy['ehp'] > 0:
        if player.hp <= 0:
            print('You died!')
            activehp = player.hp
            break # TODO Send the user to the menu, when I create one.
        print('"What should I do?" Current Enemy: {0}, Enemy HP: {1}, Your HP: {2}/{3}'.format(enemy['ename'], str(enemy['ehp']), str(activehp), str(player.hp)))
        print('(A)TTACK, (D)EFEND') # TODO Add some sort of running option, probably based on some kind of chance so you can't just leave at a critical point.
        patkcalc = random.randint(player.atkrange[0], player.atkrange[1])
        pdefcalc = random.randint(player.defrange[0], player.defrange[1])
        phitchance = random.randint(0, 100)
        eatkcalc = random.randint(0, enemy['eatk'])
        ehitchance = random.randint(0, 100)
        match input().lower():
            case 'a':
                if phitchance > player.hitchance and ehitchance > enemy['ehitchance']:
                    print('Both of you missed your attack!')
                elif phitchance > player.hitchance:
                    activehp = activehp - eatkcalc
                    print('You missed your attack, and the enemy hit you for {0} damage!'.format(str(eatkcalc)))
                elif ehitchance > enemy['ehitchance']:
                    enemy['ehp'] = enemy['ehp'] - patkcalc
                    print('You hit your an enemy, and dealt {0} damage!'.format(str(patkcalc)))
                    print('The enemy missed their attack!')
                else:
                    enemy['ehp'] = enemy['ehp'] - patkcalc
                    activehp = activehp - eatkcalc
                    print('You hit your an enemy, and dealt {0} damage!'.format(str(patkcalc)))
                    print('The enemy dealt {0} damage!'.format(str(eatkcalc)))
            case 'd':
                if pdefcalc == 0:
                    activehp = activehp - eatkcalc
                    print('You were too slow, and the enemy hit you for {0} damage!'.format(str(eatkcalc)))
                elif ehitchance > enemy['Ehitchance']:
                    print('Even though you defended, the enemy missed their attack!')
                else:
                    if pdefcalc >= eatkcalc:
                        print('You defended against an enemy, and fully deflected {0} damage!'.format(str(pdefcalc)))
                    else:
                        activehp = activehp - (eatkcalc - pdefcalc)
                        print('You defended against an enemy, and deflected {0} damage! But you took the remaining {1} damage!'.format(str(pdefcalc), str(eatkcalc - pdefcalc)))
            case _:
                print('Please input the right command.')
    else:
        player.exp = player.exp + enemy['expgain']
        player.gold = player.gold + enemy['goldgain']
        print('You won the fight! You gained {0} EXP and {1} GOLD!\nYour current EXP = {2}, Your current GOLD = {3}.'.format(str(enemy['expgain']), str(enemy['goldgain']), str(player.exp), str(player.gold)))
        if player.exp >= player.lvl * 27: # TODO Replace this formula with something different
            player.lvl += 1
            player.exp = 0
            print('You leveled up! You are now LVL {0}!'.format(str(player.lvl)))
            print('Next level up goal is: {0} EXP!'.format(str(player.lvl * 27)))
            print('You can upgrade your stats, please input a character in brackets from one of them:')
            lvlupinfo = '(A)TK, (D)EF, (H)P'
            print(lvlupinfo)
            while True:
                match input().lower(): # TODO Test this
                    case 'a':
                        player.atkrange += 1
                        return
                    case 'd':
                        player.defrange += 1
                        return
                    case 'h':
                        player.hp += 3
                        return
                    case _:
                        print('please input the right letter name:')
                        print(lvlupinfo)
        else:
            print('Next level up is in: {0} EXP!'.format(str(player.lvl * 27 - player.exp)))


player = characterChoice() # TEMPORARY CODE
enemy = badplayerChoice() # TEMPORARY CODE
fightPhase(player, enemy) # TEMPORARY CODE
