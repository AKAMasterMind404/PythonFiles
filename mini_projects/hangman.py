import random

number_of_lives = len('hangman')
list_of_words = ['Tummbbad']

selected_word = list_of_words[random.randint(0, len(list_of_words) - 1)].lower()
current_stage = list('_' * len(selected_word))
# print(current_stage)

completed = False

while number_of_lives and ''.join(current_stage) != selected_word:
    print(''.join(current_stage))
    a = input('\nGuess an alphabet:')
    if a in selected_word:
        current_stage[selected_word.index(a)] = a
    else:
        number_of_lives -= 1
        print('Oops! This alphabet doesnt exist in the word!')
        print('Lives left:{}'.format(number_of_lives))

print('You lost!') if not number_of_lives else print('You Win!')
