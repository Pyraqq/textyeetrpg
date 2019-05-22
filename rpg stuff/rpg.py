import random, pickle, os

# Stats
class Levelstats: #Level stats function
    def __init__(self, LVL, LVLRequirements, EXP, GOLD):
        self.LVL = LVL
        self.LVLRequirements = LVLRequirements
        self.EXP = EXP
        self.GOLD = GOLD

levelos = Levelstats(1, 27, -27, 0)

class Characterinfoclass: # Class choice function
    def __init__(self, classname, PATK, PDEF, PHP, PHPActive, inventory, inventoryslots, PATKBonus, PDEFBonus, hitchance):
        self.classname = classname
        self.PATK = PATK
        self.PDEF = PDEF
        self.PHP = PHP
        self.PHPActive = PHPActive
        self.inventory = None
        self.inventoryslots = None
        self.PATKBonus = PATKBonus
        self.PDEFBonus = PDEFBonus
        self.hitchance = hitchance

    def equipFunctionATK(self, slot, slottype, name, bonusvalue, hitchance, unequipfirst, equipinput): # Equip Function for items that increases ATK
        if slot in self.inventoryslots:
            print(unequipfirst.format(slottype))
        else:
            self.inventoryslots[slot] = name
            self.PATKBonus += bonusvalue
            self.hitchance = hitchance
            self.inventory[equipinput] = 'EQUIPPED'
            print('You have equipped the item!')
    
    def equipFunctionDEF(self, slot, slottype, name, bonusvalue, unequipfirst, equipinput): # Equip Function for items that increases DEF
        if slot in self.inventoryslots:
            print(unequipfirst.format(slottype))
        else:
            self.inventoryslots[slot] = name
            self.PDEFBonus += bonusvalue
            self.inventory[equipinput] = 'EQUIPPED'
            print('You have equipped the item!')

    def unequipFunctionATK(self, slot, bonusvalue, hitchance): # Unequip Function for items that increases ATK
        del self.inventoryslots[slot]
        self.PATKBonus -= bonusvalue
        self.hitchance = hitchance

    def unequipFunctionDEF(self, slot, bonusvalue): # Unequip Function for items that increases DEF
        del self.inventoryslots[slot]
        self.PDEFBonus -= bonusvalue

    def storeFunction(self, name, costvalue, itemdenied, storeoption, itemnocash): # Defines what item was bought and the price for it
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
    
    def itemDrop(self, name): # Item drop event from ADVENTURE
        self.inventory[name] = 'UNEQUIPPED'
        print('It is a {0}!'.format(name))

def enemySpecifier(ATKValue, HPValue, EXPValue, Name, GOLDValue, Ehitchance):
    enemy = {
    'EATK' : ATKValue,
    'EHP' : HPValue,
    'EXPGain' : EXPValue,
    'EName' : Name,
    'GOLDGain' : GOLDValue,
    'Ehitchance' : Ehitchance
    }
    return enemy

def randomEnemy(): # Random enemy chance from ADVENTURE
    randomenemyint = random.randint(0, 100)
    if randomenemyint <= 60:
        enemy = enemySpecifier(3, 21, 5, 'RAT', 2, 50)
    elif randomenemyint <= 90:
        enemy = enemySpecifier(6, 36, 10, 'GOBLIN', 5, 60)
    elif randomenemyint <= 100:
        enemy = enemySpecifier(9, 45, 11, 'THIEF', 10, 80)
    return enemy

def characterChoice(): # Character Choice
    print('Choose your class:')
    classinfo = '(B)ERSERKER (ATK = 4, DEF = 3, HP = 45)\n(P)ROTECTOR (ATK = 3, DEF = 4, HP = 60)'
    print(classinfo)
    cchoice = True
    while cchoice:
        classinput = input().lower()
        if classinput == 'b': # Berserker class choice
            player = Characterinfoclass('Berserker', 3, 3, 45, 45, None, None, 1, 0, 75)
            player.inventory = {
            'WOODEN SWORD' : 'EQUIPPED'
            }
            player.inventoryslots = {
            'HAND1' : 'WOODEN SWORD'
            }
            cchoice = False
        elif classinput == 'p': # Protector class choice
            player = Characterinfoclass('Protector', 3, 3, 60, 60, None, None, 0, 1, 80)
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

