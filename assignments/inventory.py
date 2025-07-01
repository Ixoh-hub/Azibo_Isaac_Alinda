Inventory = ["FIFA24", "NFS2024", "PES2024", "GTA V"]

#view inventory items

def view():
    print("\nGames in stock")
    for item in Inventory:
        print(f"-{item}")
        
#add inventory items loop

def add():
    while True:
        item = input("Enter new Game or type exit to go back: ")
        if item.lower() == "exit":
            break
        if item in Inventory:
            print("Game already in stock")
        else:
            Inventory.append(item)
            print("Game added successfully")
            
# main program loop

while True:
    print("\n Welcome to LUSEKE Game Inventory")
    print("\n PRESS:\n 1. View Inventory \n 2. Add Game \n 3. Exit")
    choice = int(input("\nEnter your choice: ")) 
    if choice == 1:
        view()
    elif choice == 2:
        add()
    elif choice == 3:
        print("\n Bye....exiting")
        break
    else:
        print("\n Invalid choice")            