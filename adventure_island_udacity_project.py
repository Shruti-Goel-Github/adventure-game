import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro(creature):
    print_pause("You find yourself standing in an open field, filled with"
                " grass and yellow wildflowers.")
    print_pause("Rumor has it that a {} is somewhere around here, and"
                " has been terrifying the nearby village.".format(creature))
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)"
                " dagger.")


def first_door(list_sword, creature):
    print_pause("You approach the door of the house.\n")
    print_pause("You are about to knock when the door opens and out steps"
                " a {}.\n".format(creature))
    print_pause("Eep! This is the {}'s house!\n".format(creature))
    print_pause("The {} attacks you!\n".format(creature))
    if "golden_sword" not in list_sword:
        choice_first_door = input("You feel a bit under-prepared for this, "
                                  "what with only having a tiny dagger.\n"
                                  "Would you like to (1) fight or (2) run "
                                  "away?")
        if choice_first_door == '1':
            print_pause("You do your best...\n")
            print_pause("but your dagger is no match for the {}.\n"
                        .format(creature))
            print_pause("You have been defeated!\n")
            play_again()
        elif choice_first_door == '2':
            print_pause("You run back into the field. Luckily, you don't seem "
                        "to have been followed.")
            choice(list_sword, creature)
        else:
            first_door(list_sword, creature)
    else:
        choice_first_door = input("Would you like to (1) fight or (2) run"
                                  " away?")
        if choice_first_door == '1':
            print_pause("As the {} moves to attack, you unsheath your new "
                        "sword.\n".format(creature))
            print_pause("The Sword of Ogoroth shines brightly in your hand as "
                        "you brace yourself for the attack.\n")
            print_pause("But the {} takes one look at your shiny new toy and "
                        "runs away!\n".format(creature))
            print_pause("You have rid the town of the {}. You are "
                        "victorious!\n".format(creature))
            play_again()
        if choice_first_door == '2':
            print_pause("You run back into the field. Luckily,"
                        " you don't seem to"
                        " have been followed.")
            choice(list_sword, creature)


def second_door(list_sword, creature):
    print_pause("You peer cautiously into the cave.")
    if "golden_sword" not in list_sword:
        print_pause("It turns out to be only a very small cave.\n"
                    "Your eye catches a glint of metal behind a rock.\n"
                    "You have found the magical Sword of Ogoroth!\n"
                    "You discard your silly old dagger and take "
                    "the sword with you.\n"
                    "You walk back out to the field.\n")
        list_sword.append("golden_sword")
        choice(list_sword, creature)
    else:
        print_pause("You've been here before, and gotten all "
                    "the good stuff.\n"
                    "It's just an empty cave now.\n"
                    "You walk back out to the field.\n")
        choice(list_sword, creature)


def choice(list_sword, creature):
    print_pause("Enter 1 to knock on the door of the house.\n"
                "Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice_val = input("(Please enter 1 or 2).\n")
    if choice_val == '1':
        first_door(list_sword, creature)
    elif choice_val == '2':
        second_door(list_sword, creature)
    else:
        choice(list_sword, creature)


def play_again():
    play_choice = input("Would you like to play again y/n?")
    if play_choice.lower() == 'y':
        print_pause("Excellent! Restarting the game ...")
        main_run()
    elif play_choice.lower() == 'n':
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()


def main_run():
    list_sword = []
    random_choice = random.choice(["wicked fairie", "pirates",
                                   "dragon", "gorgon"])
    intro(random_choice)
    choice(list_sword, random_choice)


main_run()
