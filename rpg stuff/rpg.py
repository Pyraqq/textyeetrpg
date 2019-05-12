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

    def equipFunctionATK(self, slot, slottype, name, bonusvalue, unequipfirst, equipinput):
        if slot in self.inventoryslots:
            print(unequipfirst.format(slottype))
        else:
            self.inventoryslots[slot] = name
            self.PATKBonus += bonusvalue
            self.inventory[equipinput] = 'EQUIPPED'
            print('You have equipped the item!')
    
    def equipFunctionDEF(self, slot, slottype, name, bonusvalue, unequipfirst, equipinput):
        if slot in self.inventoryslots:
            print(unequipfirst.format(slottype))
        else:
            self.inventoryslots[slot] = name
            self.PDEFBonus += bonusvalue
            self.inventory[equipinput] = 'EQUIPPED'
            print('You have equipped the item!')

    def unequipFunctionATK(self, slot, bonusvalue):
        del self.inventoryslots[slot]
        self.PATKBonus -= bonusvalue

    def unequipFunctionDEF(self, slot, bonusvalue):
        del self.inventoryslots[slot]
        self.PDEFBonus -= bonusvalue

    def storeFunction(self, name, costvalue, itemdenied, storeoption, itemnocash):
        if levelos.GOLD >= costvalue:
            if name in self.inventory:
                print(itemdenied)
                print(storeoption)
            else:
                levelos.GOLD -= costvalue
                self.inventory[name] = 'UNEQUIPPED'
                print('You bought the {0}!'.format(name))
                print(storeoption)
        else:
            print(itemnocash)
            print(storeoption)
    
    def itemDrop(self, name):
        self.inventory[name] = 'UNEQUIPPED'
        print('It is a {0}!'.format(name))

def enemySpecifier(ATKValue, HPValue, EXPValue, Name, GOLDValue):
    enemy = {
    'EATK' : ATKValue,
    'EHP' : HPValue,
    'EXPGain' : EXPValue,
    'EName' : Name,
    'GOLDGain' : GOLDValue
    }
    return enemy

def randomEnemy():
    randomenemyint = random.randint(0, 100)
    if randomenemyint <= 60:
        enemy = enemySpecifier(3, 21, 5, 'RAT', 2)
    elif randomenemyint <= 90:
        enemy = enemySpecifier(6, 36, 10, 'GOBLIN', 5)
    elif randomenemyint <= 100:
        enemy = enemySpecifier(9, 45, 11, 'THIEF', 10)
    return enemy

def characterChoice(): # Character Choice
    print('Choose your class:')
    classinfo = 'BERSERKER (ATK = 6, DEF = 3, HP = 45)\nPROTECTOR (ATK = 3, DEF = 6, HP = 60)'
    print(classinfo)
    cchoice = True
    while cchoice:
        classinput = input().lower()
        if classinput == 'berserker':
            player = Characterinfoclass(3, 3, 45, 45, None, None, 3, 0)
            player.inventory = {
            'WOODEN SWORD' : 'EQUIPPED'
            }
            player.inventoryslots = {
            'HAND1' : 'WOODEN SWORD'
            }
            cchoice = False
        elif classinput == 'protector':
            player = Characterinfoclass(3, 3, 60, 60, None, None, 0, 3)
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

def adventure(player):
    wherewyltg = 'Where would you like to go?'
    locations = 'WOODS, EXIT'
    rightcommand = 'Please input the right command:'
    whattodo = 'WALK, EXIT'
    whatshould = 'What should I do?'
    print(wherewyltg)
    print(locations)
    lchoice = True
    while lchoice:
        locationchoice = input().lower()
        if locationchoice == 'woods':
            lchoice = False
            wanderingaround = True
            print(whatshould)
            while wanderingaround:
                print(whattodo)
                decision = input().lower()
                if decision == 'walk':
                    print('You move forward.')
                    randomevent = random.randint(0, 100)
                    if randomevent <= 40:
                        print('You have encountered an enemy!')
                        enemy = randomEnemy()
                        fightPhase(player, enemy)
                        print(whatshould)
                    elif randomevent <= 45:
                        print('You have found an item!')
                        randomitem = random.randint(0, 100)
                        if randomitem <= 70:
                            if 'WOODEN SWORD' in player.inventory:
                                print('You already have this item, so you sell it for {} GOLD!'.format(5))
                                player.GOLD += 5
                            else:
                                Characterinfoclass.itemDrop(player, 'WOODEN SWORD')
                        elif randomitem <= 90:
                            if 'WOODEN SHIELD' in player.inventory:
                                print('You already have this item, so you sell it for {} GOLD!'.format(7))
                                player.GOLD += 7
                            else:
                                Characterinfoclass.itemDrop(player, 'WOODEN SHIELD')
                        elif randomitem <= 97:
                            if 'IRON SWORD' in player.inventory:
                                print('You already have this item, so you sell it for {} GOLD!'.format(12))
                                player.GOLD += 12
                            else:
                                Characterinfoclass.itemDrop(player, 'IRON SWORD')
                        elif randomitem <= 100:
                            if 'LEATHER ARMOR SET' in player.inventory:
                                print('You already have this item, so you sell it for {} GOLD!'.format(15))
                                player.GOLD += 15
                            else:
                                Characterinfoclass.itemDrop(player, 'LEATHER ARMOR SET')
                        print(whatshould)
                    elif randomevent <= 100:
                        print('Nothing happens.')
                        print(whatshould)
                elif decision == 'exit':
                    wanderingaround = False
                    print(wherewyltg)
                    print(locations)
                    lchoice = True
                else:
                    print(rightcommand)
        elif locationchoice == 'exit':
            lchoice = False
            dayChoice(player)
        else:
            print(rightcommand)
            print(locations)

