import random

# Text colours

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

# Colour Coding
# 
# Purple = Story
# Green = Options
# White = Player Input
# Orange = Game Instructions/Help

# Title Screen
print("Welcome to the Nether Isle RPG")


# What do you want to be known by?
class Player:

    player_name = ''
    player_class = None
    player_weapon = ''

    def intro(self):
        print(P+"Welcome to The Nether Isle!"+W)
        self.get_name()
        self.get_class()
        self.player_weapon = self.player_class.get_weapon()
        self.print_summary()

    def get_name(self):
        self.player_name = input(P+"What is your name, adventurer? \n"+W)
        print(P+f"\nAh good to meet you, {self.player_name}."+W)

    def get_class(self): 
        res = input(P+"\nWhat class are you, traveller? \n" + G+"[1] Barbarian \n[2] Wizard \n[3] Rogue \n[4] Ranger \n"+W)
        if res == "1":
            self.player_class = Barbarian()
        elif res == "2":
            self.player_class = Wizard()
        elif res == "3":
            self.player_class = Rogue()
        elif res == "4":
            self.player_class = Ranger()
        else:
            print(R+"\nSorry, I didn't understand your input. Please respond with 1, 2, 3 or 4."+W)
            self.get_class()

    def print_summary(self):
        print(P+f"\nSo you're a {self.player_weapon} wielding {self.player_class.name()}! Welcome to the Nether Isle, {self.player_name}. \n\nThis is a world full of dangers. You will come across traps, puzzles and monsters along your journey. Your task is to collect four magic rings, each of which will grant you access to the next realm.\nOnce you have collected all four, you will be able to face your final challenge; defeating the tyrannical ruler of the Nether Isle.")
        print("\nWe wish you the best of luck on your adventure."+W)

class Barbarian:

    def name(self):
        return "Barbarian"

    def get_weapon(self):
        res = input(P+"\nWhat is your weapon of choice, barbarian? \n" + G+"[1] Sword \n[2] Axe \n[3] Mace \n"+W)

        if res == "1":
            return "sword"
        elif res == "2":
            return "axe"
        elif res == "3":
            return "mace"
        else:
            print(R+"\nSorry, I didn't understand your input. Please respond with 1, 2 or 3."+W)
            return self.get_weapon()


class Wizard:

    def name(self):
        return "Wizard"
    
    def get_weapon(self):
        res = input(P+"\nWhat is your weapon of choice, wizard? \n" + G+"[1] Staff \n[2] Wand \n[3] Spellbook \n"+W)

        if res == "1":
            return "staff"
        elif res == "2":
            return "wand"
        elif res == "3":
            return "spellbook"
        else:
            print(R+"\nSorry, I didn't understand your input. Please respond with 1, 2 or 3."+W)
            return self.get_weapon()
        
class Rogue:

    def name(self):
        return "Rogue"
    
    def get_weapon(self):
        res = input(P+"\nWhat is your weapon of choice, rogue? \n" + G+"[1] Dagger \n[2] Crossbow \n[3] Throwing Stars \n"+W)

        if res == "1":
            return "Dagger"
        elif res == "2":
            return "Crossbow"
        elif res == "3":
            return "Throwing Stars"
        else:
            print(R+"\nSorry, I didn't understand your input. Please respond with 1, 2 or 3."+W)
            return self.get_weapon()
        
class Ranger:

    def name(self):
        return "Ranger"
    
    def get_weapon(self):
        res = input(P+"\nWhat is your weapon of choice, ranger? \n" + G+"[1] Long Bow \n[2] Spear \n[3] Darts \n"+W)
                
        if res == "1":
            return "Long Bow"
        elif res == "2":
            return "Spear"
        elif res == "3":
            return "Darts"
        else:
            print(R+"\nSorry, I didn't understand your input. Please respond with 1, 2 or 3."+W)
            return self.get_weapon()

# Combat Instructions. Can be called anytime from room 5 onward

def combat_instructions():
    print(O+"The combat in this game operates with random number commands, not dissimilar to the dice rolls of Dungeons and Dragons. From here on, we will refer to the calling of these commands as 'dice rolls'.\n")
    print("Each enemy has a HP (Health Points) value, as does the player. Each time a dice roll occurs, the result of that roll will be subtracted from the enemy, or from the player for an enemy roll.\n")
    print("The number from the dice roll can also be affected by multiple things. Both player and enemy attacks can be buffed by items or effects. They can also by reduced by other items or effects.\n"+W)

# Player Spawn

