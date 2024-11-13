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
print("order_list", order_list)
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
    menu_category = input("Type menu item to view or (q) to quit: ")
    
    # exit the loop if the user typed 'q'
    # Check if the customer's input is a number
    if menu_category == 'q':
        break
    
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
            i = 1
            menu_items = {}
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary
                if type(value) is dict:
                    for key2, value2 in value.items():
                        print(f"{i}      | {key} - {key2}{' ' * (24 - len(key + key2) - 3)} | ${value2}")
                        menu_items[i] = {"Item name": f"{key} - {key2}", "Price": value2}
                        i += 1
                else:
                    print(f"{i}      | {key}{' ' * (24 - len(key))} | ${value}")
                    menu_items[i] = {"Item name": key, "Price": value}
                    i += 1
            # 2. Ask customer to input menu item number
            # Get the customer's input
            menu_input = input("Type the number of the menu item that you'd like to select: ")
            # Print out the menu item number they selected               
            # 3. Check if the customer typed a number           
            if isinstance(menu_input, str) and menu_input.isdigit():
                # Convert the menu selection to an integer
                menu_input = int(menu_input)                                  
            if menu_input in menu_items:
                # 4. its a key, proceed
                select_itm = menu_items[int(menu_input)]                    
                # Store the item name as a variable
                itm_name = select_itm["Item name"]
                # Store the item price as a variable
                itm_price = select_itm["Price"]
                # Ask the customer for the quantity of the menu item
                qty_input = input(f"How many {itm_name} would you like to order? ")
                if qty_input.isdigit():
                    qty = int(qty_input)
                else:
                        # Tell the customer that their input isn't valid
                    print("Invalid input. Defaulting quantity value to 1.")
                    qty = 1
                
                    # Add the selected item and quantity to the order list
                order_list.append({
                    "Item name": itm_name,
                    "Price": itm_price,
                    "Quantity": qty
                })
                print(f"Adding ({qty}) - {itm_name} to your order.")                        
            else:  
                # 4. if not a key, print error                       
                # Tell the customer they didn't select a menu option
                print("You didn't select a valid menu option.")  
    else:
        print(f"'{menu_category}' was not a valid menu option.")        
        menu_category = 1
        
    # 5. Continuous while loop to keep ordering
    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()

        # Check the customer's input
        match keep_ordering.lower():           
            case "y":
                 # Keep ordering
                place_order = True
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
                print("You didn't enter a Y or N. Please try again.")   
   
# Print out the customer's order
print("Here is your order. We'll have it out in a jiffy!\n")
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
    print(f"{item_name}{itemname_spaces} | {price}{itemprice_spaces} | {quantity}{itemqty_spaces} | ${itmtotal}")

# 11. Calculate the cost of the order using list comprehension
subtotal = sum([x["Price"]*x["Quantity"] for x in order_list])

subtotal =str(round(subtotal, 2))    
taxtotal = float(subtotal) * 1.0825
taxtotal = taxtotal - float(subtotal)
taxtotal =str(round(taxtotal, 2))
grandtotal = float(taxtotal) + float(subtotal)
grandtotal =str(round(grandtotal, 2))

print(f"----------------------------------------------------------")
print(f"---------------------------------- | SubTotal   | ${float(subtotal):.2f}")
print(f"---------------------------------- | SalesTax   | ${float(taxtotal):.2f}")
print(f"---------------------------------- | GrandTotal | ${float(grandtotal):.2f}")

order_list.clear
totals_list.clear
subtotals_list.clear