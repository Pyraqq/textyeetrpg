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

#Class choice function
def CharacterChoice(): 
	global PATK
	global PDEF
	global PHP
	global PHPActive
	print('Choose your class:')
	ClassInfo = 'BERSERKER (ATK = 2, DEF = 1, HP = 15), PROTECTOR (ATK = 1, DEF = 2, HP = 15)'
	print(ClassInfo)
	CChoice = True
	while CChoice == True:
		ClassChoice = input().lower()
		if ClassChoice == 'berserker':
			PATK = 2
			PDEF = 1
			PHP = 15
			PHPActive = 15
			CChoice = False
		elif ClassChoice == 'protector':
			PATK = 1
			PDEF = 2
			PHP = 15
			PHPActive = 15
			CChoice = False
		else:
			print('Please input the right class name:')
			print(ClassInfo)
	return PATK and PDEF and PHP and PHPActive

#Enemy Choice function
def BadPlayerChoice(): 
	global EATK
	global EHP
	global EXPGain
	global EnemyChoice
	print('Choose an enemy to fight:')
	EnemyInfo = 'RAT (ATK = 1, EXP = 5, HP = 7), GOBLIN (ATK = 2, EXP = 10, HP = 15)'
	print(EnemyInfo)
	EChoice = True
	while EChoice == True:
		EnemyChoice = input().lower()
		if EnemyChoice == 'rat':
			EATK = 1
			EHP = 7
			EXPGain = 5
			EChoice = False
		elif EnemyChoice == 'goblin':
			EATK = 2
			EHP = 15
			EXPGain = 10
			EChoice = False
		else:
			print('Please input the right enemy name:')
			print(EnemyInfo)
	return EATK and EHP and EXPGain and EnemyChoice

#Fight function
def FightPhase(): 
	global LVL
	global EHP
	global PHP
	global PHPActive
	global PATK
	global PDEF
	global EXP
	while EHP > 0:
		if PHPActive <= 0:
			print('You died!')
			break
		print('What should I do? Current Enemy: ' + EnemyChoice.upper() + ', Enemy HP: ' + str(EHP) + ', Your HP: ' + str(PHPActive) + '/' + str(PHP))
		print('ATTACK, DEFEND')
		PATKCALC = 0 #Your Attack value
		PDEFCALC = 0 #Your Defense value
		EATKCALC = 0 #Enemy's Attack value
		FightChoice = input().lower()
		if FightChoice == 'attack': #attack option
			PATKCALC = random.randint(0, PATK)
			EATKCALC = random.randint(0, EATK)
			if PATKCALC == 0:
				PHPActive = PHPActive - EATKCALC
				print('You missed your attack, and the enemy hit you for ' + str(EATKCALC) + ' damage!')
			else:
				EHP = EHP - PATKCALC
				print('You hit your an enemy, and dealt ' + str(PATKCALC) + ' damage!')
				PHPActive = PHPActive - EATKCALC
				print('The enemy dealt ' + str(EATKCALC) + ' damage!')
		elif FightChoice == 'defend': #defend option
			PDEFCALC = random.randint(0, PDEF)
			EATKCALC = random.randint(0, EATK)
			if PDEFCALC == 0:
				PHPActive = PHPActive - EATKCALC
				print('You were too slow, and the enemy hit you for ' + str(EATKCALC) + ' damage!')
			else:
				if PDEFCALC > EATKCALC:
					PDEFCALC = EATKCALC
					PHPActive = PHPActive - (EATKCALC - PDEFCALC)
					print('You defended against an enemy, and deflected ' + str(PDEFCALC) + ' damage!')
				else:
					PHPActive = PHPActive - (EATKCALC - PDEFCALC)
					print('You defended against an enemy, and deflected ' + str(PDEFCALC) + ' damage!')
		else:
			print('Please input the right command.')
	else:
		EXP = EXP + EXPGain
		print('You won the fight! You gained ' + str(EXPGain) + ' EXP! Your current EXP = ' + str(EXP + LVLRequirements) + '.')
		if EXP >= 0: #Level up if statement
			LVL = LVL + 1
			EXP = EXP - LVLRequirements
			print('You leveled up! You are now LVL ' + str(LVL) + '!')
			print('You can upgrade your stats, please input one of them:')
			LVLUPInfo = 'ATK, DEF, HP'
			print(LVLUPInfo)
			LUChoice = True
			while LUChoice == True:
				LVLUPChoice = input().lower()
				if LVLUPChoice == 'atk':
					PATK = PATK + 1
					LUChoice = False
				elif LVLUPChoice == 'def':
					PDEF = PDEF + 1
					LUChoice = False
				elif LVLUPChoice == 'hp':
					PHP = PHP + 2
					LUChoice = False
				else:
					print('Please input the right stat name:')
					print(LVLUPInfo)
		PHPActive = PHP

CharacterChoice()
while LVL < 5:
	BadPlayerChoice()
	FightPhase()

if LVL == 5:
	print('You won the game!')