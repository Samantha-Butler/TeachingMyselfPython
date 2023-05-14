#This is a coffeebot, step bystep from CodeAcademy but tweaked for some minor changes.
def coffee_bot():
  print("Welcome to the cafe!")

  size = get_size()
  drink_type = get_drink_type()
  print(f"Alright, that's a {size} {drink_type}!")

  name = input("Can I get your name please? \n")
  print(f"Thanks, {name}! Your drink will be ready shortly.")

def get_size():
  res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n")
  
  if res == "a":
    return "Small"
  elif res == "b":
    return "Medium"
  elif res == "c":
    return "Large"
  else:
    return "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response."

def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed coffee \n[b] Mocha \n[c] Latte \n")

  if res == "a":
    return "Brewed Coffee"
  elif res == "b":
    return "Mocha"
  elif res == "c":
    return order_latte()
  else:
    return get_drink_type()

def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% Milk \n[b] Non-fat milk \n[c] Soy Milk \n")
  
  if res == "a":
    return "2% Milk"
  if res == "b":
    return "Non-fat Milk"
  if res == "c":
    return "Soy milk"
  else:
    return order_latte()

#Call coffee_bot()
coffee_bot()
