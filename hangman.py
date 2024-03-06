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

capital_cities_dict = {
    'france': 'paris', 'germany': 'berlin', 'italy': 'rome', 'spain': 'madrid', 'united kingdom': 'london',
    'japan': 'tokyo', 'united states': 'washingtondc.', 'canada': 'ottawa', 'australia': 'canberra',
    'brazil': 'brasilia', 'china': 'beijing', 'russia': 'moscow', 'india': 'newdelhi', 'egypt': 'cairo',
    'south africa': 'pretoria'
}

animals_list = [
    'lion', 'tiger', 'elephant', 'giraffe', 'panther', 'leopard', 'zebra', 'rhinoceros', 'hippopotamus', 'kangaroo',
    'panda', 'koala', 'wolf', 'bear', 'cheetah', 'buffalo', 'alligator', 'crocodile', 'eagle', 'owl', 'falcon',
    'parrot', 'shark', 'dolphin', 'whale'
]

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

def car_game():
    print("\n\nWelcome to Car Brand Hangman, let's begin\n\n")
    word = choice(list(hang_dict.keys()))
    guessed_letters = []
    act_word = first_replacer(word)
    counter = 0
    attempts = 6
    hint_given = False

    while counter < attempts:
        hanged_man(act_word, counter)
        if counter == attempts - 1 and not hint_given:
            hint_request = input("This is your last attempt. Would you like a hint? (yes/no): ").lower()
            if hint_request == "yes":
                print(f"Hint: The brand is from {hang_dict[word]}")
                hint_given = True
        letter = input("Input a letter: ").lower()

        while letter not in possibilities or letter in guessed_letters:
            if letter in guessed_letters:
                print("You've already guessed that letter.")
            else:
                print("Please input a valid letter.")
            letter = input("Input a letter: ").lower()

        guessed_letters.append(letter)

        if letter in word:
            indexes = letter_locator(word, letter)
            act_word = replacer(act_word, letter, indexes)

            if "_" not in act_word:
                print(f"Congratulations! You've guessed the car brand: {word}")
                break
        else:
            counter += 1

        if counter == attempts:
            hanged_man(act_word, counter)
            print(f"You've run out of attempts! The brand was: {word}")



def capital_city_game():
    print("\n\nWelcome to the Capital Cities Hangman, let's begin\n\n")
    country, city = choice(list(capital_cities_dict.items()))
    guessed_letters = []
    act_city = first_replacer(city)
    counter = 0
    attempts = 6
    hint_given = False

    while counter < attempts:
        hanged_man(act_city, counter)
        if counter == attempts - 1 and not hint_given:
            hint_request = input("This is your last attempt. Would you like another hint? (yes/no): ").lower()
            if hint_request == "yes":

                print(f"Hint: The capital city of {country}")
                hint_given = True
        letter = input("Input a letter: ").lower()

        while letter not in possibilities or letter in guessed_letters:
            if letter in guessed_letters:
                print("You've already guessed that letter.")
            else:
                print("Please input a valid letter.")
            letter = input("Input a letter: ").lower()

        guessed_letters.append(letter)

        if letter in city.lower():
            indexes = letter_locator(city.lower(), letter)
            act_city = replacer(act_city, letter, indexes)

            if "_" not in act_city:
                print(f"Congratulations! You've guessed the capital city: {city}")
                break
        else:
            counter += 1

        if counter == attempts:
            hanged_man(act_city, counter)
            print(f"You've run out of attempts! The capital city was: {city}")

def animal_game():
    print("\n\nWelcome to the Animal Hangman, let's begin\n\n")
    animal = choice(animals_list)
    guessed_letters = []
    act_animal = first_replacer(animal)
    counter = 0
    attempts = 6

    while counter < attempts:
        hanged_man(act_animal, counter)
        letter = input("Input a letter: ").lower()

        while letter not in possibilities or letter in guessed_letters:
            if letter in guessed_letters:
                print("You've already guessed that letter.")
            else:
                print("Please input a valid letter.")
            letter = input("Input a letter: ").lower()

        guessed_letters.append(letter)

        if letter in animal:
            indexes = letter_locator(animal, letter)
            act_animal = replacer(act_animal, letter, indexes)

            if "_" not in act_animal:
                print(f"Congratulations! You've guessed the animal: {animal.capitalize()}")
                break
        else:
            counter += 1

        if counter == attempts:
            hanged_man(act_animal, counter)
            print(f"You've run out of attempts! The animal was: {animal.capitalize()}")


def final_game():
    game = input("What game would you like to play (press 1, 2 or 3) \n (1) car game\n (2) capital city game\n (3) animal game\n\n write here: ")
    if game == "1":
        car_game()
    if game == "2":
        capital_city_game()
    if game == "3":
        animal_game()


final_game()