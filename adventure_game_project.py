import time
import random
import sys


def print_pause(message_to_print):
    print(message_to_print, "\n")
    time.sleep(3)


def start_game():
    items = []
    print_pause(
        "As a young high school student in todays world, life is filled with "
        "decisions, that can make or break a kid.")
    print_pause(
        "Everyday after school as the bell rings, a young student must look "
        "past all of his friends getting picked up and ponder about his "
        "everyday adventure.")
    print_pause("'Dam sometimes I really can't stand walking...'")
    print_pause(
        "The fate of the student lies in your hands. Please choose wisely...")
    while True:
        option = input("What are you going to do after school?\n"
                       "1. Kick it with friends and OG's.\n"
                       "2. Go home ASAP.\n"
                       "3. Head to the courts to play basketball.\n")
        if option == '1':
            og_decision(items)
        elif option == '2':
            head_home(items)
        elif option == '3':
            play_basketball(items)
        if option not in ('1', '2', '3'):
            print_pause(
                "Not an appropriate choice. Please choose '1', '2', or '3'")
        else:
            break


def og_decision(items):
    print_pause(
        "As you leave school and begin your journey home, you realize your "
        "missing your house key. You then remember that you left it in your "
        "homies backpack.")
    print_pause(
        "You approach your friends who are chilling on the corner of the "
        "street with the older guys, and you ask him, 'Ayyy. You have my "
        "house key?'")
    print_pause(
        "He responds, 'Hell yea, I got it in my bag, go grab it. But just "
        "grab the key, don't snoop around...'")
    print_pause(
        "You reach into the bag and there appears to be drugs in there... "
        "What do you do next?")
    while True:
        option = input("1. Grab only the drugs.\n"
                       "2. Grab only the house key.\n"
                       "3. Grab both, the drugs and the house key.\n")
        if option == '1':
            drugs(items)
        elif option == '2':
            house_key(items)
        elif option == '3':
            house_key_drugs(items)
        if option not in ('1', '2', '3'):
            print_pause(
                "Not an appropriate choice. Please choose '1', '2', or '3'")
        else:
            break


def drugs(items):
    print_pause(
        "Your addiction is over powering your thought process and you totally "
        "forget to grab the house key... Drugs are bad!!!")
    play_again()


def house_key(items):
    print_pause(
        "'Dam, why does my friend have some drugs in his backpack? Is he "
        "holding it for someone? Let's pray it is something else...'")
    print_pause(
        "You ignore the drugs and grab your house key. You think to yourself "
        "about your friend, but you know the smart thing to do is leave.")
    items.append("house key")
    while True:
        option = input("Where to now?\n"
                       "1. Sprint home as fast as possible.\n"
                       "2. Head to the basketball courts.\n")
        if option == '1':
            head_home(items)
        elif option == '2':
            play_basketball(items)
        if options not in ('1', '2'):
            print_pause(
                "Not an appropriate choice. Please choose '1', '2', or '3'")
        else:
            break


def house_key_drugs(items):
    print_pause(
        "'Im nervous holding on to these drugs... Oh man I hope I don't get "
        "caught with them on me...'")
    print_pause(
        "Just as you say that, police show up and arrest everyone on the spot."
        " You get searched and have the drugs. You go to jail. Game over...")
    play_again()


def head_home(items):
    print_pause(
        "You made the decision to head home, to avoid any criminal activity "
        "your friends my be doing.")
    print_pause(
        "Whoo. You made it home safe and sound, even though the journey home "
        "can be very dangerous, but you know how to avoid danger.")
    while True:
        if "house key" in items:
            print_pause(
                "'Thank goodness I grabbed my key, I am not trying to go back "
                "with my friends.'")
            print_pause(
                "You use the house key to get inside your house. As you walk "
                "inside, you're greeted by your puppy named Smokee.")
            print_pause(
                "You pet Smokee and head to your room. You think to yourself "
                "about what you need from the house.")
            print_pause("I need to grab a few things? Hmmmm...")
            option = input(
                "1. Grab only my shoes.\n"
                "2. Grab a weapon, my shoes, and tell mom 'I love u'\n"
                "3. Grab my shoes and tell mom 'I love you'\n")
            if option == '1':
                get_shoes(items)
            elif option == '2':
                get_shoes_weapon_mom(items)
            elif option == '3':
                get_shoes_mom(items)
            if option not in ('1', '2', '3'):
                print_pause(
                    "Not an appropriate choice. Please choose '1', '2', or '3'"
                )
            else:
                break
        else:
            print_pause(
                "Oh no. I forgot the grab the key from my friend. Now I can't "
                "even get into my house...")
            play_again()


def get_shoes(items):
    print_pause(
        "All you grab is your shoes, but forget other things. You didn't even "
        "tell your mom that you love her. That's unfortunate!")
    play_again()


