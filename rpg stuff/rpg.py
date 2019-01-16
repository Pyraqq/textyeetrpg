import random

#Stats
LVL = 1
LVLRequirements = 25 * LVL + 5 * LVL
EXP = -LVLRequirements
PHP = 0
PATK = 0
PDEF = 0
EHP = 0
EATK = 0
EXPGain = 0
EnemyChoice = '0'

def CharacterChoice(): #Class choice function
	global PATK
	global PDEF
	global PHP
	print('Choose your class:')
	print('BERSERKER (ATK = 2, DEF = 1, HP = 15), PROTECTOR (ATK = 1, DEF = 2, HP = 20)')
	CChoice = True
	while CChoice == True:
		ClassChoice = input()
		if ClassChoice == 'BERSERKER':
			PATK = 2
			PDEF = 1
			PHP = 15
			CChoice = False
		elif ClassChoice == 'PROTECTOR':
			PATK = 1
			PDEF = 2
			PHP = 15
			CChoice = False
		else:
			print('Please input the right class name:')
	return PATK and PDEF and PHP

def BadPlayerChoice(): #Enemy Choice function
	global EATK
	global EHP
	global EXPGain
	print('Choose an enemy to fight:')
	print('RAT, GOBLIN')
	EChoice = True
	while EChoice == True:
		EnemyChoice = input()
		if EnemyChoice == 'RAT':
			EATK = 1
			EHP = 7
			EXPGain = 5
			EChoice = False
		elif EnemyChoice == 'GOBLIN':
			EATK = 2
			EHP = 15
			EXPGain = 10
			EChoice = False
		else:
			print('Please input the right enemy name:')
	return EATK and EHP and EXPGain

def FightPhase(): #Fight function
	global EHP
	global PHP
	global EXP
	while EHP > 0:
		if PHP <= 0:
			print('You died!')
			break
		print('What should I do? Current Enemy: ' + EnemyChoice + ' Enemy HP: ' + str(EHP) + ' Your HP: ' + str(PHP))
		print('ATTACK, DEFEND')
		PATKCALC = 0 #Your Attack value
		PDEFCALC = 0 #Your Defense value
		EATKCALC = 0 #Enemy's Attack value
		FightChoice = input()
		if FightChoice == 'ATTACK': #attack option
			PATKCALC = random.randint(0, PATK)
			EATKCALC = random.randint(0, EATK)
			if PATKCALC == 0:
				PHP = PHP - EATKCALC
				print('You missed your attack, and the enemy hit you for ' + str(EATKCALC) + ' damage!')
			else:
				EHP = EHP - PATKCALC
				print('You hit your an enemy, and dealt ' + str(PATKCALC) + ' damage!')
				PHP = PHP - EATKCALC
				print('The enemy dealt ' + str(EATKCALC) + ' damage!')
		elif FightChoice == 'DEFEND': #defend option
			PDEFCALC = random.randint(0, PDEF)
			EATKCALC = random.randint(0, EATK)
			if PDEFCALC == 0:
				PHP = PHP - EATKCALC
				print('You were too slow, and the enemy hit you for ' + str(EATKCALC) + ' damage!')
			else:
				if PDEFCALC > EATKCALC:
					PDEFCALC = EATKCALC
					PHP = PHP - (EATKCALC - PDEFCALC)
					print('You defended against an enemy, and deflected ' + str(PDEFCALC) + ' damage!')
				else:
					PHP = PHP - (EATKCALC - PDEFCALC)
					print('You defended against an enemy, and deflected ' + str(PDEFCALC) + ' damage!')
		else:
			print('Please input the right command:')
	else:
		EXP = EXP + EXPGain
		print('You won the fight! You gained ' + str(EXPGain) + ' EXP! Your current EXP = ' + str(EXP + LVLRequirements) + '.')
		if EXP >= 0:
			LVL = LVL + 1
			EXP = EXP - LVLRequirements
			print('You leveled up! You are now LVL ' + str(LVL) + '!')

CharacterChoice()
BadPlayerChoice()
FightPhase()