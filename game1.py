import random

def calculate_damage(current_hp, damage):
	return max(0, current_hp - damage)

def is_game_over(hp, score):
	return hp <= 0 or score >= 100

health = 100
score = 0

while True:
	print(f"HP: {health}")
	print(f"Score: {score}")
	print("1. Explore")
	print("2. Rest")
	print("3. Quit")

	action = input("Choose an action: ")

	if action == "1":
		if random.choice(("trap", "treasure")) == "trap":
			damage = random.randint(10, 25)
			health = calculate_damage(health, damage)
			print(f"You encountered a trap and took {damage} damage.")
		else:
			score += 20
			print("You found treasure and gained 20 score.")
	elif action == "2":
		health = min(100, health + 15)
		score -= 5
		print("You rested and recovered 15 HP.")
	elif action == "3":
		break

	if is_game_over(health, score):
		break

if score >= 100:
	print("You won!")
elif health <= 0:
	print("You lost because you ran out of HP.")
else:
	print("You quit early.")
