print("Welcome to my Azure-900 mini Quiz!")

name = input("What is your name? \n")

score = 0

play = input(f"Hi, {name}! Did you want to partake in this mini quiz to help strengthen your Azure knowledge? \n[a] Yes, please! \n[b] No thank you! \n")

if play.lower() == "a":
    print(f"That's brilliant {name}! Let's get started.")

else:
    quit()

#Lets add some questions! Question 1
answer = input("1. Which Azure service should you use to store certificates? \n[a] Azure Security Centre \n[b] an Azure storage account \n[c] Azure Key Vault \n")
if answer.lower() == "c":
    print("That is correct!")
    score += 1

else:
    print("That is incorrect. The answer was c: Azure Key Vault")

#Question 2
answer = input("2. You need to associate the costs of resources to different groups without changing any locations. What should you use? \n[a] Resource tags \n[b] Resource groups \n[c] Subscriptions \n")
if answer.lower() == "a":
    print("That is correct!")
    score += 1

else:
    print("That is incorrect. The answer was a: Resource tags")

#Question 3
answer = input("3. What can be applied to stop the accidental deletion of a resource? \n[a] a resource tag \n[b] a resource lock \n[c] a policy \n")
if answer.lower() == "b":
    print("That is correct!")
    score += 1

else:
    print("That is incorrect. The answer was b: a resource lock")

#Question 4
answer = input("4. You are recommending Azure virtual machines. The solution must enforce the company standards. Which should your recommend? \n[a] Azure Policy \n[b] Azure Blueprints \n[c] Azure Cost Management \n")
if answer.lower() == "a":
    print("That is correct!")
    score += 1

else:
    print("That is incorrect. The answer was a: Azure Policy")

#Question 5
answer = input("5. Multi-factor authentication is enabled on accounts with write permissions. What should you ensure is implemented? \n[a] Resource tags \n[b] Resource locks \n[c] Azure Policy \n")
if answer.lower() == "c":
    print("That is correct!")
    score += 1

else:
    print("That is incorrect. The answer was c: Azure Policy")

#Final score statement, make sur to change the 1 to the number of questions!
print(f"Well done {name}, you got a score of {score}. That is: " + str(score / 5 * 100) + "%. ")
