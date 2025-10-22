#Flashcards.py
#Program allows the user to create, modify, and study flashcards from a console window. 
#Created 9/29/2025

from Validated_Input import validated_input
from Validation_Lib import String_Valdiation_Type
import copy
import random

SET_DATA = "SetData"

#Classes:

class Flashcard_Set:
    '''Class to store flashcard set information'''

    def __init__(self, name, entries=None):
        self.name = name
        if entries == None:
            self.entries = []
        else:
            self.entries = entries

    def add_entry(self, entry):
        self.entries.append(entry)

    def descriptor_string(self):
        return f"{self.name} - Terms: {len(self.entries)}"

    def display_entries(self):
        print(f"\nFlashcards in Flashcard Set \"{self.name}\":")
        if len(self.entries) == 0:
            print("No flashcards to display\n")
        else:
            for index, entry in enumerate(self.entries):
                print(f"({index + 1}) {entry.display_string()}")
            print() #for space

        return len(self.entries)

class Entry:
    '''Class to store information for each individual flashcard'''

    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def display_string(self):
        return(f"{self.term}: {self.definition}")

    def save_string(self):
        return(f"{self.term},{self.definition}\n")

    @classmethod
    def entry_from_save_string(cls, string):
        parts = string.split(',')
        return Entry(parts[0], parts[1])

#Functions:

def display_sets():
    '''displays a numbered list of all sets currently in the flashcard_sets list'''

    print() #for space

    if len(flashcard_sets) > 0:
        for index, flashcard_set in enumerate(flashcard_sets):
            print(f"({index + 1}) {flashcard_set.descriptor_string()}")
    else:
        print("No flashcard sets currently saved.")

    return

def add_flashcard_set():
    '''Takes user input to add a new flashcard set and add entries to it'''

    name = validated_input("\nEnter the name of the flashcard set: ", str, string_validation_type=String_Valdiation_Type.ALPHANUMERIC_AND_SPACE)
    name = name.title()

    new_set = Flashcard_Set(name)

    print("\nEnter flashcard information:")
    while True:
        term = validated_input("Enter term (or 'qqq' to finish): ", str)
        if term == 'qqq':
            break
        definition = validated_input("Enter definition: ", str)
        
        new_set.add_entry(Entry(term, definition))

    flashcard_sets.append(new_set)
    print("\nFlashcard set saved!\n")
    return

def edit_flashcard_set():
    '''Allows user to edit flashcard details'''

    print("\nEdit Menu:")
    print("(1) Edit Flashcard Set Name")
    print("(2) Add Flashcards to Flashcard Set")
    print("(3) Edit Flashcards in Flashcard Set")
    print("(4) Remove Flashcards from Flashcard Set")
    print("(5) Cancel")
    edit_option = validated_input("Select an option (1-5): ", int, min_value=1, max_value=5)

    if edit_option != 5:
        display_sets()
        set_index = validated_input(f"\nSelect a set to edit or enter 0 to cancel (0-{len(flashcard_sets)}): ", int, min_value=0, max_value=len(flashcard_sets))

        if set_index != 0:
            set_index -= 1

            match edit_option:
                case 1:
                    #Edit set name
                    name = validated_input("\nEnter a new name for the flashcard set: ", str, string_validation_type=String_Valdiation_Type.ALPHA_AND_SPACE)
                    flashcard_sets[set_index].name = name
                case 2:
                    #Add new flashcards
                    print("\nEnter flashcard information:")
                    while True:
                        term = validated_input("Enter term (or 'qqq' to finish): ", str)
                        if term == 'qqq':
                            break
                        definition = validated_input("Enter definition: ", str)
        
                        flashcard_sets[set_index].add_entry(Entry(term, definition))
                case 3:
                    #Edit flashcard entries
                    while True:
                        total = flashcard_sets[set_index].display_entries()
                        entry_index = validated_input(f"Select a flashcard to edit (1-{total}): ", int, min_value=1, max_value=total) - 1
                        entry = flashcard_sets[set_index].entries[entry_index]

                        print(f"\nCurrent term: {entry.term}")
                        entry.term = validated_input("Enter the new term: ", str)
                        print(f"Current definition: {entry.definition}")
                        entry.definition = validated_input("Enter the new definition: ", str)

                        if not validated_input("Would you like to edit another flashcard? (Y/N): ", bool):
                            break
                case 4:
                    #Remove flashcards
                    while True:
                        total = flashcard_sets[set_index].display_entries()
                        if total > 0:
                            entry_index = validated_input(f"Select a flashcard to remove (1-{total}): ", int, min_value=1, max_value=total) - 1
                            if validated_input("Are you sure? This cannot be undone (Y/N): ", bool):
                                flashcard_sets[set_index].entries.pop(entry_index)

                            print() # for space
                            if not validated_input("Would you like to remove another flashcard? (Y/N): ", bool):
                                break
                        else:
                            break
                case _:
                    raise ValueError("Unexpected value of edit_option")

            print("\nChanges saved!")

    print() #for space
    return

