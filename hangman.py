from random import choice


hang_dict = {
    'toyota': 'Japan', 'ford': 'USA', 'chevrolet': 'USA', 'honda': 'Japan', 'nissan': 'Japan', 'bmw': 'Germany',
    'mercedes': 'Germany', 'volkswagen': 'Germany', 'audi': 'Germany', 'hyundai': 'South Korea', 'kia': 'South Korea',
    'peugeot': 'France', 'renault': 'France', 'subaru': 'Japan', 'mazda': 'Japan', 'volvo': 'Sweden',
    'fiat': 'Italy', 'porsche': 'Germany', 'lexus': 'Japan', 'jeep': 'USA', 'cadillac': 'USA', 'dodge': 'USA',
    'tesla': 'USA', 'infiniti': 'Japan', 'lincoln': 'USA', 'buick': 'USA', 'chrysler': 'USA', 'acura': 'Japan',
    'lamborghini': 'Italy', 'bentley': 'UK', 'mitsubishi': 'Japan', 'jaguar': 'UK', 'rollsroyce': 'UK', 'mclaren': 'UK',
    'ferrari': 'Italy', 'astonmartin': 'UK', 'landrover': 'UK', 'maserati': 'Italy', 'gmc': 'USA', 'alfaromeo': 'Italy',
    'citroen': 'France', 'skoda': 'Czech Republic', 'mini': 'UK', 'suzuki': 'Japan', 'saab': 'Sweden', 'seat': 'Spain',
    'dacia': 'Romania', 'lancia': 'Italy', 'lotus': 'UK', 'bugatti': 'France', 'koenigsegg': 'Sweden', 'rimac': 'Croatia',
    'pagani': 'Italy', 'smart': 'Germany', 'opel': 'Germany', 'mg': 'UK', 'polestar': 'Sweden', "lada": "Russia", "ram": "USA"
}

possibilities = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def first_replacer(word):
    string1=""
    for i in word:
        string1 += "_"

    return string1

def letter_locator(word, letter):
    indexes = []
    if letter in word:
        lista=list(enumerate(word))
        for i in lista:
            if i[1] == letter:
                indexes.append(i[0])
    return indexes

def replacer(string, letter, index):
    temp_list=list(string)
    for i in index:
        temp_list[i]=letter
    edited_word="".join(temp_list)
    return edited_word

def hanged_man(act_word, counter):
    if counter == 0:
        print("------")
        print("\n\n\n",act_word)
    if counter == 1:
        print("------")
        print("     |")
        print("\n\n\n", act_word)
    if counter == 2:
        print("------")
        print("     |")
        print("     0")
        print("\n\n\n", act_word)
    if counter == 3:
        print("------")
        print("     |")
        print("     0")
        print("    /|")
        print("\n\n\n", act_word)
    if counter == 4:
        print("------")
        print("     |")
        print("     0")
        print("    /|\\")
        print("\n\n\n", act_word)
    if counter == 5:
        print("------")
        print("     |")
        print("     0")
        print("    /|\\")
        print("     |")
        print("    /|")
        print("\n\n\n", act_word)
    if counter == 6:
        print("------")
        print("     |")
        print("     0")
        print("    /|\\")
        print("     |")
        print("    /|\\")
        print("\n\n\n", act_word)
        print("\n\n You're dead!!")

def game():
    print("\n\nWelcome to Car Brand Hangman, let's begin\n\n")
    word = choice(list(hang_dict.keys()))
    guessed_letters = []  # Track all guessed letters
    act_word = first_replacer(word)  # Initial masked word
    counter = 0  # Count of incorrect guesses
    attempts = 6  # Total allowed attempts
    hint_given = False

    while counter < attempts:
        hanged_man(act_word, counter)
        if counter == attempts - 1 and not hint_given:
            hint_request = input("This is your last attempt. Would you like a hint? (yes/no): ").lower()
            if hint_request == "yes":
                print(f"Hint: The brand is from {hang_dict[word]}")
                hint_given = True  # Ensure hint is not offered again
        letter = input("Input a letter: ").lower()

        while letter not in possibilities or letter in guessed_letters:
            if letter in guessed_letters:
                print("You've already guessed that letter.")
            else:
                print("Please input a valid letter.")
            letter = input("Input a letter: ").lower()

        guessed_letters.append(letter)  # Add guessed letter to the list

        if letter in word:
            indexes = letter_locator(word, letter)
            act_word = replacer(act_word, letter, indexes)
            # Check if the word is fully guessed
            if "_" not in act_word:
                print(f"Congratulations! You've guessed the car brand: {word}")
                break
        else:
            counter += 1  # Increment only for incorrect guesses

        if counter == attempts:
            hanged_man(act_word, counter)
            print(f"You've run out of attempts! The brand was: {word}")



game()