def dataLoad(): # Data load function
    player = Characterinfoclass(None, 0, 0, 0, 0, None, None, 0, 0, 0)
    wyltgload = 'Would you like to load your save data? (Y/N)'
    loadchoice = True
    while loadchoice:
        print(wyltgload)
        loadquestion = input().lower()
        if loadquestion == 'y': # Load choice
            if os.path.getsize("rpg stuff//savedata.txt") <= 0:
                print('There is nothing to load!')
                loadchoice = False
                player = characterChoice()
            else:
                f= open("rpg stuff//savedata.txt", "r")
                invfile = "rpg stuff//invdata.txt"
                infile = open(invfile, 'rb')
                levelos.LVL = int(f.readline())
                levelos.LVLRequirements = int(f.readline())
                levelos.EXP = int(f.readline())
                levelos.GOLD = int(f.readline())
                player.classname = f.readline()
                player.PATK = int(f.readline())
                player.PDEF = int(f.readline())
                player.PHP = int(f.readline())
                player.PHPActive = int(f.readline())
                player.PATKBonus = int(f.readline())
                player.PDEFBonus = int(f.readline())
                player.hitchance = int(f.readline())
                invdict = pickle.load(infile)
                player.inventory = invdict['inv']
                player.inventoryslots = invdict['slt']
                f.close()
                infile.close()
                loadchoice = False
                print('Loaded!')
        elif loadquestion == 'n':
            loadchoice = False
            player = characterChoice()
        else:
            pass
    return player

def adventure(player): # Basically main menu
    wherewyltg = 'Where would you like to go?'
    locations = '(W)OODS, (E)XIT'
    rightcommand = 'Please input the right command:'
    whattodo = '(W)ALK, (E)XIT'
    whatshould = 'What should I do?'
    print(wherewyltg)
    print(locations)
    lchoice = True
    while lchoice:
        locationchoice = input().lower()
        if locationchoice == 'w': # Woods Location choice
            lchoice = False
            wanderingaround = True
            print(whatshould)
            while wanderingaround:
                print(whattodo)
                decision = input().lower()
                if decision == 'w': # Walk choice
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
                                levelos.GOLD += 5
                            else:
                                Characterinfoclass.itemDrop(player, 'WOODEN SWORD')
                        elif randomitem <= 90:
                            if 'WOODEN SHIELD' in player.inventory:
                                print('You already have this item, so you sell it for {} GOLD!'.format(7))
                                levelos.GOLD += 7
                            else:
                                Characterinfoclass.itemDrop(player, 'WOODEN SHIELD')
                        elif randomitem <= 97:
                            if 'IRON SWORD' in player.inventory:
                                print('You already have this item, so you sell it for {} GOLD!'.format(12))
                                levelos.GOLD += 12
                            else:
                                Characterinfoclass.itemDrop(player, 'IRON SWORD')
                        elif randomitem <= 100:
                            if 'LEATHER ARMOR SET' in player.inventory:
                                print('You already have this item, so you sell it for {} GOLD!'.format(15))
                                levelos.GOLD += 15
                            else:
                                Characterinfoclass.itemDrop(player, 'LEATHER ARMOR SET')
                        print(whatshould)
                    elif randomevent <= 100:
                        print('Nothing happens.')
                        print(whatshould)
                elif decision == 'e': # Exit to location choice
                    wanderingaround = False
                    print(wherewyltg)
                    print(locations)
                    lchoice = True
                else:
                    print(rightcommand)
        elif locationchoice == 'e': # Exit to menu
            lchoice = False
            dayChoice(player, levelos)
        else:
            print(rightcommand)
            print(locations)

