print('Choose your class:')
print('Berserker, Shielder')
EXP = 0
LVL = 1
CChoice = True
while CChoice == True:
	ClassChoice = input()
	if ClassChoice == 'Berserker':
		PATK = 2
		PDEF = 0
		PHP = 15
		CChoice = False
	elif ClassChoice == 'Shielder':
		PATK = 1
		PDEF = 2
		PHP = 20
		CChoice = False
	else:
		print('Please input the right class name:')
print('Choose an enemy to fight:')
print('Rat, Goblin')
EChoice = True
while EChoice == True:
	EnemyChoice = input()
	if EnemyChoice == 'Rat':
		EATK = 1
		PDEF = 1
		PHP = 5
		EXPGain = 5
		EChoice = False
	elif EnemyChoice == 'Goblin':
		EATK = 2
		PDEF = 2
		EHP = 10
		EXPGain = 10
		EChoice = False
	else:
		print('Please input the right enemy name:')
print('What should I do?')
print('attack, defend')