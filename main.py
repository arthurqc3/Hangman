import random
import os
from hangman_art import stages, logo
from hangman_words import word_list

guessed = ""
end_of_game = False    
display = []                            # Display para as palavras
chosen_word = random.choice(word_list)  # Escolher palavra aleatoria
word_lenght = len(chosen_word)          # Receber tamanho da palavra aleatória
lives = 6                               # Vidas 

for char in list(chosen_word):
	display += "_"

print(logo)
print(f"Bem vindo(a) ao jogo da forca, você tem {lives} vidas, Boa Sorte!")
print(stages[lives])

# Começo do jogo

while not end_of_game:	
	print(f"{' '.join(display)}")

	guess = input("Escreva uma letra: \n").lower()
	os.system('clear')

	if guess in guessed:
		print(f"A letra {guess.upper()} já foi escolhida")

	for position in range(word_lenght):
		char = chosen_word[position]
		if char == guess:
			display[position] = guess

	if guess not in chosen_word and guess != guessed:
		lives -= 1
		print(f"A letra {guess.upper()} não faz parte da palavra, você perdeu uma vida agora tem {lives} no total ")
		if lives == 0:             # Verificar Derrota quando lives chegar em zero
			print(f"\nA palavra era {chosen_word.upper()}")
			print("Você perdeu :(")
			end_of_game = True  

	if "_" not in display:         # Verificar vitoria quando
		print(f"\nA palavra era {chosen_word.upper()}")
		print("Você ganhou :D")       # Não tiver "_" no display
		end_of_game = True
	
	print(stages[lives])
	guessed = guess