
furnitures = []

while True:
    print("""WeBestore Furniture Management
    1. Insert New Furniture
    2. View All Furniture
    3. View Selected Furniture by Slicing Index Range
    4. Update Furniture
    5. Delete Furniture
    6. Delete All Furniture
    7. Exit""")
    menu_option = int(input("Choose an option: "))
    while menu_option > 7 or menu_option < 1:
        menu_option = int(input("Choose an option from 1 to 7: "))
    if menu_option == 1:
        while True:
            furniture_input = input("Enter the name of the furniture item to insert (between 5 and 20 characters): ")
            if len(furniture_input) <= 5 or len(furniture_input) >= 20:
                print("\nInvalid input. The name must be between 5 and 20 characters. Please try again.")
            else:
                furnitures.append(furniture_input)
                print("Data has been added succesfully inserted!\n")
                break

    elif menu_option == 2:
        if len(furnitures) == 0:
            print("No furniture in the list.\n")
        else:
            print("Furniture list:")
            for i in range(len(furnitures)):
                print(f"{i + 1}. {furnitures[i]}")
            print("\n")

    elif menu_option == 3:
        if len(furnitures) == 0:
            print("No furniture in the list.\n")
        else:
            while True:
                start_index = int(input(f"Enter the start index (1 to {len(furnitures)}): "))
                if start_index < 1 or start_index > len(furnitures):
                    print(f"Invalid start index. Please enter a value between 1 and {len(furnitures)}.\n")
                else:
                    break

            while True:
                end_index = int(input(f"Enter the end index ({start_index} to {len(furnitures)}): "))
                if start_index > end_index or end_index > len(furnitures):
                    print(f"Invalid end index. Please enter a value between {start_index} and {len(furnitures)}.\n")
                else:
                    break
            
            print(f"The furniture items from index {start_index} to {end_index} are: ")
            print(furnitures[start_index - 1 : end_index])
            

    elif menu_option == 4:
        if len(furnitures) == 0:
            print("No furniture in the list.\n")
        else:
            while True:
                update_index = int(input(f"Enter the number of the item you want to update (1 to {len(furnitures)}): "))
                if update_index < 1 or update_index > len(furnitures):
                    print(f"Invalid index. Please enter a number between 1 and {len(furnitures)}.\n")
                else:
                    while True:
                        updated_furniture = input("Enter the new name (between 5 and 20 characters): ")
                        if len(updated_furniture) < 5 or len(updated_furniture) > 20:
                            print("Invalid input. The name must be between 5 and 20 characters. Please try again.\n")
                        else:
                            furnitures[update_index - 1] = updated_furniture
                            print("Furniture has been succesfully updated!\n")
                            break
                    break

    elif menu_option == 5:
        if len(furnitures) == 0:
            print("No furniture in the list.\n")
        else:
            while True:
                deleted_index = int(input("Input the index of the furniture to be deleted: "))
                if deleted_index < 1 or deleted_index > len(furnitures):
                    print(f"Invalid input. The index must be between 1 and {len(furnitures)}\n")
                else:
                    del(furnitures[deleted_index - 1])
                    print("Furniture has been succesfully deleted!\n")
                    break              

    elif menu_option == 6:
        furnitures.clear()
        print("All furniture has been deleted.\n")

    elif menu_option == 7:
        break
