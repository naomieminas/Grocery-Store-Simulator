'''
    Project: Grocery Store Simulator
    Name: Naomie Minassie
    Date: September 20, 2024
    Course: CMSC 150: Introduction to Computing - Section 04
    Program Description: This is a grocery store simulation program. The program\
    will ring up customer's items and print back an itemized receipt of the item.
'''

# Grocery Inventory with at least 10 items, including one compound word item
INVENTORY = {
    "milk": 3.71, 
    "bread": 2.50, 
    "eggs": 4.96, 
    "flour": 4.00, 
    "chicken breast": 9.89,  # Compound word item
    "bananas": 1.49, 
    "cereal": 5.98, 
    "lettuce": 3.18, 
    "nutella": 7.73, 
    "grapes": 4.59
}

# -----  CHECKOUT FUNCTIONS  ----- #

def clerk_checkout():
    """
    Handles the clerk-style checkout where items are entered one by one.
    Shows a running total after each item, and an itemized receipt at the end.
    """
    total = 0   # Running total for the cart
    cart = {}   # Dictionary to track items and quantities

    while True:
        item = input("Enter item (or 'END CART' to finish): ").lower()

        if item == "end cart":      # End cart input
            break
        elif item in INVENTORY:     # Valid item, update cart and total
            # Update cart and total
            total += INVENTORY[item]
            if item in cart:
                cart[item] += 1     # Increase item count if already in cart
            else:
                cart[item] = 1      # Add new item to the cart
            print(f"Running total: ${total:.2f}")       # Show running total
        else:
            print(f"{item} is not in inventory.")       # Invalid item
    
    display_receipt(cart)       # Display receipt after checkout

def express_checkout():
    """
    Handles the express-style checkout where all items are entered at once.
    Only the first 10 items are totaled, and an itemized receipt is displayed.
    """
    cart = {}       # Dictionary to track items and quantities
    items = input("Enter items separated by commas: ").lower().split(",")

    for i, item in enumerate(items):
        item = item.strip()     # Remove extra spaces
        if item in INVENTORY and i < 10:   # Only considers first 10 items
            if item in cart:
                cart[item] += 1         # Increase item count if already in cart
            else:
                cart[item] = 1          # Add new item to cart
        elif i >= 10:           # Stop after 10 items
            break
        elif item not in INVENTORY:
            print(f"{item} is not in inventory.")       # Invalid item
    
    display_receipt(cart)       # Display receipt after checkout

def display_receipt(cart):
    """
    Displays the itemized receipt showing the item name, quantity, and price.
    Each item should be displayed on a separate line, followed by the total.
    """
    total = 0       # Initialize total for the cart
    print("\nItemized Receipt:")        # Header for the receipt
    for item, quantity in cart.items():     # Loop through each itme in the cart
        price = INVENTORY[item]     # Get the price of the item from the inventory
        print(f"{item.title()} (x{quantity}): ${price:.2f}")    # Display item, quanity and price
        total += price * quantity       # Update toal based on item quantity
    print(f"\nTotal: ${total:.2f}")     # Display final total with 2 decimal places

# MAIN CODE

def main():
    """
    Main function to select the type of checkout (clerk or express).
    Calls the respective checkout function based on user input.
    If an invalid checkout mehtod is selected, the program will notify the user.
    """

    #Ask user for checkout method
    method = input("Choose checkout method ('clerk' or 'express'): ").lower()

    if method == "clerk":
        clerk_checkout()        # Call clerk checkout function
    elif method == "express":
        express_checkout()      # Call express checkout function
    else:
        print("Invalid checkout method selected.")   # Notify user of invalid selection

# Calls the main function
if __name__ == "__main__":
    main()
