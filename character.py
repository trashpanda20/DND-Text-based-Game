#game that plays dnd for you but offers you dialogue

import mysql.connector
import random
import json

#mysql.connector.connect(host='localhost',
                        #database='DND_Spells',
                        #user='root',
                        #password='dndspells')

class character:
    def __init__(self, name, age, race, role, level):
        self. name = name
        self.age = age
        self.race = race
        self.role = role
        self.level = level
        self.hp = self.hp_roll()
        self.ac = self.armor_class()

        #we want to role a set of numbers for the hp.
        #role a set for the AC as well but based on the class
        #let tehm choose a class.
    ROLES = {
        "Warlock": {"Description": ("Warlocks are mystic beings who use the ancient arts of magic. It's a closed practice, so most don't understand the ways of those who practice. Due to the finicky nature of magic, Melee weapons are not typical. Warlocks only use magic."), "hp_range": (10,20), "armor": (13)},
        "Guardian": {"Description": ("Guardians are your knights. They fight for the sense of righteousness that they hold within themselves. They are the very definition of protecting others who cannot protect themselves. The practice the way of the ancients while altering it to be better fit for melee combat. "), "hp_range": (13,20), "armor": (16)},
        "Outlaw": {"Description": ("Outlaws are those who tend to be on the wrong side of the law, though there are alwasy exceptions. For those who have no interest in magic or don't believe in it. They tend to be knights, theives, or even assassains. The way of the outlaw is to fight with weapons, not 'illusions'."), "hp_range": (11,18), "armor": (15)}
    }
    def hp_roll(self):
        hp_range = self.ROLES[self.role]["hp_range"]
        return random.randint(hp_range[0],hp_range[1])  
     
    def armor_class(self):
        armor_class = self.ROLES[self.role]["armor"]
        return armor_class
    
    def __str__(self):
        return(f"Character: {self.name}\n"
               f"Age: {self.age}\n"
               f"Race: {self.race}\n"
               f"Role: {self.role}\n"
               f"Level: 1\n"
               f"HP: {self.hp}\n"
               f"Armor Class: {self.ac}")
    
    def to_dict(self):
        return{
            "name": self.name,
            "age": self.age,
            "race": self.race,
            "role": self.role,
            "level": self.level,
            "hp": self.hp,
            "ac": self.ac
        }
    
def from_dict(character, data):
        return character(data["name"], data["age"], data["race"], data["role"], data["level"])

def creating():
        name = input("What is your name, mysterious adventurer? \n")
        race = input("What kind of creature are you? \n")
        age =  input(f"Ah, yes. I see now. How old might you be? I always seem to never be able to tell with {race}. \n")
        for role,details in character.ROLES.items():
            print(f"{role}:")
            print(details["Description"])
        role = input("Which practice do you subscribe to? \n").capitalize()
        level = 1
        print(f"Every character starts out at {level}. \n")

        Character = character(name, age, race, role, level)
        return Character

def save_characters(characters, filename="characters.json"):
    
        with open(filename, "w") as file:
            json.dump([char.to_dict() for char in characters], file, indent=4)
        print(f"Characters saved to {filename}.")

def load_characters(filename="characters.json"):
        
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                return [character.from_dict(char_data) for char_data in data]
        except FileNotFoundError:
            print("No saved characters found. Starting with an empty list.")
            return []
        
    
def main_menu():
        characters = load_characters()
        
        while True:
            print("\n--- Main Menu ---")
            print("1. Create a new character")
            print("2. View saved characters")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                new_character = creating()
                characters.append(new_character)
                save_characters(characters)
                print("\nCharacter created and saved!")
            elif choice == "2":
                if characters:
                    print("\nSaved Characters:")
                    for i, char in enumerate(characters, start=1):
                        print(f"\nCharacter {i}:")
                        print(char)
                else:
                    print("\nNo characters found.")
            elif choice == "3":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
