age =  (input("Are you a cigarette addict older than 75 years old?").lower().strip() == "yes")
chronic = (input("Do you have a severe chronic disease?").lower().strip() == "yes")
immune = (input("Is your immune system too weak?").lower().strip() == "yes")
if age and chronic and immune:
    print("You are in risky group")
else:
    print("You are not in risky group")