def dayChoice(player): # Day option
    choiceoflife = 'What should I do today?'
    dayinfo = 'ADVENTURE, ARENA, STORE, INVENTORY'
    invinfo = 'EQUIP, UNEQUIP, EXIT'
    unequipfirst = 'Unequip your {0} first!'
    print(choiceoflife)
    print(dayinfo)
    dchoice = True
    while dchoice:
        takeyourtime = input().lower()
        if takeyourtime == 'adventure':
            adventure(player)
        elif takeyourtime == 'arena':
            enemy = badplayerChoice(player)
            fightPhase(player, enemy)
            print(choiceoflife)
            print(dayinfo)
        elif takeyourtime == 'store':
            store(player, dayinfo)
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
                        print('If you are done, please EXIT this action.')
                        equipinput = input().upper()
                        if equipinput in player.inventory:
                            if player.inventory[equipinput] == 'EQUIPPED':
                                print('This item is already equipped!')
                            else:
                                if equipinput == 'WOODEN SWORD':
                                    Characterinfoclass.equipFunctionATK(player, 'HAND1', 'weapon', 'WOODEN SWORD', 1, unequipfirst, equipinput)
                                elif equipinput == 'WOODEN SHIELD':
                                    Characterinfoclass.equipFunctionDEF(player, 'HAND2', 'shield', 'WOODEN SHIELD', 1, unequipfirst, equipinput)
                                elif equipinput == 'LEATHER ARMOR SET':
                                    Characterinfoclass.equipFunctionDEF(player, 'BODY', 'armor', 'LEATHER ARMOR SET', 2, unequipfirst, equipinput)
                                elif equipinput == 'IRON SWORD':
                                    Characterinfoclass.equipFunctionATK(player, 'HAND1', 'weapon', 'IRON SWORD', 2, unequipfirst, equipinput)
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
                        print('If you are done, please EXIT this action.')
                        unequipinput = input().upper()
                        if unequipinput in player.inventory:
                            if player.inventory[unequipinput] == 'EQUIPPED':
                                player.inventory[unequipinput] = 'UNEQUIPPED'
                                if unequipinput == 'WOODEN SWORD':
                                    Characterinfoclass.unequipFunctionATK(player, 'HAND1', 1)
                                elif unequipinput == 'WOODEN SHIELD':
                                    Characterinfoclass.unequipFunctionDEF(player, 'HAND2', 1)
                                elif unequipinput == 'LEATHER ARMOR SET':
                                    Characterinfoclass.unequipFunctionDEF(player, 'BODY', 2)
                                elif unequipinput == 'IRON SWORD':
                                    Characterinfoclass.unequipFunctionATK(player, 'HAND1', 2)
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

def store(player, dayinfo): # Store option
    storeoption = '1 = WOODEN SWORD (10 gold, +1 ATK)\n2 = WOODEN SHIELD (15 gold, +1 DEF)\n3 = LEATHER ARMOR SET (30 gold, +2 DEF)\n4 = IRON SWORD (25 GOLD, +1 ATK)\nIf you are done, please EXIT the store.'
    itemdenied = 'You already have this item!'
    itemnocash = 'You dont have enough GOLD!'
    print('What should I buy?')
    print('You currently have: {0} GOLD.'.format(levelos.GOLD))
    print(storeoption)
    schoice = True
    while schoice:
        sinput = input().lower()
        if sinput == '1':
            Characterinfoclass.storeFunction(player, 'WOODEN SWORD', 10, itemdenied, storeoption, itemnocash)
        elif sinput == '2':
            Characterinfoclass.storeFunction(player, 'WOODEN SHIELD', 15, itemdenied, storeoption, itemnocash)
        elif sinput == '3':
            Characterinfoclass.storeFunction(player, 'LEATHER ARMOR SET', 30, itemdenied, storeoption, itemnocash)
        elif sinput == '4':
            Characterinfoclass.storeFunction(player, 'IRON SWORD', 25, itemdenied, storeoption, itemnocash)
        elif sinput == 'exit':
            print('What should I do today?')
            print(dayinfo)
            break
        else:
            print('Please input the right item:')
            print(storeoption)
    return player

# Enemy Choice function
def badplayerChoice(player):
    print('Choose an enemy to fight: (or EXIT)')
    enemyinfochoice = 'RAT (ATK = 3, HP = 21, EXP = 5, GOLD = 2)\nGOBLIN (ATK = 6, HP = 36, EXP = 10, GOLD = 5)\nTHIEF (ATK = 9, HP = 45, EXP = 11, GOLD = 10)'
    print(enemyinfochoice)
    echoice = True
    while echoice:
        enemyinput = input().lower()
        if enemyinput == 'rat':
            enemy = enemySpecifier(3, 21, 5, 'RAT', 2)
            echoice = False
        elif enemyinput == 'goblin':
            enemy = enemySpecifier(6, 36, 10, 'GOBLIN', 5)
            echoice = False
        elif enemyinput == 'thief':
            enemy = enemySpecifier(9, 45, 11, 'THIEF', 10)
            echoice = False
        elif enemyinput == 'exit':
            echoice = False
            dayChoice(player)
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
        print('You won the fight! You gained {0} EXP and {1} GOLD!\nYour current EXP = {2}, Your current GOLD = {3}.'.format(str(enemy['EXPGain']), str(enemy['GOLDGain']), str(levelos.EXP + levelos.LVLRequirements), str(levelos.GOLD)))
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
                    player.PHP += 3
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
    if levelos.LVL == 10:
        print('You won the game!')

if __name__ == '__main__':
    main()
