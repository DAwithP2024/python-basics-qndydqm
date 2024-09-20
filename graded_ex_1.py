# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    if sort_order == "asc":
        return sorted(products_list, key=lambda x: x[1])
    elif sort_order == "desc":
        return sorted(products_list, key=lambda x: x[1], reverse=True)


def display_products(products_list):
    for idx, (product, price) in enumerate(products_list, start=1):
        print(f"{idx}. {product} - ${price}")


def display_categories():
    for idx, category in enumerate(products, start=1):
        print(f"{idx}. {category}")
    try:
        category_index = int(input("Select a category by number: ")) - 1
        if 0 <= category_index < len(products):
            return category_index
        else:
            print("Invalid category selection. Please try again.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None


def add_to_cart(cart, product, quantity):
    cart.append((*product, quantity))


def display_cart(cart):
    print("Your Cart:")
    total_cost = 0
    for product, price, qty in cart:
        total = price * qty
        print(f"{product} - ${price} x {qty} = ${total}")
        total_cost += total
    print(f"Total cost: ${total_cost}")


def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for item, price, qty in cart:
        print(f"{qty} x {item} - ${price} = ${price * qty}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days.")
    print("Payment will be accepted upon delivery.")


def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)


def validate_email(email):
    return "@" in email


def main():
    cart = []
    total_cost = 0

    # Ask for user details
    while True:
        name = input("Please enter your full name: ")
        if validate_name(name):
            break
        print("Invalid name. Please enter your first and last name, containing only alphabets.")

    while True:
        email = input("Please enter your email address: ")
        if validate_email(email):
            break
        print("Invalid email. Please try again.")

    # Category selection and shopping process
    while True:
        print("\nAvailable product categories:")
        display_categories()
        category_index = display_categories()

        if category_index is not None:
            category = list(products.keys())[category_index]
            print(f"\nProducts in {category}:")
            category_products = products[category]
            display_products(category_products)

            while True:
                print("\nOptions:")
                print("1. Select a product to buy")
                print("2. Sort products by price")
                print("3. Go back to category selection")
                print("4. Finish shopping")
                choice = input("Please choose an option: ")

                if choice == '1':
                    try:
                        product_choice = int(input("Enter the product number: ")) - 1
                        if 0 <= product_choice < len(category_products):
                            quantity = int(input("Enter the quantity: "))
                            add_to_cart(cart, category_products[product_choice], quantity)
                            total_cost += category_products[product_choice][1] * quantity
                        else:
                            print("Invalid product number.")
                    except ValueError:
                        print("Please enter valid numbers.")

                elif choice == '2':
                    sort_order = input("Enter 1 for ascending, 2 for descending: ")
                    sort_order = "asc" if sort_order == '1' else "desc"
                    sorted_products = display_sorted_products(category_products, sort_order)
                    display_products(sorted_products)

                elif choice == '3':
                    break

                elif choice == '4':
                    if cart:
                        display_cart(cart)
                        address = input("Enter your delivery address: ")
                        generate_receipt(name, email, cart, total_cost, address)
                    else:
                        print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                    return

                else:
                    print("Invalid option. Please try again.")

    

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