def dayChoice(player, levelos): # Day option
    choiceoflife = 'What should I do today?'
    dayinfo = 'A(D)VENTURE, (A)RENA, (S)TORE, (I)NVENTORY, S(T)ATUS, SA(V)E'
    invinfo = 'E(Q)UIP, (U)NEQUIP, (E)XIT'
    unequipfirst = 'Unequip your {0} first!'
    print(choiceoflife)
    print(dayinfo)
    dchoice = True
    while dchoice:
        takeyourtime = input().lower()
        if takeyourtime == 'd': # Adventure choice
            adventure(player)
        elif takeyourtime == 'a': # Arena choice
            enemy = badplayerChoice(player)
            fightPhase(player, enemy)
            print(choiceoflife)
            print(dayinfo)
        elif takeyourtime == 's': # Store choice
            store(player, dayinfo)
        elif takeyourtime == 'i': # Inventory choice
            print(player.inventory)
            invchoice = True
            while invchoice:
                print(invinfo)
                invinput = input().lower()
                if invinput == 'q': # Equip choice
                    print('What would you like to equip?')
                    equipchoice = True
                    while equipchoice:
                        print(player.inventory)
                        print('If you are done, please (E)XIT this action.')
                        equipinput = input().upper()
                        if equipinput in player.inventory:
                            if player.inventory[equipinput] == 'EQUIPPED':
                                print('This item is already equipped!')
                            else:
                                if equipinput == 'WOODEN SWORD':
                                    Characterinfoclass.equipFunctionATK(player, 'HAND1', 'weapon', 'WOODEN SWORD', 1, 75, unequipfirst, equipinput)
                                elif equipinput == 'WOODEN SHIELD':
                                    Characterinfoclass.equipFunctionDEF(player, 'HAND2', 'shield', 'WOODEN SHIELD', 1, unequipfirst, equipinput)
                                elif equipinput == 'LEATHER ARMOR SET':
                                    Characterinfoclass.equipFunctionDEF(player, 'BODY', 'armor', 'LEATHER ARMOR SET', 2, unequipfirst, equipinput)
                                elif equipinput == 'IRON SWORD':
                                    Characterinfoclass.equipFunctionATK(player, 'HAND1', 'weapon', 'IRON SWORD', 2, 65, unequipfirst, equipinput)
                        elif equipinput == 'E':
                                equipchoice = False
                                print(player.inventory)
                        else:
                            print('Please input the right item:')
                elif invinput == 'u': # Unequip Choice
                    print('What would you like to unequip?')
                    unequipchoice = True
                    while unequipchoice:
                        print(player.inventory)
                        print('If you are done, please (E)XIT this action.')
                        unequipinput = input().upper()
                        if unequipinput in player.inventory:
                            if player.inventory[unequipinput] == 'EQUIPPED':
                                player.inventory[unequipinput] = 'UNEQUIPPED'
                                if unequipinput == 'WOODEN SWORD':
                                    Characterinfoclass.unequipFunctionATK(player, 'HAND1', 1, 80)
                                elif unequipinput == 'WOODEN SHIELD':
                                    Characterinfoclass.unequipFunctionDEF(player, 'HAND2', 1)
                                elif unequipinput == 'LEATHER ARMOR SET':
                                    Characterinfoclass.unequipFunctionDEF(player, 'BODY', 2)
                                elif unequipinput == 'IRON SWORD':
                                    Characterinfoclass.unequipFunctionATK(player, 'HAND1', 2, 80)
                                print('You have unequipped the item!')
                            elif player.inventory[unequipinput] == 'UNEQUIPPED':
                                print('This item is already unequipped!')
                        elif unequipinput == 'E':
                            unequipchoice = False
                            print(player.inventory)
                elif invinput == 'e': # Exit to menu
                    invchoice = False
                    print(choiceoflife)
                    print(dayinfo)
                else:
                    print('Please input the right command:')
        elif takeyourtime == 't': # Status choice
            print('Current Class: ' + player.classname)
            print('LVL = ' + str(levelos.LVL))
            print('EXP = ' + str(levelos.EXP + levelos.LVLRequirements))
            print('EXP to next level = ' + str(levelos.LVLRequirements))
            print('GOLD = ' + str(levelos.GOLD))
            print('HP = ' + str(player.PHP))
            print('Max ATK = ' + str(player.PATK + player.PATKBonus))
            print('Min ATK = ' + str(player.PATKBonus))
            print('Max DEF = ' + str(player.PDEF + player.PDEFBonus))
            print('Min DEF = ' + str(player.PDEFBonus))
            print('Current Hitchance = ' + str(player.hitchance) + '%')
            print(dayinfo)
        elif takeyourtime == 'v': # Save choice
            f= open("rpg stuff//savedata.txt", "w")
            invfile = "rpg stuff//invdata.txt"
            outfile = open(invfile, 'wb')
            f.write(str(levelos.LVL) + '\n')
            f.write(str(levelos.LVLRequirements) + '\n')
            f.write(str(levelos.EXP) + '\n')
            f.write(str(levelos.GOLD) + '\n')
            f.write(player.classname + '\n')
            f.write(str(player.PATK) + '\n')
            f.write(str(player.PDEF) + '\n')
            f.write(str(player.PHP) + '\n')
            f.write(str(player.PHPActive) + '\n')
            f.write(str(player.PATKBonus) + '\n')
            f.write(str(player.PDEFBonus) + '\n')
            f.write(str(player.hitchance))
            inventorystuff = {
            'inv' : player.inventory,
            'slt' : player.inventoryslots
            }
            pickle.dump(inventorystuff, outfile)
            f.close()
            outfile.close()
            print('Saved!')
            print(dayinfo)
        else:
            print('Please input the right command:')
            print(dayinfo)

def store(player, dayinfo): # Store option
    storeoption = '1 = WOODEN SWORD (10 gold, +1 ATK, 75% Hit Chance)\n2 = WOODEN SHIELD (15 gold, +1 DEF)\n3 = LEATHER ARMOR SET (30 gold, +2 DEF)\n4 = IRON SWORD (25 GOLD, +1 ATK, 65% Hit Chance)\nIf you are done, please (E)XIT the store.'
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
        elif sinput == 'e':
            print('What should I do today?')
            print(dayinfo)
            break
        else:
            print('Please input the right item:')
            print(storeoption)
    return player

