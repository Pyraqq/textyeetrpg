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
    def __init__(self, PATK, PDEF, PHP, PHPActive, inventory, inventoryslots, PATKBonus, PDEFBonus): 
        self.PATK = PATK
        self.PDEF = PDEF
        self.PHP = PHP
        self.PHPActive = PHPActive
        self.inventory = None
        self.inventoryslots = None
        self.PATKBonus = PATKBonus
        self.PDEFBonus = PDEFBonus

def characterChoice(): # Character Choice
    print('Choose your class:')
    classinfo = 'BERSERKER (ATK = 2, DEF = 1, HP = 15), PROTECTOR (ATK = 1, DEF = 2, HP = 20)'
    print(classinfo)
    cchoice = True
    while cchoice:
        classinput = input().lower()
        if classinput == 'berserker':
            player = Characterinfoclass(1, 1, 15, 15, None, None, 1, 0)
            player.inventory = {
            'WOODEN SWORD' : 'EQUIPPED'
            }
            player.inventoryslots = {
            'HAND1' : 'WOODEN SWORD'
            }
            cchoice = False
        elif classinput == 'protector':
            player = Characterinfoclass(1, 1, 20, 20, None, None, 0, 1)
            player.inventory = {
            'WOODEN SHIELD' : 'EQUIPPED'
            }
            player.inventoryslot = {
            'HAND2' : 'WOODEN SHIELD'
            }
            cchoice = False
        else:
            print('Please input the right class name:')
            print(classinfo)
    return player

