import random
import time
class Poke_a_Greg:

	def __init__ (self, HP, move1, move1ACC, move1SP, move1POWER, move2, move2ACC, move2SP, move2POWER, move3, move3ACC, move3SP, move3POWER, name):
		self.HP = HP
		self.move1 = move1
		self.move1ACC = move1ACC
		self.move1SP = move1SP
		self.move1POWER = move1POWER
		self.move2 = move2
		self.move2ACC = move2ACC
		self.move2SP = move2SP
		self.move2POWER = move2POWER
		self.move3 = move3
		self.move3ACC = move3ACC
		self.move3SP = move3SP
		self.move3POWER = move3POWER
		self.name = name

	def p():
		move = "Scratch"
	def battle(self, enemy):
		gameover = False
		while gameover == False:

			while self.HP > 0 and enemy.HP > 0:
				print(enemy.name + " is at " + str(enemy.HP) + " health, and " + self.name + " is at " + str(self.HP) + " health.\n")
				print("What do you want " + self.name + " to use?")
				print("Your choices are:\n" + self.move1 + "\n" + self.move2 + "\n" + self.move3 + "\n")
				move = input("> ")
				move = move.lower()
				com_r_move = (random.randint(1, 3))
				if move == self.move1.lower():
					if com_r_move == 1:
						if self.move1SP > enemy.move1SP:
							moveACC = (random.randint(1, 100))
							if moveACC <= self.move1ACC:
								enemy.HP = enemy.HP - self.move1POWER
								if enemy.HP <= 0:
									return "\n" + self.name + " used " + self.move1 + " and was succsessful! " + enemy.name + " passed out! You win!\n"
								else:
									print("\n" + self.name + " used " + self.move1 + " and was succsessful!\n")
							else:
								enemy.HP = enemy.HP
								print("\n" + self.name + " used " + self.move1 + " and was unsucsessful!\n")
							com_moveACC = (random.randint(1, 100))
							if com_moveACC <= enemy.move1ACC:
								self.HP = self.HP - enemy.move1POWER
								if self.HP <= 0:
									return enemy.name + " used " + enemy.move1 + " and was succsessful! " + self.name + " passed out! You lose!\n"
								else:
									print(enemy.name + " used " + enemy.move1 + " and was succsessful!\n")
							else:
								print(enemy.name + " used " + enemy.move1 + " and was unsucsessful!\n")
								self.HP = self.HP
						else:
							com_moveACC = (random.randint(1, 100))
							if com_moveACC <= enemy.move1ACC:
								self.HP = self.HP - enemy.move1POWER
								if self.HP <= 0:
									return enemy.name + " used " + enemy.move1 + " and was succsessful! " + self.name + " passed out! You lose!\n"
								else:
									print(enemy.name + " used " + enemy.move1 + " and was succsessful!\n")
							else:
								print(enemy.name + " used " + enemy.move1 + " and was unsucsessful!\n")
								self.HP = self.HP
							moveACC = (random.randint(1, 100))
							if moveACC <= self.move1ACC:
								enemy.HP = enemy.HP - self.move1POWER
								if enemy.HP <= 0:
									return "\n" + self.name + " used " + self.move1 + " and was succsessful! " + enemy.name + " passed out! You win!\n"
								else:
									print("\n" + self.name + " used " + self.move1 + " and was succsessful!\n")
							else:
								enemy.HP = enemy.HP
								print("\n" + self.name + " used " + self.move1 + " and was unsucsessful!\n")


				elif move == self.move2.lower():
					if com_r_move == 2:
						if self.move2SP > enemy.move2SP:
							moveACC = (random.randint(1, 100))
							if moveACC <= self.move2ACC:
								enemy.HP = enemy.HP - self.move2POWER
								if enemy.HP <= 0:
									return "\n" + self.name + " used " + self.move2 + " and was succsessful! " + enemy.name + " passed out! You win!\n"
								else:
									print("\n" + self.name + " used " + self.move2 + " and was succsessful!\n")
							else:
								enemy.HP = enemy.HP
								print("\n" + self.name + " used " + self.move2 + " and was unsucsessful!\n")
							com_moveACC = (random.randint(1, 100))
							if com_moveACC <= enemy.move2ACC:
								self.HP = self.HP - enemy.move2POWER
								if self.HP <= 0:
									return enemy.name + " used " + enemy.move2 + " and was succsessful! " + self.name + " passed out! You lose!\n"
								else:
									print(enemy.name + " used " + enemy.move2 + " and was succsessful!\n")
							else:
								print(enemy.name + " used " + enemy.move2 + " and was unsucsessful!\n")
								self.HP = self.HP
						else:
							com_moveACC = (random.randint(1, 100))
							if com_moveACC <= enemy.move2ACC:
								self.HP = self.HP - enemy.move2POWER
								if self.HP <= 0:
									return enemy.name + " used " + enemy.move2 + " and was succsessful! " + self.name + " passed out! You lose!\n"
								else:
									print(enemy.name + " used " + enemy.move2 + " and was succsessful!\n")
							else:
								print(enemy.name + " used " + enemy.move2 + " and was unsucsessful!\n")
								self.HP = self.HP
							moveACC = (random.randint(1, 100))
							if moveACC <= self.move2ACC:
								enemy.HP = enemy.HP - self.move2POWER
								if enemy.HP <= 0:
									return "\n" + self.name + " used " + self.move2 + " and was succsessful! " + enemy.name + " passed out! You win!\n"
								else:
									print("\n" + self.name + " used " + self.move2 + " and was succsessful!\n")
							else:
								enemy.HP = enemy.HP
								print("\n" + self.name + " used " + self.move2 + " and was unsucsessful!\n")


				elif move == self.move3.lower():
					if com_r_move == 3:
						if self.move3SP > enemy.move3SP:
							moveACC = (random.randint(1, 100))
							if moveACC <= self.move3ACC:
								enemy.HP = enemy.HP - self.move3POWER
								if enemy.HP <= 0:
									return "\n" + self.name + " used " + self.move3 + " and was succsessful! " + enemy.name + " passed out! You win!\n"
								else:
									print("\n" + self.name + " used " + self.move3 + " and was succsessful!\n")
							else:
								enemy.HP = enemy.HP
								print("\n" + self.name + " used " + self.move3 + " and was unsucsessful!\n")
							com_moveACC = (random.randint(1, 100))
							if com_moveACC <= enemy.move3ACC:
								self.HP = self.HP - enemy.move3POWER
								if self.HP <= 0:
									return enemy.name + " used " + enemy.move3 + " and was succsessful! " + self.name + " passed out! You lose!\n"
								else:
									print(enemy.name + " used " + enemy.move3 + " and was succsessful!\n")
							else:
								print(enemy.name + " used " + enemy.move3 + " and was unsucsessful!\n")
								self.HP = self.HP
						else:
							com_moveACC = (random.randint(1, 100))
							if com_moveACC <= enemy.move3ACC:
								self.HP = self.HP - enemy.move3POWER
								if self.HP <= 0:
									return enemy.name + " used " + enemy.move3 + " and was succsessful! " + self.name + " passed out! You lose!\n"
								else:
									print(enemy.name + " used " + enemy.move3 + " and was succsessful!\n")
							else:
								print(enemy.name + " used " + enemy.move3 + " and was unsucsessful!\n")
								self.HP = self.HP
							moveACC = (random.randint(1, 100))
							if moveACC <= self.move3ACC:
								enemy.HP = enemy.HP - self.move3POWER
								if enemy.HP <= 0:
									return "\n" + self.name + " used " + self.move3 + " and was succsessful! " + enemy.name + " passed out! You win!\n"
								else:
									print("\n" + self.name + " used " + self.move3 + " and was succsessful!\n")
							else:
								enemy.HP = enemy.HP
								print("\n" + self.name + " used " + self.move3 + " and was unsucsessful!\n")
				else:
					print("That's not a valid input! (Check your spelling)")
	def move():
		return


Kyle = Poke_a_Greg(100, "Scratch", 90, 35, 10, "Sneeze", 67, 15, 14, "Fart", 38, 8, 22, "Christmas Kyle")
Carter = Poke_a_Greg(100, "Slap", 46, 28, 20, "Bad Breath", 25, 22, 35, "Power Punch", 30, 10, 30, "Clueless Carter")
Kenny = Poke_a_Greg(100, "Kick", 80, 40, 12, "Side Kick", 55, 20, 18, "Headbutt", 12, 5, 60, "Halloween Kenny")
print(Kyle.battle(Carter))
print(Kyle.battle(Kenny))