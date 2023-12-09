# Menu dictionary
menu-items = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

menu_dashes = "-" * 42

#create an empty order list with the following dictionary format
# = [{"Item name": "string", "Price": float, "Quantity: int"}, {next item}]
customers_order_list = []

while place_order:
    # menu_selection by customer
    
    #check to see if it is a number - if not print error and re-ask
    
    #change to integer
    
    #check to see if the integer is on the menu list - if not - error
    
    #use number to get a name from menu_items dictionary
    item_name = ????
    
    #Ask customer for quantity of the item
    quantity = input(f'How many {item_name}s do you want?')
    
    #check to see if quantity is an integer - if not quantity = 1
    if type(quantity) is not int:
        quantity = 1
        print("Since you did not type an integer, quantity was set to 1.")
        
    
    #append order list to have item_name, price, and quantity
    
    #ask customer if they want to order again with match/case
    while True:
        keep_ordering = input("Do you want to order another item?\ny=yes n=no")
        #check customer's input
        match keep_ordering.lower():
            #customer chose yes
            case 'y':
                place_order = True
                break
            #customer chose no, so complete order and exit to print receipt
            case 'n':
                place_order = False
                print("Thank you for your order.")
                break
            #customer gave an invalid response
            case_:
                print("I didn't understand your response. Please try again.")
                print("Signed\nHAL-9000")
    match keep_ordering.lower():
        case 'y':
            keep_ordering = True
        case 'n':
            keep_ordering = False
            
    

    
    



# Launch the store and present a greeting to the customer
print("Welcome to the Order-By-Number food truck.")

# Customers may want to view different sections of the menu, so let's create a 
# continuous loop
while True:
    # Ask the customer which menu category they want to view
    print("Which menu would you like to view? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval 
    menu_items = {}

    # Print the options to choose from menu headings (all the first level 
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number to view or q to quit: ")

    # Exit the loop if user typed 'q'
    if menu_category == 'q':
        break
    # Check if the customer's input is a number
    elif menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Display the heading for the sub-menu
            print(menu_dashes)
            print(f"This is the {menu_category_name} menu.")
            print(menu_dashes)
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")

            # Initialize a menu item counter
            item_counter = 1
            # Print out the menu options from the menu_category_name
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    # Iterate through the dictionary items
                    for key2, value2 in value.items():
                        # Print the menu item
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{item_counter}      | "
                              + f"{key} - {key2}{item_spaces} | "
                              + f"${value2}")
                        # Add 1 to the item_counter
                        item_counter += 1
                else:
                    # Print the menu item
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{item_counter}      | "
                          + f"{key}{item_spaces} | ${value}")
                    # Add 1 to the item_counter
                    item_counter += 1
            
            print(menu_dashes)
            input("Press enter to return to the main menu.")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")
