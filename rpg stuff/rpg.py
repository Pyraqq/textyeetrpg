import random

#Beginning question.
print('Choose your class:')
print('BERSERKER (ATK = 2, DEF = 1, HP = 15), PROTECTOR (ATK = 1, DEF = 2, HP = 20)')

#Stats
EXP = 0
LVL = 1

#Class Choice
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

#Enemy Choice
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
		EXP = 15
		EXPGain = 10
		EChoice = False
	else:
		print('Please input the right enemy name:')
		
#Fight code
def FightPhase():
	global PATK
	global PHP
	global PHP
	global EATK
	global EHP
	global EXPGain
	while EHP > 0:
		print('What should I do? Current Enemy: ' + EnemyChoice + ' Enemy HP: ' + str(EHP) + ' Your HP: ' + str(PHP))
		print('ATTACK, DEFEND')
		PATKCALC = 0 #Your Attack value
		PDEFCALC = 0 #Your Defense value
		EATKCALC = 0 #Enemy's Attack value
		FightChoice = input()
		if FightChoice == 'ATTACK':
			PATKCALC = random.randint(0, PATK)
			if PATKCALC == 0:
				EATKCALC = random.randint(0, EATK)
				PHP = PHP - EATKCALC
				print('You missed your attack, and the enemy hit you for ' + str(EATKCALC) + ' damage!')
			else:
				EHP = EHP - PATKCALC
				print('You hit your an enemy, and dealt ' + str(PATKCALC) + ' damage!')
				PHP = PHP - EATKCALC
				print('The enemy dealt ' + str(EATKCALC) + ' damage!')
		elif FightChoice == 'DEFEND':
			PDEFCALC = random.randint(0, PDEF)
			if PDEFCALC == 0:
				PHP = PHP - EATKCALC
				print('You were too slow, and the enemy hit you for ' + str(EATKCALC) + ' damage!')
			else:
				PHP = PHP - (PATKCALC - PDEFCALC)
				print('You defended against an enemy, and deflected ' + str(PDEFCALC) + ' damage!')
		else:
			print('Please input the right command:')
			
FightPhase() #Calling the fight phase
