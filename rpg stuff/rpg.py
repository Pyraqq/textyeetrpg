import random

# Stats
class Levelstats:
	def __init__(self, LVL, LVLRequirements, EXP):
		self.LVL = LVL
		self.LVLRequirements = LVLRequirements
		self.EXP = EXP

levelos = Levelstats(1, 30, -30)

class Characterinfoclass: # Class choice function
	def __init__(self, PATK, PDEF, PHP, PHPActive): 
		self.PATK = PATK
		self.PDEF = PDEF
		self.PHP = PHP
		self.PHPActive = PHPActive

def characterChoice():
	print('Choose your class:')
	classinfo = 'BERSERKER (ATK = 2, DEF = 1, HP = 15), PROTECTOR (ATK = 1, DEF = 2, HP = 15)'
	print(classinfo)
	cchoice = True
	while cchoice == True:
		classchoice = input().lower()
		if classchoice == 'berserker':
			player = Characterinfoclass(2, 1, 15, 15)
			cchoice = False
		elif classchoice == 'protector':
			player = Characterinfoclass(1, 2, 15, 15)
			cchoice = False
		else:
			print('Please input the right class name:')
			print(classinfo)
	return player

# Enemy Choice function
def BadPlayerChoice():
	print('Choose an enemy to fight:')
	enemyinfo = 'RAT (ATK = 1, HP = 7, EXP = 5), GOBLIN (ATK = 2, HP = 12, EXP = 10)'
	print(enemyinfo)
	echoice = True
	while echoice == True:
		enemychoice = input().lower()
		if enemychoice == 'rat':
			enemy = {
			'EATK' : 1,
			'EHP' : 7,
			'EXPGain' : 5,
			'EName' : 'RAT'
			}
			echoice = False
		elif enemychoice == 'goblin':
			enemy = {
			'EATK' : 2,
			'EHP' : 12,
			'EXPGain' : 10,
			'EName' : 'GOBLIN'
			}
			echoice = False
		else:
			print('Please input the right enemy name:')
			print(enemyinfo)
	return enemy

# Fight function
def FightPhase():
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
		fightchoice = input().lower()
		if fightchoice == 'attack': # attack option
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
		elif fightchoice == 'defend': # defend option
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
		print('You won the fight! You gained {0} EXP! Your current EXP = {1}.'.format(str(enemy['EXPGain']), str(levelos.EXP + levelos.LVLRequirements)))
		if levelos.EXP >= 0: # Level up if statement
			levelos.LVL = levelos.LVL + 1
			levelos.LVLRequirements = 25 * levelos.LVL + 2 * levelos.LVL
			levelos.EXP = levelos.EXP - levelos.LVLRequirements
			print('You leveled up! You are now LVL {0}!'.format(str(levelos.LVL)))
			print('Next level up goal is: {0} EXP!'.format(str(levelos.LVLRequirements)))
			print('You can upgrade your stats, please input one of them:')
			lvlupinfo = 'ATK, DEF, HP'
			print(lvlupinfo)
			luchoice = True
			while luchoice == True:
				lvlupchoice = input().lower()
				if lvlupchoice == 'atk':
					player.PATK = player.PATK + 1
					luchoice = False
				elif lvlupchoice == 'def':
					player.PDEF = player.PDEF + 1
					luchoice = False
				elif lvlupchoice == 'hp':
					player.PHP = player.PHP + 2
					luchoice = False
				else:
					print('Please input the right stat name:')
					print(lvlupinfo)
		else:
			print('Next level up goal is: {0} EXP!'.format(str(levelos.LVLRequirements)))
		player.PHPActive = player.PHP

player = characterChoice()
while levelos.LVL < 5:
	enemy = BadPlayerChoice()
	FightPhase()

if levelos.LVL == 5:
	print('You won the game!')