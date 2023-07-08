#Exploring parent and child classses to create data, reuse attributes and functions in a banking system format.

#Parent class
class User(): 
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_details(self):
        print(f"Personal Details. Name: {self.name}. Age: {self.age}. Gender: {self.gender}.")

#Child class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposits(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f"Your balance has been updated. It is now: £{self.balance}.")

    def withdraw(self, take_away):
        self.take_away = take_away
        if self.take_away > self.balance:
            print(f"Not enough funds. Balance available to withdraw = £{self.balance}")
        else:
            self.balance = self.balance - self.take_away
            print(f"Your account balance is now: £{self.balance}")

    def view_balance(self):
        self.show_details()
        print(f"Your balance is £{self.balance}.")


Customer1 = Bank("Sam", 29, "Female") #Inputting data into variable
Customer1.show_details()      #Printing user details called from line 7, using data in variable on line 13
Customer1.deposits(20) #Adds £20 to balance
Customer1.deposits(500) #Adds £500 to balance
Customer1.withdraw(12) #Withdraws £12
Customer1.withdraw(100000) #Attemps to withdraw, then error message in line 25 printed
Customer1.withdraw(507) #Allows withdrawal of £507
Customer1.view_balance() #Shows final balance of £1