def badplayerChoice(player): # Enemy Choice function
    print('Choose an enemy to fight: (or (E)XIT)')
    enemyinfochoice = 'RAT (ATK = 3, HP = 21, EXP = 5, GOLD = 2, Hitchance = 50)\nGOBLIN (ATK = 6, HP = 36, EXP = 10, GOLD = 5, Hitchance = 60)\nTHIEF (ATK = 9, HP = 45, EXP = 11, GOLD = 10, Hitchance = 80)'
    print(enemyinfochoice)
    echoice = True
    while echoice:
        enemyinput = input().lower()
        if enemyinput == 'rat':
            enemy = enemySpecifier(3, 21, 5, 'RAT', 2, 50)
            echoice = False
        elif enemyinput == 'goblin':
            enemy = enemySpecifier(6, 36, 10, 'GOBLIN', 5, 60)
            echoice = False
        elif enemyinput == 'thief':
            enemy = enemySpecifier(9, 45, 11, 'THIEF', 10, 80)
            echoice = False
        elif enemyinput == 'e': # Exit to menu
            echoice = False
            dayChoice(player, levelos)
        else:
            print('Please input the right enemy name:')
            print(enemyinfochoice)
    return enemy

# Fight function
def fightPhase(player, enemy): # Basically fight code
    playeratkmin = player.PATKBonus
    playeratkmax = player.PATK + player.PATKBonus
    playerdefmin = player.PDEFBonus
    playerdefmax = player.PDEF + player.PDEFBonus
    if playeratkmin == 0:
        playeratkmin += 1
    hitchance = player.hitchance
    while enemy['EHP'] > 0:
        if player.PHPActive <= 0:
            print('You died!')
            player.PHPActive = player.PHP
            dataLoad()
            break
        print('What should I do? Current Enemy: {0}, Enemy HP: {1}, Your HP: {2}/{3}'.format(enemy['EName'].upper(), str(enemy['EHP']), str(player.PHPActive), str(player.PHP)))
        print('(A)TTACK, (D)EFEND')
        patkcalc = 0 # Your Attack value
        pdefcalc = 0 # Your Defense value
        eatkcalc = 0 # Enemy's Attack value
        fightinput = input().lower()
        if fightinput == 'a': # Attack choice
            patkcalc = random.randint(playeratkmin, playeratkmax)
            phitchance = random.randint(0, 100)
            eatkcalc = random.randint(0, enemy['EATK'])
            ehitchance = random.randint(0, 100)
            if phitchance > hitchance:
                player.PHPActive = player.PHPActive - eatkcalc
                print('You missed your attack, and the enemy hit you for {0} damage!'.format(str(eatkcalc)))
            elif phitchance > hitchance and ehitchance > enemy['Ehitchance']:
                print('Both of you missed your attack!')
            elif ehitchance > enemy['Ehitchance']:
                enemy['EHP'] = enemy['EHP'] - patkcalc
                print('You hit your an enemy, and dealt {0} damage!'.format(str(patkcalc)))
                print('The enemy missed their attack!')
            else:
                enemy['EHP'] = enemy['EHP'] - patkcalc
                print('You hit your an enemy, and dealt {0} damage!'.format(str(patkcalc)))
                player.PHPActive = player.PHPActive - eatkcalc
                print('The enemy dealt {0} damage!'.format(str(eatkcalc)))
        elif fightinput == 'd': # Defend Choice
            pdefcalc = random.randint(playerdefmin, playerdefmax)
            eatkcalc = random.randint(0, enemy['EATK'])
            ehitchance = random.randint(0, 100)
            if pdefcalc == 0:
                player.PHPActive = player.PHPActive - eatkcalc
                print('You were too slow, and the enemy hit you for {0} damage!'.format(str(eatkcalc)))
            elif ehitchance > enemy['Ehitchance']:
                print('Even though you defended, the enemy missed their attack!')
            else:
                if pdefcalc > eatkcalc:
                    print('You defended against an enemy, and fully deflected {0} damage!'.format(str(pdefcalc)))
                else:
                    player.PHPActive = player.PHPActive - (eatkcalc - pdefcalc)
                    print('You defended against an enemy, and deflected {0} damage! But you took the remaining {1} damage!'.format(str(pdefcalc), str(eatkcalc - pdefcalc)))
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
                lvlupinput = input().lower() # This is where you upgrade your Max ATK DEF and HP
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
    player = dataLoad()
    while levelos.LVL < 10:
        dayChoice(player, levelos)
    if levelos.LVL == 10:
        print('You won the game!')

if __name__ == '__main__':
    main()
