football_player = {"Name":"Cristiano", "Surname":"Ronaldo", "Number":"7", "Growth":"1,87"}
for keys, values in football_player.items():
    print(keys, values, sep=" - ")
while True:
    ask_add = input("\nDo you want to add key and value in the dictionary?\n1. Yes\n2. No\nYour choise: ")
    if ask_add in ["1", "Yes", "yes"]:
        football_player2 = football_player.copy()
        insert_key = input("\nEnter the key for value, which you want to add: ")
        insert_value = input("Enter the value: ")
        football_player2[insert_key] = insert_value
        for keys, values in football_player2.items():
            print(keys, values, sep=" - ")
            continue
    elif ask_add in ["2", "No", "no"]:
        print("Ok")
        break
    else:
        print("Invalid choice! Try again...")
        continue
