import random
from hangman_ascii import stages, logo ## or use * for importing every thing
from hangman_words import word_list

# word_list = ["aardvark", "baboon", "camel"]


print(logo)

chosen_letter = random.choice(word_list)

display = []

length = len(chosen_letter)

for x in range(length):
    display.append('_') 

print(" ".join(display) )

end_of_game = True

count = 0

while end_of_game :
    guess = input('Guess the letter: ')
    if guess in display:
        print(f'you already guessed the letter {guess} ')
    else:
        for position in range(length):
            if chosen_letter[position] == guess:
                display[position] = guess
        if guess in chosen_letter:
            print(stages[count])
        if guess not in chosen_letter:
            count += 1
            print(stages[count])
            print('word not match and you lose one life')
        print(f'{" ".join(display)}')
        if count == 6:
            print('you loose')
            # break
            end_of_game = False
        if "_" not in display:
            end_of_game = False
            print('you win')

