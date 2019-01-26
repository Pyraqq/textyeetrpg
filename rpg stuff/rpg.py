import random

# Stats
class Levelstats: #Level stats function
    def __init__(self, LVL, LVLRequirements, EXP, GOLD):
        self.LVL = LVL
        self.LVLRequirements = LVLRequirements
        self.EXP = EXP
        self.GOLD = GOLD

levelos = Levelstats(1, 30, -30, 0)

class Characterinfoclass: # Class choice function
    def __init__(self, PATK, PDEF, PHP, PHPActive, inventory): 
        self.PATK = PATK
        self.PDEF = PDEF
        self.PHP = PHP
        self.PHPActive = PHPActive
        self.inventory = None

def characterChoice(): # Character Choice
    print('Choose your class:')
    player = None
    classinfo = 'BERSERKER (ATK = 2, DEF = 1, HP = 15), PROTECTOR (ATK = 1, DEF = 2, HP = 20)'
    print(classinfo)
    cchoice = True
    while cchoice:
        classinput = input().lower()
        if classinput == 'berserker':
            player = Characterinfoclass(2, 1, 15, 15, None)
            inventory = {
            'WOODEN SWORD' : 'Equipped'
            }
            player.inventory = inventory
            cchoice = False
        elif classinput == 'protector':
            player = Characterinfoclass(1, 2, 20, 20, None)
            inventory = {
            'WOODEN SHIELD' : 'Equipped'
            }
            player.inventory = inventory
            cchoice = False
        else:
            print('Please input the right class name:')
            print(classinfo)
    return player

def dayChoice(player): # Day option
    choiceoflife = 'What should I do today?'
    dayinfo = 'FIGHT, STORE, INVENTORY'
    invinfo = 'EQUIP, EXIT'
    print(choiceoflife)
    print(dayinfo)
    dchoice = True
    while dchoice:
        takeyourtime = input().lower()
        if takeyourtime == 'fight':
            break
        elif takeyourtime == 'store':
            store(player)
        elif takeyourtime == 'inventory':
            print(player.inventory)
            invchoice = True
            while invchoice:
                print(invinfo)
                invinput = input().lower()
                if invinput == 'equip':
                    print('WIP')
                elif invinput == 'exit':
                    invchoice = False
                    print(choiceoflife)
                    print(dayinfo)
                else:
                    print('Please input the right command:')
        else:
            print('Please input the right command:')
            print(dayinfo)

def store(player): # Store option
    print('What should I buy?')
    storeoption = '1 = WOODEN SWORD (10 gold, +1 ATK), 2 = WOODEN SHIELD (15 gold, +1 DEF), 3 =LEATHER ARMOR SET (30 gold, +2 DEF). If you are done, please EXIT the store.'
    itemdenied = 'You already have this item!'
    itemnocash = 'You dont have enough GOLD!'
    print(storeoption)
    schoice = True
    while schoice:
        sinput = input().lower()
        if sinput == '1':
            if levelos.GOLD >= 10:
                if 'WOODEN SWORD' in player.inventory:
                    print(itemdenied)
                    print(storeoption)
                else:
                    levelos.GOLD =- 10
                    player.inventory['WOODEN SWORD'] = 'Unequipped'
                    print('You bought the WOODEN SWORD!')
                    print(storeoption)
            else:
                print(itemnocash)
                print(storeoption)
        elif sinput == '2':
            if levelos.GOLD >= 15:
                if 'WOODEN SHIELD' in player.inventory:
                    print(itemdenied)
                    print(storeoption)
                else:
                    levelos.GOLD =- 15
                    player.inventory['WOODEN SHIELD'] = 'Unequipped'
                    print('You bought the WOODEN SHIELD!')
                    print(storeoption)
            else:
                print(itemnocash)
                print(storeoption)
        elif sinput == '3':
            if levelos.GOLD >= 30:
                if 'LEATHER ARMOR SET' in player.inventory:
                    print(itemdenied)
                else:
                    levelos.GOLD =- 30
                    player.inventory['LEATHER ARMOR SET'] = 'Unequipped'
                    print('You bought the LEATHER ARMOR SET!')
            else:
                print(itemnocash)
                print(storeoption)
        elif sinput == 'exit':
            print('What should I do today?')
            dayinfo = 'FIGHT, STORE, INVENTORY'
            print(dayinfo)
            break
        else:
            print('Please input the right item:')
            print(storeoption)
    return player