shoe_list = ['Kobes', 'LeBrons', 'Jordans', 'Pumas']
shoe_item = random.choice(shoe_list)


def get_shoes_weapon_mom(items):
    items.append("shoes")
    items.append("weapon")

    print_pause(
        "You grab a weapon, just in case some trouble happens along the way. "
        "In this neighborhood, anything is possible.")
    print_pause(
        "You grab your favorite pair of shoes, which happen to be, your " +
        shoe_item)
    print_pause(
        "After a long day, there is nothing like playing some basketball.")
    while True:
        option = input(
            "I can't wait to hoop. Let's go!\n"
            "1. Leave the house and go the the basketball courts.\n")
        if option == '1':
            play_basketball(items)
        if option not in ('1'):
            print_pause(
                "Not an appropriate choice. Please choose '1', '2', or '3'")
        else:
            break


def get_shoes_mom(items):
    print_pause(
        "'I hope I grabbed everything?' Your missing something... Sorry!!")
    play_again()


def play_basketball(items):
    fight_on_the_way(items)
    while True:
        print_pause(
            "You make your way to the basketball courts, which needs your "
            "house key to unlock the gate.")
        print_pause("You use the key to open the gate to the courts.")
        print_pause(
            "Another kid sees you enter thr courts and asks, 'Ayyyy. You "
            "tryna play next with me? You'll be our fifth?'")
        print_pause(
            "You look down at your shoes in your hands and respond, 'Hell "
            "yea, I'm down! Let me put my shoes on real quick.'")
        print_pause(
            "You begin playing how you normally play which is incredibly "
            "hard and passionate. You hate losing regardless what it is, you "
            "have a crazy competative nature that drives you everyday.")
        print_pause(
            "It's been an intense game. It has came down to the last shot. "
            "As a basketball player, you have to make the right decision in a "
            "pressure situation like this.")
        print_pause("The ball is in your hands...")
        if "shoes" in items:
            option = input("Games tied. Only 4 seconds left. What do you do?\n"
                           "1. Pass to Bilal in the corner for a 3.\n"
                           "2. Force a contested jump shot.\n"
                           "3. Drive to the hoop for a lay-up.\n")
            if option == '1':
                print_pause(
                    "Great pass!!! Bilal made the shot, you won! Ahhhhhhhh "
                    "the crowd goes crazy, chanting, 'M.V.P., M.V.P., M.V.P!!")
                win()
            if option == '2':
                print_pause("Oh no, you shot the ball and it was an airball. "
                            "Game over!!!")
                play_again()
            if option == '3':
                print_pause(
                    "As you drive to the hoop, Yousef blocks the shot! He "
                    "gives you the Mutumbo finger, waving it back and forth "
                    "in your face. 'No, no, no. Not in my house! Game over...")
                play_again()
            if option not in ('1', '2', '3'):
                print_pause(
                    "Not an appropriate choice. Please choose '1', '2', or '3'"
                )
            else:
                break
        else:
            print_pause("No shoes, you cant hoop.")
            play_again()


def fight_on_the_way(items):
    print_pause(
        "Like we said before, the neighborhood can be dangerous, so you must "
        "always be on the look out for anything suspicious. Even though the "
        "courts are a few blocks away, anything can hap...")
    print_pause("'WHAM!' A man attacks you on the way to the courts.")
    while True:
        if "weapon" in items:
            print_pause(
                "Thank goodness you grabbed that weapon from your house.")
            print_pause("You must fight! What are you doing???")
            option = input("1. Hit him in the head.\n"
                           "2. Hit him in the stomach.\n"
                           "3. Throw him off and run!\n")
            if option == '1' or option == '2' or option == '3':
                print_pause(
                    "You do whatever you can to fight off the strange "
                    "attacker. Your free! Now get your butt to the courts!")
                return
            if option not in ('1', '2', '3'):
                print_pause(
                    "Not an appropriate choice. Please choose '1', '2', or '3'"
                )
            else:
                break
        else:
            print_pause(
                "NOOOOOOOOOO. You forgot to grab a weapon from your house..."
                " You lose the fight...")
            play_again()


def play_again():
    while True:
        option = input("You lost, play again? y/n").lower()
        if option == 'y':
            start_game()
        elif option == 'n':
            sys.exit()
        if option not in ('y', 'n'):
            print_pause("Not an appropriate choice. Please choose 'y', or 'n'")
        else:
            break


def win():
    print_pause(
        "Let's go, we won the game! As a great basketball player, being "
        "selfish can be your downfall. Teamwork and defense will win "
        "championships. Go Lakers.")
    while True:
        option = input("Want to play again? Please choose y/n\n")
        if option == 'y':
            start_game()
        elif option == 'n':
            sys.exit()
        if option not in ('y', 'n'):
            print_pause("Not an appropriate choice. Please choose 'y', or 'n'")
        else:
            break


start_game()
