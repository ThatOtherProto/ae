import sys
import time
import logging
import warnings
import random
sys.stderr.write("err: import time is unused\n")
sys.stderr.write("THERE IS AN ERROR ON LINE 55\n")
sys.stderr.write("there is no number c on line 38\n")

print("This part of the game is old and outdated, it won't be updated and debug mode is always on. soz! - the creator :3")
time.sleep(1)
print("If you want the updated version of the game, please download the latest version of the game on github (look at releases, it should be at the top, this will be at the bottom) - the (femboy) creator :3")
time.sleep(1)

x = int(random.randint(1, 3))

inventory = []

def m4_a():
    print("m4_a() subroutine has been activated")
    print("you are on the m4")
    print("""where do you want to go?
1) go to cardiff
2) go to Llanfairpwllgwyngyllgogerychrwyndrobwllllantysiliogogoch
3) check inventory""")
    choice = input(int(""))
    if choice == "1":
        warnings.warn("this subroutine does not exist", stacklevel=2)
        sys.stderr.write("program has been terminated")
    elif choice == "2":
        warnings.warn("this subroutine does not exist", stacklevel=2)
        sys.stderr.write("program has been terminated")
    elif choice == "3":
        warnings.warn("this will loop the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        m4_a()
    else:
        warnings.warn("please input a valid integer", stacklevel=2)
        warnings.warn("this will loop the subroutine", stacklevel=2)
        m4_a()

def newport():
    print("newport() subroutine has been activated")
    print("you can skip this if you want lol")
    print("""what do you want to do?
1) go get supplies
2) go on the M4
3) check inventory""")
    choice = input(int(""))
    if choice == "1":
        print("you go get supplies and got food")
        warnings.warn("this will loop the subroutine", stacklevel=2)
        newport()
    elif choice =="2":
        m4_a()
    elif choice == "3":
        warnings.warn("this will loop the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        newport()
    else:
        warnings.warn("please input a valid integer", stacklevel=2)
        warnings.warn("this will loop the subroutine", stacklevel=2)
        newport()

def street():
    print("street() subroutine has been activated")
    print("you are now outside")
    print("""what do you want to do?
1) get in the car
2) check inventory""")
    choice = input(int(""))
    if choice == "1":
        newport()
    elif choice =="2":
        warnings.warn("this will loop the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        street()
    else:
        warnings.warn("please input a valid integer", stacklevel=2)
        warnings.warn("this will loop the subroutine", stacklevel=2)
        street()

def house_kitchen_cupboards():
    print("house_kitchen_cupboards() subroutine has been activated")
    print("you go to check the cupboards")
    print("""check cupboard:
1) cupboard 1
2) cupboard 2
3) cupboard 3
4) go back
5) check inventory""")
    choice = input(int(""))
    if choice == "1":
        print("you check the cupboard")
        if x == "1":
            print("you found a knife")
            inventory.append("knife")
            knife = True
            warnings.warn("This will loop the subroutine", stacklevel=2)
            house_kitchen_cupboards()
        else:
            print("you found nothing")
            warnings.warn("This will loop the subroutine", stacklevel=2)
            house_kitchen_cupboards()
    elif choice == "2":
        print("you check the cupboard")
        if x == "2":
            print("you found a knife")
            inventory.append("knife")
            knife = True
            warnings.warn("This will loop the subroutine", stacklevel=2)
            house_kitchen_cupboards()
        else:
            print("you found nothing")
            warnings.warn("This will loop the subroutine", stacklevel=2)
            house_kitchen_cupboards()
    elif choice == "3":
        print("you check the cupboard")
        if x == "3":
            print("you found a knife")
            inventory.append("knife")
            knife = True
            warnings.warn("This will loop the subroutine", stacklevel=2)
            house_kitchen_cupboards()
        else:
            print("you found nothing")
            warnings.warn("This will loop the subroutine", stacklevel=2)
            house_kitchen_cupboards()
    elif choice == "4":
        house_kitchen()
    elif choice == "5":
        warnings.warn("this will loop the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        house_kitchen_cupboards()
    else:
        warnings.warn("please input a vaild integer", stacklevel=2)
        warnings.warn("this will loop the subroutine", stacklevel=2)
        house_kitchen_cupboards()

def house_kitchen():
    print("house_kitchen() subroutine has been activated")
    print("you went into the kitchen")
    print("""what do you want to do?
1) fight zombie
2) look in the cupboards
3) check inventory""")
    choice = input(int(""))
    if choice == "1":
        print("you go to fight the zombie")
        if knife == True:
            print("you fight the zombie")
            print("you win")
            house_hallway()
        else:
            print("you can't fight the zombie yet")
            warnings.warn("this will repeat the subroutine", stacklevel=2)
            house_kitchen()
    elif choice == "2":
        house_kitchen_cupboards()
    elif choice == "3":
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        house_kitchen()
    else:
        warnings.warn("please input a vaild integer", stacklevel=2)
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        house_kitchen()

def house_hallway():
    print("house_hallway() subroutine has been activated")
    print("you entered the hallway")
    print("""what do you want to do?
1) go to the kitchen
2) go outside
3) go to the living room
4) go to the dining room
5) check inventory""")
    choice = input(int(""))
    if choice == "1":
        house_kitchen()
    if choice =="2":
        street()
    if choice == "3":
        print("You have died, please restart the game (there is no saving lol)")
    if choice == "4":
        print("You have died, please restart the game (there is no saving lol)")
    if choice == "5":
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        house_hallway()
    else:
        warnings.warn("please input a valid integer", stacklevel=2)
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        house_landing()

def house_landing():
    print("house_landing() subroutine has been activated")
    print("you have entered the landing")
    print("""only 1 of 4 rooms will help you escape
1) turn back
2) bedroom 2
3) bedroom 3
4) bathroom
5) go downstairs
6) inventory (does not progress the game)""")
    choice = input(int(""))
    if choice == "1":
        print("You have died, please restart the game (there is no saving lol)")
    elif choice == "2":
        print("You have died, please restart the game (there is no saving lol)")
    elif choice == "3":
        print("You have died, please restart the game (there is no saving lol)")
    elif choice == "4":
        print("You have died, please restart the game (there is no saving lol)")
    elif choice == "5":
        house_hallway()
    elif choice == "6":
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        house_landing()
    else:
        warnings.warn("please input a valid integer", stacklevel=2)
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        house_landing()

def house_bedroom():
    print("house_bedroom() subroutine is activated")
    print("You need to leave and escape.")
    print("""What do you want to do?
1) leave the bedroom
2) grab your phone
3) inventory (does not progress the game)""")
    choice = input(int())
    if choice == "1":
        house_landing()
    elif choice == "2":
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        inventory.append("phone")
        house_bedroom()
    elif choice == "3":
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        print("inventory: ", inventory)
        house_bedroom()
    else:
        warnings.warn("please input a valid integer", stacklevel=2)
        warnings.warn("this will repeat the subroutine", stacklevel=2)
        house_bedroom()
    
def house():
    print("house() subroutine is activated")
    print("this is the house where your're lives")
    print("tiem to leave teh hose :3")
    house_bedroom()

name = print("What's your're name?")
sys.stderr.write("err: unused variable name\n")
print("sike your're name is caine >:3")
print(";w;")
print("ono zombie caine aaaaaaa zombie aaaaaaaaaaaaaaaa - said co-caine")
print("dgsafagrwigfrwuvfebvgiubjsbvv\bxzbv - says the zombie")
print("ono the zombie has zombied the zombie and is going to zombie our zombie runnn! - said co-caine")
house()

