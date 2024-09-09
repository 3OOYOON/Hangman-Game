import random

dictionaryFile = "phrase.txt"

unknown = ''
max_guesses = 15
guess_history = 0

chosen_phrase = [] 
f = open('phrase.txt')
for line in f:
    chosen_phrase.append(line)
chosen_phrase = random.choice(chosen_phrase)

words = chosen_phrase.split()      
for word in words:                                                     
    unknown = unknown + '_' * len(word)
    unknown = unknown + ' '
print(unknown)    

guessed = ''
letters = []

new_unknown = ''.join(chosen_phrase) 
chosen_phrase_list = list(chosen_phrase.lower())  # Convert the chosen phrase to lowercase

while unknown != chosen_phrase:
    if '_' not in unknown: 
        print('Bravo!!! You Won!')    
        break

    guess = input('What is your guess? Your guess has to be a letter.').lower()  # Convert the input to lowercase
    for letter in chosen_phrase_list:  # Use the lowercase version of the chosen phrase
        letters.append(letter)

    guess_history = guess_history + 1 
    new_unknown = ''

    for i in range(len(chosen_phrase)):
        if guess == chosen_phrase_list[i]:
            new_unknown = new_unknown + guess
        else:
            new_unknown = new_unknown + unknown[i]
    unknown = new_unknown
    print(unknown)  

    if guess in letters:
        new_unknown = [(chosen if chosen == guess else blank) for chosen, blank in zip(chosen_phrase_list, unknown)]
        unknown = new_unknown
        guessed = str(new_unknown)
    elif guess_history >= max_guesses:
        print('Bummer. Better luck next time')
        print('The phrase was:')
        print(chosen_phrase)
        break
    else:
        print('That letter was not in the phrase, try again')