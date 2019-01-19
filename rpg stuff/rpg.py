import random

#Stats
class LevelStats:
	def __init__(self, LVL, LVLRequirements, EXP):
		self.LVL = LVL
		self.LVLRequirements = LVLRequirements
		self.EXP = EXP

LevelOS = LevelStats(1, 30, -30)

class CharacterInfoClass: #Class choice function
	def __init__(self, PATK, PDEF, PHP, PHPActive): 
		self.PATK = PATK
		self.PDEF = PDEF
		self.PHP = PHP
		self.PHPActive = PHPActive

def CharacterChoice():
	print('Choose your class:')
	ClassInfo = 'BERSERKER (ATK = 2, DEF = 1, HP = 15), PROTECTOR (ATK = 1, DEF = 2, HP = 15)'
	print(ClassInfo)
	CChoice = True
	while CChoice == True:
		ClassChoice = input().lower()
		if ClassChoice == 'berserker':
			Player = CharacterInfoClass(2, 1, 15, 15)
			CChoice = False
		elif ClassChoice == 'protector':
			Player = CharacterInfoClass(1, 2, 15, 15)
			CChoice = False
		else:
			print('Please input the right class name:')
			print(ClassInfo)
	return Player

class BadPlayerInfoClass:
	def __init__(self, EATK, EHP, EXPGain, EName):
		self.EATK = EATK
		self.EHP = EHP
		self.EXPGain = EXPGain
		self.EName = EName

#Enemy Choice function
def BadPlayerChoice():
	print('Choose an enemy to fight:')
	EnemyInfo = 'RAT (ATK = 1, HP = 7, EXP = 5), GOBLIN (ATK = 2, HP = 12, EXP = 10)'
	print(EnemyInfo)
	EChoice = True
	while EChoice == True:
		EnemyChoice = input().lower()
		if EnemyChoice == 'rat':
			Enemy = BadPlayerInfoClass(1, 7, 5, 'RAT')
			EChoice = False
		elif EnemyChoice == 'goblin':
			Enemy = BadPlayerInfoClass(2, 12, 10, 'GOBLIN')
			EChoice = False
		else:
			print('Please input the right enemy name:')
			print(EnemyInfo)
	return Enemy

#Fight function
def FightPhase():
	while Enemy.EHP > 0:
		if Player.PHPActive <= 0:
			print('You died!')
			CharacterChoice()
			break
		print('What should I do? Current Enemy: ' + Enemy.EName.upper() + ', Enemy HP: ' + str(Enemy.EHP) + ', Your HP: ' + str(Player.PHPActive) + '/' + str(Player.PHP))
		print('ATTACK, DEFEND')
		PATKCALC = 0 #Your Attack value
		PDEFCALC = 0 #Your Defense value
		EATKCALC = 0 #Enemy's Attack value
		FightChoice = input().lower()
		if FightChoice == 'attack': #attack option
			PATKCALC = random.randint(0, Player.PATK)
			EATKCALC = random.randint(0, Enemy.EATK)
			if PATKCALC == 0:
				Player.PHPActive = Player.PHPActive - EATKCALC
				print('You missed your attack, and the enemy hit you for ' + str(EATKCALC) + ' damage!')
			else:
				Enemy.EHP = Enemy.EHP - PATKCALC
				print('You hit your an enemy, and dealt ' + str(PATKCALC) + ' damage!')
				Player.PHPActive = Player.PHPActive - EATKCALC
				print('The enemy dealt ' + str(EATKCALC) + ' damage!')
		elif FightChoice == 'defend': #defend option
			PDEFCALC = random.randint(0, Player.PDEF)
			EATKCALC = random.randint(0, Enemy.EATK)
			if PDEFCALC == 0:
				Player.PHPActive = Player.PHPActive - EATKCALC
				print('You were too slow, and the enemy hit you for ' + str(EATKCALC) + ' damage!')
			else:
				if PDEFCALC > EATKCALC:
					PDEFCALC = EATKCALC
					Player.PHPActive = Player.PHPActive - (EATKCALC - PDEFCALC)
					print('You defended against an enemy, and deflected ' + str(PDEFCALC) + ' damage!')
				else:
					Player.PHPActive = Player.PHPActive - (EATKCALC - PDEFCALC)
					print('You defended against an enemy, and deflected ' + str(PDEFCALC) + ' damage!')
		else:
			print('Please input the right command.')
	else:
		LevelOS.EXP = LevelOS.EXP + Enemy.EXPGain
		print('You won the fight! You gained ' + str(Enemy.EXPGain) + ' EXP! Your current EXP = ' + str(LevelOS.EXP + LevelOS.LVLRequirements) + '.')
		if LevelOS.EXP >= 0: #Level up if statement
			LevelOS.LVL = LevelOS.LVL + 1
			LevelOS.LVLRequirements = 25 * LevelOS.LVL + 2 * LevelOS.LVL
			LevelOS.EXP = LevelOS.EXP - LevelOS.LVLRequirements
			print('You leveled up! You are now LVL ' + str(LevelOS.LVL) + '!')
			print('Next level up goal is: ' + str(LevelOS.LVLRequirements) + ' EXP!')
			print('You can upgrade your stats, please input one of them:')
			LVLUPInfo = 'ATK, DEF, HP'
			print(LVLUPInfo)
			LUChoice = True
			while LUChoice == True:
				LVLUPChoice = input().lower()
				if LVLUPChoice == 'atk':
					Player.PATK = Player.PATK + 1
					LUChoice = False
				elif LVLUPChoice == 'def':
					Player.PDEF = Player.PDEF + 1
					LUChoice = False
				elif LVLUPChoice == 'hp':
					Player.PHP = Player.PHP + 2
					LUChoice = False
				else:
					print('Please input the right stat name:')
					print(LVLUPInfo)
		else:
			print('Next level up goal is: ' + str(LevelOS.LVLRequirements) + ' EXP!')
		Player.PHPActive = Player.PHP

Player = CharacterChoice()
while LevelOS.LVL < 5:
	Enemy = BadPlayerChoice()
	FightPhase()

if LevelOS.LVL == 5:
	print('You won the game!')