# Enemy Choice function
def badplayerChoice():
    print('Choose an enemy to fight:')
    enemyinfochoice = 'RAT (ATK = 1, HP = 7, EXP = 5, GOLD = 2), GOBLIN (ATK = 2, HP = 12, EXP = 10, GOLD = 5)'
    print(enemyinfochoice)
    echoice = True
    while echoice:
        enemyinput = input().lower()
        if enemyinput == 'rat':
            enemy = {
            'EATK' : 1,
            'EHP' : 7,
            'EXPGain' : 5,
            'EName' : 'RAT',
            'GOLDGain' : 2
            }
            echoice = False
        elif enemyinput == 'goblin':
            enemy = {
            'EATK' : 2,
            'EHP' : 12,
            'EXPGain' : 10,
            'EName' : 'GOBLIN',
            'GOLDGain' : 5
            }
            echoice = False
        else:
            print('Please input the right enemy name:')
            print(enemyinfochoice)
    return enemy

# Fight function
def fightPhase(player, enemy):
    while enemy['EHP'] > 0:
        if player.PHPActive <= 0:
            print('You died!')
            player.PHPActive = player.PHP
            characterChoice()
            break
        print('What should I do? Current Enemy: {0}, Enemy HP: {1}, Your HP: {2}/{3}'.format(enemy['EName'].upper(), str(enemy['EHP']), str(player.PHPActive), str(player.PHP)))
        print('ATTACK, DEFEND')
        patkcalc = 0 # Your Attack value
        pdefcalc = 0 # Your Defense value
        eatkcalc = 0 # Enemy's Attack value
        fightinput = input().lower()
        if fightinput == 'attack': # attack option
            patkcalc = random.randint(0, player.PATK)
            eatkcalc = random.randint(0, enemy['EATK'])
            if patkcalc == 0:
                player.PHPActive = player.PHPActive - eatkcalc
                print('You missed your attack, and the enemy hit you for {0} damage!'.format(str(eatkcalc)))
            else:
                enemy['EHP'] = enemy['EHP'] - patkcalc
                print('You hit your an enemy, and dealt {0} damage!'.format(str(patkcalc)))
                player.PHPActive = player.PHPActive - eatkcalc
                print('The enemy dealt {0} damage!'.format(str(eatkcalc)))
        elif fightinput == 'defend': # defend option
            pdefcalc = random.randint(0, player.PDEF)
            eatkcalc = random.randint(0, enemy['EATK'])
            if pdefcalc == 0:
                player.PHPActive = player.PHPActive - eatkcalc
                print('You were too slow, and the enemy hit you for {0} damage!'.format(str(eatkcalc)))
            else:
                if pdefcalc > eatkcalc:
                    pdefcalc = eatkcalc
                    player.PHPActive = player.PHPActive - (eatkcalc - pdefcalc)
                    print('You defended against an enemy, and deflected {0} damage!'.format(str(pdefcalc)))
                else:
                    player.PHPActive = player.PHPActive - (eatkcalc - pdefcalc)
                    print('You defended against an enemy, and deflected {0} damage!'.format(str(pdefcalc)))
        else:
            print('Please input the right command.')
    else:
        levelos.EXP = levelos.EXP + enemy['EXPGain']
        levelos.GOLD = levelos.GOLD + enemy['GOLDGain']
        print('You won the fight! You gained {0} EXP and {1} GOLD! Your current EXP = {2}, Your current GOLD = {3}.'.format(str(enemy['EXPGain']), str(enemy['GOLDGain']), str(levelos.EXP + levelos.LVLRequirements), str(levelos.GOLD)))
        if levelos.EXP >= 0: # Level up if statement
            levelos.LVL += 1
            levelos.LVLRequirements = 27 * levelos.LVL
            levelos.EXP = levelos.EXP - levelos.LVLRequirements
            print('You leveled up! You are now LVL {0}!'.format(str(levelos.LVL)))
            print('Next level up goal is: {0} EXP!'.format(str(levelos.LVLRequirements)))
            print('You can upgrade your stats, please input one of them:')
            lvlupinfo = 'ATK, DEF, HP'
            print(lvlupinfo)
            luchoice = True
            while luchoice:
                lvlupinput = input().lower()
                if lvlupinput == 'atk':
                    player.PATK = player.PATK + 1
                    luchoice = False
                elif lvlupinput == 'def':
                    player.PDEF = player.PDEF + 1
                    luchoice = False
                elif lvlupinput == 'hp':
                    player.PHP = player.PHP + 2
                    luchoice = False
                else:
                    print('Please input the right stat name:')
                    print(lvlupinfo)
        else:
            print('Next level up goal is: {0} EXP!'.format(str(levelos.LVLRequirements)))
        player.PHPActive = player.PHP

def main():
    player = characterChoice()
    while levelos.LVL < 10:
        dayChoice(player)
        enemy = badplayerChoice()
        fightPhase(player, enemy)
    if levelos.LVL == 10:
        print('You won the game!')

if __name__ == '__main__':
    main()
