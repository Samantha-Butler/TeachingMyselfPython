# What do you want to be known by?
class Player:

    player_name = ''
    player_class = ''
    player_weapon = ''

    def intro(self):
        print("Welcome to The Nether Isle!")
        self.get_name()
        self.get_class()
        self.player_weapon = self.player_class.get_weapon()
        self.print_summary()

    def get_name(self):
        self.player_name = input(str("What is your name, adventurer? \n"))
        print(f"Ah good to meet you, {self.player_name}.")

    def get_class(self): 
        res = input(str("What class are you, traveller? \n[1] Barbarian \n[2] Wizard \n[3] Rogue \n[4] Ranger \n"))
        if res == "1":
            self.player_class = Barbarian()
        elif res == "2":
            self.player_class = Wizard()
        elif res == "3":
            self.player_class = Rogue()
        elif res == "4":
            self.player_class = Ranger()
        else:
            print("Sorry, I didn't understand your input. Please respond with 1, 2, 3 or 4.")
            self.get_class()

    def print_summary(self):
        print(f"So you're a {self.player_weapon} wielding {self.player_class.name()}! Welcome to the Nether Isle, {self.player_name}.")


class Barbarian:

    def name(self):
        return "Barbarian"

    def get_weapon(self):
        res = input(str("What is your weapon of choice, barbarian? \n[1] Sword \n[2] Axe \n[3] Mace \n"))

        if res == "1":
            return "sword"
        elif res == "2":
            return "axe"
        elif res == "3":
            return "mace"
        else:
            print("Sorry, I didn't understand your input. Please respond with 1, 2 or 3.")
            return self.get_weapon()


class Wizard:

    def name(self):
        return "Wizard"
    
    def get_weapon(self):
        res = input(str("What is your weapon of choice, wizard? \n[1] Staff \n[2] Wand \n[3] Spellbook \n"))

        if res == "1":
            return "staff"
        elif res == "2":
            return "wand"
        elif res == "3":
            return "spellbook"
        else:
            print("Sorry, I didn't understand your input. Please respond with 1, 2 or 3.")
            return self.get_weapon()


class Rogue:

    def name(self):
        return "Rogue"
    
    def get_weapon(self):
        res = input(str("What is your weapon of choice, rogue? \n [1] Dagger \n[2] Crossbow \n[3] Throwing Star \n"))

        if res == "1":
            return "dagger"
        elif res == "2":
            return "crossbow"
        elif res == "3":
            return "throwing star"
        else:
            print("Sorry, I didn't understand your input. Please respond with 1, 2 or 3.")
            return self.get_weapon()


class Ranger:
    def name(self):
        return "Ranger"
    
    def get_weapon(self):
        res = input(str("What is your weapon of choice, ranger? \n[1] Long Bow \n[2] Spear \n[3] Darts \n"))

        if res == "1":
            return "long bow"
        elif res == "2":
            return "spear"
        elif res == "3":
            return "darts"
        else:
            print("Sorry, I didn't understand your input. Please respond with 1, 2 or 3.")
            return self.get_weapon()

player = Player()
player.intro()