def remove_flashcard_set():
    '''function to delete a flashcard set'''

    if len(flashcard_sets) > 0:

        display_sets()

        user_input = validated_input(f"\nSelect a set to remove or enter 0 to cancel (0-{len(flashcard_sets)}): ", int, min_value=0, max_value=len(flashcard_sets))

        if user_input != 0:
            if validated_input("Are you sure? This action cannot be undone (Y/N): ", bool):
                flashcard_sets.pop(user_input - 1)
    else:
        print("No flashcard sets currently saved.")

    return

def save_flashcard_sets():
    #save flashcard set names in a file for access purposes
    with open(SET_DATA, 'w', encoding='utf-8') as save_file:
        for flashcard_set in flashcard_sets:
            save_file.write(flashcard_set.name + '\n')

    #save flahscard set entries in files named the names of the set
    for flashcard_set in flashcard_sets:
        with open(flashcard_set.name, 'w', encoding='utf-8') as set_file:
            for entry in flashcard_set.entries:
                set_file.write(entry.save_string())

    return

def load_flashcard_sets():
    #load flashcard set name (names of other files with entry info)
    with open(SET_DATA, 'r', encoding='utf-8') as file:
        sets = file.readlines()

    #load entry information from set names
    for line in sets:
        with open(line.strip(), 'r', encoding='utf-8') as file:
            entries = []
            for entry in file.readlines():
                entries.append(Entry.entry_from_save_string(entry.strip()))
            flashcard_sets.append(Flashcard_Set(line.strip(), entries))

    return

def study_flashcard_style():

    if len(flashcard_sets) > 0:

        display_sets()

        user_input = validated_input(f"\nSelect a set to study or enter 0 to cancel (0-{len(flashcard_sets)}): ", int, min_value=0, max_value=len(flashcard_sets))

        if (user_input > 0):
            user_input -= 1

            study_set = copy.deepcopy(flashcard_sets[user_input].entries)

            if validated_input("Would you like to randomize the flashcards? (Y/N): ", bool):
                random.shuffle(study_set)

            print("\nPress Enter to 'flip' the flashcard and again to advance to the next.")
            for flashcard in study_set:
                print() #for space
                input(flashcard.term)
                input(flashcard.definition)

            print("Set complete\n")

    else:
        print("No flashcard sets currently saved.\n")


def study_test_style():
    
    if len(flashcard_sets) > 0:

        display_sets()

        user_input = validated_input(f"\nSelect a set to study or enter 0 to cancel (0-{len(flashcard_sets)}): ", int, min_value=0, max_value=len(flashcard_sets))

        if (user_input > 0):
            user_input -= 1

            study_set = copy.deepcopy(flashcard_sets[user_input].entries)

            if validated_input("Would you like to randomize the flashcards? (Y/N): ", bool):
                random.shuffle(study_set)

            num_correct = 0
            for flashcard in study_set:
                print(f"\n{flashcard.term}: ")
                flashcard_response = input().strip()

                if flashcard.definition == flashcard_response:
                    print("\033[32mCorrect!!\033[0m")
                    num_correct += 1
                else:
                    print("\033[31mIncorrect\033[0m :'(")
                    print(f"Correct answer: {flashcard.definition}")

            print("\nSet complete")
            print(f"Score: {num_correct}/{len(study_set)}\n")

    else:
        print("No flashcard sets currently saved.")

#Begin main code:

flashcard_sets = []

load_flashcard_sets()

#Main menu:
while True:
    print("Main Menu:")
    print("(1) Add New Flashcard Set")
    print("(2) Edit Flashcard Set")
    print("(3) Remove Flashcard Set")
    print("(4) Study Flashcard Set (flashcard mode)")
    print("(5) Study Flashcard Set (test mode)")
    print("(6) Save and Exit")

    user_input = validated_input("Select an option (1-6): ", int, min_value=1, max_value=6)

    match user_input:
        case 1:
            add_flashcard_set()
        case 2:
            edit_flashcard_set()
        case 3:
            remove_flashcard_set()
        case 4:
            study_flashcard_style()
        case 5:
            study_test_style()
        case 6:
            save_flashcard_sets()
            print("\nThank you for using our flashcard program!")
            break
        case _:
            raise ValueError("Unexpected value of user_input")