def dayChoice(player): # Day option
    choiceoflife = 'What should I do today?'
    dayinfo = 'FIGHT, STORE, INVENTORY'
    invinfo = 'EQUIP, UNEQUIP, EXIT'
    unequipfirst = 'Unequip your {0} first!'
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
                    print('What would you like to equip?')
                    equipchoice = True
                    while equipchoice:
                        print(player.inventory)
                        print('If you are done, please EXIT the inventory.')
                        equipinput = input().upper()
                        if equipinput in player.inventory:
                            if player.inventory[equipinput] == 'EQUIPPED':
                                print('This item is already equipped!')
                            else:
                                if equipinput == 'WOODEN SWORD':
                                    if 'HAND1' in player.inventoryslots:
                                        print(unequipfirst.format('weapon'))
                                    else:
                                        player.inventoryslots['HAND1'] = 'WOODEN SWORD'
                                        player.PATKBonus += 1
                                        player.inventory[equipinput] = 'EQUIPPED'
                                        print('You have equipped the item!')
                                elif equipinput == 'WOODEN SHIELD':
                                    if 'HAND2' in player.inventoryslots:
                                        print(unequipfirst.format('shield'))
                                    else:
                                        player.inventoryslots['HAND2'] = 'WOODEN SHIELD'
                                        player.PDEFBonus += 1
                                        player.inventory[equipinput] = 'EQUIPPED'
                                        print('You have equipped the item!')
                                elif equipinput == 'LEATHER ARMOR SET':
                                    if 'BODY' in player.inventoryslots:
                                        print(unequipfirst.format('armor'))
                                    else:
                                        player.inventoryslots['BODY'] = 'LEATHER ARMOR SET'
                                        player.PDEFBonus += 2
                                        player.inventory[equipinput] = 'EQUIPPED'
                                        print('You have equipped the item!')
                                elif equipinput == 'IRON SWORD':
                                    if 'HAND1' in player.inventoryslots:
                                        print(unequipfirst.format('weapon'))
                                    else:
                                        player.inventoryslots['HAND1'] = 'IRON SWORD'
                                        player.PATKBonus += 2
                                        player.inventory[equipinput] = 'EQUIPPED'
                                        print('You have equipped the item!')
                        elif equipinput == 'EXIT':
                                equipchoice = False
                                print(player.inventory)
                        else:
                            print('Please input the right item:')
                elif invinput == 'unequip':
                    print('What would you like to unequip?')
                    unequipchoice = True
                    while unequipchoice:
                        print(player.inventory)
                        print('If you are done, please EXIT the inventory.')
                        unequipinput = input().upper()
                        if unequipinput in player.inventory:
                            if player.inventory[unequipinput] == 'EQUIPPED':
                                player.inventory[unequipinput] = 'UNEQUIPPED'
                                if unequipinput == 'WOODEN SWORD':
                                    del player.inventoryslots['HAND1']
                                    player.PATKBonus -= 1
                                elif unequipinput == 'WOODEN SHIELD':
                                    del player.inventoryslots['HAND2']
                                    player.PDEFBonus -= 1
                                elif unequipinput == 'LEATHER ARMOR SET':
                                    del player.inventoryslots['BODY']
                                    player.PDEFBonus -= 2
                                elif unequipinput == 'IRON SWORD':
                                    del player.inventoryslots['HAND1']
                                    player.PATKBonus -= 2
                                print('You have unequipped the item!')
                            elif player.inventory[unequipinput] == 'UNEQUIPPED':
                                print('This item is already unequipped!')
                        elif unequipinput == 'EXIT':
                            unequipchoice = False
                            print(player.inventory)
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
    storeoption = '1 = WOODEN SWORD (10 gold, +1 ATK), 2 = WOODEN SHIELD (15 gold, +1 DEF), 3 = LEATHER ARMOR SET (30 gold, +2 DEF), 4 = IRON SWORD (25 GOLD, +2 ATK). If you are done, please EXIT the store.'
    itemdenied = 'You already have this item!'
    itemnocash = 'You dont have enough GOLD!'
    print('You currently have: {0} GOLD.'.format(levelos.GOLD))
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
                    levelos.GOLD -= 10
                    player.inventory['WOODEN SWORD'] = 'UNEQUIPPED'
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
                    levelos.GOLD -= 15
                    player.inventory['WOODEN SHIELD'] = 'UNEQUIPPED'
                    print('You bought the WOODEN SHIELD!')
                    print(storeoption)
            else:
                print(itemnocash)
                print(storeoption)
        elif sinput == '3':
            if levelos.GOLD >= 30:
                if 'LEATHER ARMOR SET' in player.inventory:
                    print(itemdenied)
                    print(storeoption)
                else:
                    levelos.GOLD -= 30
                    player.inventory['LEATHER ARMOR SET'] = 'UNEQUIPPED'
                    print('You bought the LEATHER ARMOR SET!')
                    print(storeoption)
            else:
                print(itemnocash)
                print(storeoption)
        elif sinput == '4':
            if levelos.GOLD >= 25:
                if 'IRON SWORD' in player.inventory:
                    print(itemdenied)
                    print(storeoption)
                else:
                    levelos.GOLD -= 25
                    player.inventory['IRON SWORD'] = 'UNEQUIPPED'
                    print('You bought the IRON SWORD!')
                    print(storeoption)
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
    playeratk = player.PATK + player.PATKBonus
    playerdef = player.PDEF + player.PDEFBonus
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
            patkcalc = random.randint(0, playeratk)
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
            pdefcalc = random.randint(0, playerdef)
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
            levelos.EXP -= levelos.LVLRequirements
            print('You leveled up! You are now LVL {0}!'.format(str(levelos.LVL)))
            print('Next level up goal is: {0} EXP!'.format(str(levelos.LVLRequirements)))
            print('You can upgrade your stats, please input one of them:')
            lvlupinfo = 'ATK, DEF, HP'
            print(lvlupinfo)
            luchoice = True
            while luchoice:
                lvlupinput = input().lower()
                if lvlupinput == 'atk':
                    player.PATK += 1
                    luchoice = False
                elif lvlupinput == 'def':
                    player.PDEF += 1
                    luchoice = False
                elif lvlupinput == 'hp':
                    player.PHP += 2
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
