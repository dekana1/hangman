import random
print("H A N G M A N")

words = ['python', 'java', 'kotlin', 'javascript']
selected_word = random.choice(words)
hidden_word = list("-" * len(selected_word))

tries = 8
while "-" in hidden_word:
    if tries > 0:
        print()
        print("".join(hidden_word))
        character_guess = input("Input a letter: ").strip()
        indexes = [i for i, letter in enumerate(selected_word) if letter == character_guess]
        if character_guess in selected_word:
            for x in indexes:
                if hidden_word[x] == "-":
                    hidden_word[x] = character_guess
                else:
                    tries -= 1
                    print("No improvements")
                    break

        else:
            tries -= 1
            print("No such letter in the word")

    else:
        print("You are hanged!")
        break
else:
    print(hidden_word)
    print("You guessed the word!")
    print("You survived!")