def playerspawn():
    print(P+"\n \nYou wake up in a forest clearing. The sun is peeking through the treetops above and birds are chirping in the trees. As you stand, you can see that there is a path ahead which seems to lead deeper into the forest."+W)
    res = input(P+"Would you like to venture onward? \n"+G + "[1] Yes \n[2] No\n"+W)
    if res == "1":
        return room2_locked()
    elif res == "2":
        exit()
    else:
        print(R+"\nSorry, I didn't understand your input. Please respond with 1, 2 or 3.\n"+W)
        return playerspawn()

# Room 2 Locked

def room2_locked():
    print(P+"You follow the path for a mile or so and come to another clearing. Ahead of you is a large, dark tower with a great wooden door. To your right, there is a large cave entrance.")
    res = input("Would you like to try and open the door or explore the cave? \n" + G+"[1] Try the door \n[2] Explore the cave\n"+W)
    if res == "1":
        print(P+"The door is locked. You decide to go and explore the cave.\n"+W), 
        room2r_door_tested()
    elif res == "2":
        return room2r_door_untested()
    else:
        print(R+"\nSorry, I didn't understand your input. Please respond with 1 or 2.\n"+W)
        room2_locked()

# Room 2r (Cave, door tried)

def room2r_door_tested():
    print(P+"You cautiously creep into the cave. Once you're through the entrance it starts to slope downward. It isn't very large, so you can easily see the whole cave in the light coming through the entrance.")
    res = input("There is a large boulder towards the back and a large crack running the width of the cave. Would you like to investigate the boulder or the crack? \n" + G+"[1] Boulder \n[2] Crack\n"+W)
    if res == "1":
        print(P+"You find an old, rusty key. It looks as though it might fit the lock in the tower door."+W) # Look into adding to inventory
        return room2_unlocked()
    elif res == "2":
        print(P+"There is nothing here.")
        return room2r_door_tested()
    else: 
        print(R+"\nSorry, I didn't understand your input. Please respond with 1 or 2.\n"+W)
        return room2r_door_tested()

# Room 2r (Cave, door not tried)

def room2r_door_untested():
    print(P+"You cautiously creep into the cave. Once you're through the entrance it starts to slope downward. It isn't very large, so you can easily see the whole cave in the light coming through the entrance.")
    res = input("There is a large boulder towards the back and a large crack running the width of the cave. Would you like to investigate the boulder or the crack? \n" + G+"[1] Boulder \n[2] Crack\n"+W)
    if res == "1":
        print(P+"You find an old, rusty key. You wonder what it might unlock."+W) # Look into adding to inventory
        return room2_unlocked()
    elif res == "2":
        print(P+"There is nothing here.")
        return room2r_door_untested()
    else: 
        print(R+"\nSorry, I didn't understand your input. Please respond with 1 or 2.\n"+W)
        return room2r_door_untested()
    
# Room 2 Unlocked

def room2_unlocked():
    print(P+"You make your way out of the cave and back into the clearing. The door to the tower lies ahead of you.")
    res = input("Would you like to try the key in the door or end your adventure here? \n" + G+ "[1] Try the door \n[2] End your adventure\n"+W)
    if res == "1":
        print(P+"The turn the rusty key in the lock. It's tough but it slowly turns and the door slowly creaks open."+W)
        return room3()
    elif res == "2":
        exit()
    else:
        print(R+"\nSorry, I didn't understand your input. Please respond with 1 or 2.\n"+W)
        return room2_unlocked()
    
# Room 3 (Riddle)    

def room3():
    print(P+"The door opens up into a great, round stone hall. There is a spiral staircase encirlcing the wall of the tower, however the first few stairs are missing. There appears to be no way to reach them.")
    print("As you take a step further into the room, letters start appearing in the air in front of you, as if written by an unseen hand...\n")
    res = input("I don't have eyes, but once I did see. I once had thoughts, now white and empty.\n"+W).lower()
    if res == "skull":
        print(P+"As soon as the word leaves your mouth, the first few stone stairs slide out from within the wall to reveal the bottom of the staircase. Your way up the tower is now clear.\n"+W)
        return room4()
    else:
        print(R+"Nothing happens"+W)
        return room3()

# Room 4

def room4():
    print(P+"About halfway up the tower, you notice a doorway, half hidden by ivy, that leads off the stairs to a small room.")
    res = input("Would you like to investigate the hidden doorway or continue up the stairs?\n" + G+ "[1] Go through the door \n[2] Continue up the stairs\n"+W)
    if res == "1":
        return room4r()
    elif res == "2":
        return room5()
    else:
        print(R+"\nSorry, I didn't understand your input. Please respond with 1 or 2.\n"+W)
        return room4()

# Weapon/Buff room
    
def room4r():
    print("test")
    
# Monster
 
def room5():
    return combat_instructions()

player = Player()
player.intro()
playerspawn()