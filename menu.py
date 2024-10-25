# Menu dictionary
menu = {
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

# 1. Create empty order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered

order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True

while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

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
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")
            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
                # 2. Ask customer to input menu item number
                # Get the customer's input
                menu_selection = input("Type menu item number: ")
                # Print out the menu item number they selected               
                # 3. Check if the customer typed a number           
                if menu_selection.isdigit():
                     # Convert the menu selection to an integer
                    menu_selection = int(menu_selection)
                        # Check if the customer's input is a valid option                       
                    if int(menu_selection) in menu_items.keys():
                        # 4. its a key, proceed
                        menu_itm = menu_items[int(menu_selection)]                    
                        # Store the item name as a variable
                        menu_selection_name = menu_itm["Item name"]
                        # Store the item price as a variable
                        menu_selection_price = menu_itm["Price"]
                        # Ask the customer for the quantity of the menu item
                        quantity = input(f"How many {menu_selection_name} would you like to order? ")
                        print(" *** if input is invalid, the quantity defaults to 1 ")  
                        if quantity.isdigit():
                            # Convert the quantity to an integer
                            quantity = int(quantity)
                            
                            # Add the item name, price, and quantity to the order list
                            order = {
                                "Item_name": menu_selection_name,
                                "Price": menu_selection_price,
                                "Quantity": quantity
                            }
                            order_list.append(order)                       
                        else:
                            # Check if the quantity is a number, default to 1 if not
                            quantity = 1                    
                            # Print out the menu category name they selected
                        print(f"You selected {menu_selection_name}")
                    else:  
                        # 4. if not a key, print error
                        # Tell the customer that their input isn't valid
                        # Tell the customer they didn't select a menu option
                        print("Not a valid selection.")  
                
                else:                    
                    
                    # Tell the customer they didn't select a number
                    print("You didn't input a number.")                      
                
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    # 5. Continuous while loop to keep ordering
    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()

        # Check the customer's input
        match keep_ordering:
            case "yes":
                 # Keep ordering
                place_order = True
                break
            case "y":
                 # Keep ordering
                place_order = True
                break  
            case "no":
                # Exit the keep ordering question loop
                place_order = False
                print("Thank you for your order")
                break 
            case "n":
                # Exit the keep ordering question loop                
                place_order = False
                # Since the customer decided to stop ordering, thank them for
                # their order
                print("Thank you for your order")
                break 
            case _:
                # Tell the customer to try again
                print("Invalid input. Please try again.")   

   
# Print out the customer's order
print("Here is your order.\n")
print("Item name                 | Price  | Quantity   | Total")
print("--------------------------|--------|------------|---------")

subtotals_list = []
subtotal=float(0)
taxtotal=float(0)
grandtotal=float(0)  

# 6. Create a to loop to loop through the items in the customer's order
for x in order_list:  
    res=0
    order = dict(x)
    item_name=""
    price=float(0)
    quantity=int(0)
    itmtotal=float(0)     

    i = 1

    ## Created to load values for calulation
    totals_list = []
    #find the dict values, set them to var
    for x in order.values():        
         # Initialize result variable to 1
         # 7. Save the value of each key to var
        res=1
        if(i==1):
            item_name = x        
        if(i==2):
            price=float(x)
            totals_list.append(price)
        if(i==3):
            quantity=int(x) 
            totals_list.append(quantity)           
            break        
        i += 1
        
    # Loop through each value in totals list, calculate qty * price for usage in an extra total column.
    for val in totals_list:        
        # Multiply current result by the current value
        res = res * val 
        itmtotal=res
    # round value to 2 decimel            
    itmtotal =str(round(itmtotal, 2))       
    # add total to grand total
    subtotals_list.append(float(itmtotal))

    # 8. calculate empty spaces
    # 9. create space strings
    num_itemname_spaces = 31 - len(item_name) - 6
    itemname_spaces = " " * num_itemname_spaces
    num_itemprice_spaces = 8 - len(str(price)) - 2 
    itemprice_spaces = " " * num_itemprice_spaces
    num_itemqty_spaces = 12 - len(str(quantity)) - 2 
    itemqty_spaces = " " * num_itemqty_spaces
    
    # 10. print line for receipt using space strings
    print(f"{item_name}{itemname_spaces} | {price}{itemprice_spaces} | {quantity}{itemqty_spaces} | {itmtotal}")
   
#subtotal = sum(subtotals_list)
#subtotal = sum([i for i in subtotals_list])
#print(f"{subtotal} of subtotal.")
# 11. Calculate the cost of the order using list comprehension
subtotal = sum([x["Price"]*x["Quantity"] for x in order_list])

subtotal =str(round(subtotal, 2))    
taxtotal = float(subtotal) * 1.0825
taxtotal = taxtotal - float(subtotal)
taxtotal =str(round(taxtotal, 2))
grandtotal = float(taxtotal) + float(subtotal)
grandtotal =str(round(grandtotal, 2))

print(f"----------------------------------------------------------")
print(f"---------------------------------- | SubTotal   | {float(subtotal)}")
print(f"---------------------------------- | SalesTax   | {float(taxtotal)}")
print(f"---------------------------------- | GrandTotal | {float(grandtotal)}")

order_list.clear
totals_list.clear
subtotals_list.clear