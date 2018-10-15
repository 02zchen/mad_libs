def beach():
  print("\nWelcome to the beach themed Mad Libs")
  noun = input("Enter a noun(name):").title()
  verb = input("Enter a verb(past):")
  adjective = input("Enter a adjective:")
  print(noun + " went to the beach one day and " + verb + " in the ocean, when " + noun + " was done he/she felt " + adjective +", " + noun + " had a fun time at the beach. ")

def school():
  print("\nWelecome to the school theme Mad Libs")
  noun = input("Enter a noun(name):").title()
  verb = input("Enter a verb(past):")
  adjective = input("Enter a adjective:")
  print("On a cloudy Monday morning right before school " + noun + " " + verb + " fruit loops then went on the school bus, at school " + noun + " looked " + adjective + ".")

def restaurant():
  print("\nWelcome to the restaurant themed Mad Libs")
  noun = input("Enter a noun(name):").title()
  verb = input("Enter a verb(past):")
  adjective = input("Enter a adjective:")
  print("At the most famous restaurant in town " + noun + " " + verb + " his favorite meal, but after he/she felt " + adjective +".")
  
def main():
  print("Hello welcome to the game Mad Libs.")
  choice = input("Which Mad Lib theme do you want to complete\n1.Beach\n2.School\n3.Restaurant\n>>>").lower()

  if choice == "beach":
    beach()
  elif choice == "school":
    school()
  elif choice == "restaurant":
    restaurant()
main()
