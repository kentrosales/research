counter = 1000
def add_inventory_item():
    item_details = []
    while True:
        global counter
        item_name = input("Enter Item Name: ")
        quantity = int(input("Quantity: "))
        item_price = float(input("Enter Item Price: "))
        
        item_id = counter
        counter += 1

        #inventory_item variables = current item
        current_item = [item_name, item_id, quantity, item_price]
        item_details.append(current_item)

        for item in item_details:
            name = item[0].capitalize()
            item_id = item[1]
            qty = item[2]
            price = item[3]
        print(f"""
            Item Name: {name}
            Item ID: {item_id}
            Quantity: {qty}
            Price per Item: ${price}""")
        done = input("Type 'done' to quit, press Enter to add another: ")
        if done == "done":
            break
    return item_details

inventory_item = add_inventory_item()

def calculate_total_value():
    total = 0.0
    for item in inventory_item:
        qty = item[2]
        price = item[3]
        subtotal = qty * price
        total += subtotal
    print(f"The total is: ${total}") 
    return total

total = calculate_total_value()

def update_inventory(inventory_list):
    print("\nUpdating Inventory Item:")
    
    search_id = int(input("Enter Item ID: "))
    found = False

    for i in range(len(inventory_list)):
        if inventory_list[i][1] == search_id:
            new_qty = int(input("New Quantity: "))
            new_price = float(input("New Price per Item: $"))
            item_name = inventory_list[i][0]
            inventory_list[i] = (item_name, search_id, new_qty, new_price)
            print(f"\nInventory Updated: Item ID {search_id} has been updated to Quantity {new_qty} and Price ${new_price:.2f}.")
            found = True
            break
    if not found:
        print(f"\nError: Item ID {search_id} was not found.")

update_inventory(inventory_item)

def display_inventory_item(inventory_list, total):
    for i in inventory_list:
        name = i[0]
        price = i[3]
        qty = i[2]
        item_id = i[1]
    print(f"""
    Item Name: {name.capitalize()}
    Item ID: {item_id}
    Quantity: {qty}
    Price per Item: ${price}
    Total: ${total}""")

display_inventory_item(inventory_item, total)
