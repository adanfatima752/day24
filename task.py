def add_product(inventory):
    """
    Adds a new product to the inventory.
    
    Args:
    - inventory: A list of dictionaries representing the current inventory.
    """
    name = input("Enter the product name: ").strip()
    price_str = input("Enter the product price: ").strip()
    quantity_str = input("Enter the quantity in stock: ").strip()
    
    # Validate inputs
    try:
        price = float(price_str)
        if price <= 0:
            raise ValueError("Price must be positive.")
        quantity = int(quantity_str)
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    
    # Check if the product already exists
    for product in inventory:
        if product['name'].lower() == name.lower():
            print("Product already exists in inventory.")
            return
    
    # Add new product
    product = {
        'name': name,
        'price': price,
        'quantity': quantity
    }
    inventory.append(product)
    print("Product added successfully.")

def update_quantity(inventory):
    """
    Updates the quantity of an existing product.
    
    Args:
    - inventory: A list of dictionaries representing the current inventory.
    """
    name = input("Enter the product name to update: ").strip()
    quantity_str = input("Enter the new quantity: ").strip()
    
    # Validate quantity
    try:
        quantity = int(quantity_str)
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    
    # Find and update the product
    for product in inventory:
        if product['name'].lower() == name.lower():
            product['quantity'] = quantity
            print("Quantity updated successfully.")
            return
    
    print("Product not found in inventory.")

def display_inventory(inventory):
    """
    Displays all products in the inventory.
    
    Args:
    - inventory: A list of dictionaries representing the current inventory.
    """
    if not inventory:
        print("Inventory is empty.")
        return
    
    print("\nInventory:")
    for product in inventory:
        print(f"Name: {product['name']}, Price: ${product['price']:.2f}, Quantity: {product['quantity']}")
    print()

def main():
    """
    Manages the workflow of the inventory management system.
    """
    inventory = []
    
    while True:
        print("Inventory Management System")
        print("1. Add Product")
        print("2. Update Quantity")
        print("3. View Inventory")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ").strip()
        
        if choice == '1':
            add_product(inventory)
        elif choice == '2':
            update_quantity(inventory)
        elif choice == '3':
            display_inventory(inventory)
        elif choice == '4':
            print("Exiting the inventory management system.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
