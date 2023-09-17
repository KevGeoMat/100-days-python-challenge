import random

words = ["arise", "puppy", "firefighter", "question", "flower"]
cur_word = random.choice(words)
print(cur_word)
guess = input("Guess a letter: ").lower()

no_let = len(cur_word)
val =[]

for i in range(no_let):
    if cur_word[i] == guess:
        val.append(guess)
    else:
        val.append("_")

print(val)

