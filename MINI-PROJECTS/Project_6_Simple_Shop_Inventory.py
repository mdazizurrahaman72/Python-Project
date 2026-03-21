def view_products():
    print("\n---------All Product---------")
    if len(products) !=0: 

        print(f"{'Product':<12} {'Price (৳)':<15} {'Status'}")
        print("-" * 40)
        for product, price in products.items():
            if product in in_stock:
                status = "✅ Available"
            else:
                status = "❌ Out of Stock"
            print(f"{product:<15} {price:<10} {status}")
    else:
        print("No products in shop!")

def add_products():
    print("--------Add new product----------")
    new_product = input("Enter product name: ")

    if new_product in products:
        print(f"⚠️ {new_product} is alrady exists!")
    else:
        price = int(input("Enter price in Taka: "))
        products[new_product] = price

        stock_status = input("Is it in stock? (yes/no): ")

        if stock_status.lower() == "yes":
            in_stock.add(new_product)
        else:
            out_of_stock.add(new_product)

        print(f"✅ {new_product} added with price ৳ {price}")

def update_price():
    print("\n----- Update Price -----")
    product_name = input("Enter product name: ")

    if product_name in products:
        old_price = products[product_name]
        print("Cuttent price:",old_price)
        new_price = int(input("Enter new price: "))
        products[product_name] = new_price
        print(f"✅ Price updated from ৳ {old_price} to ৳ {new_price}")
    else:
        print(f"❌ {product_name} not found!")

def mark_out_of_stock():
    print("\n---------Mark out of stock-------")
    product_name = input("Enter product name: ")

    if product_name not in products:
        print(f"❌ {product_name} not found!")
    elif product_name in out_of_stock:
        print(f"⚠️ {product_name} is already out of stock!")
    else:
        in_stock.discard(product_name)
        out_of_stock.add(product_name)
        print(f"✅ {product_name} marked as out of stock")

def mark_in_stock():
    print("\n---------Mark in stock-------")
    product_name = input("Enter product name: ")

    if product_name not in products:
        print(f"❌ {product_name} not found!")
    elif product_name in in_stock:
        print(f"⚠️ {product_name} is already in stock!")
    else:
        out_of_stock.discard(product_name)
        in_stock.add(product_name)
        print(f"✅ {product_name} is back in stock!")

def view_stock_status():
    print("\n--- Stock Status ---")
    print(f"\n✅ In Stock ({len(in_stock)} items):")
    if len(in_stock) > 0:
        for item in in_stock:
            if item in products:  
                print(f"  • {item}: ৳ {products[item]}")
    else:
        print("  No items in stock")

    print(f"\n❌ Out of Stock ({len(out_of_stock)} items):")
    if len(out_of_stock) > 0:
        for item in out_of_stock:
            if item in products:  
                print(f"  • {item}: ৳ {products[item]}")
    else:
        print("  All items are in stock")     

def total_price():
    print("\n--- Shop Value ---")
    total_value = 0

    for product in in_stock:
        if product in products:
            total_value = total_value + products[product]

    print(f"Total value of in-stock items: ৳ {total_value}")
    print(f"Number of products in stock: {len(in_stock)}")
    print(f"Number of products out of stock: {len(out_of_stock)}")

products = {
    "Rice" : 65,
    "Oil" : 180,
    "Sugar" : 140,
    "Salt" : 35,
    "Milk" : 90
}

categories = {"Food","Drinks","Snacks"}
in_stock = {"Rice","Oil","Sugar","Salt","Milk"}

out_of_stock = set()

print("🏪 Welcome to Simple Shop Inventory!")
print("="*40)

keep_running = True

while keep_running:
    print("\nWhat do you want to do? ")
    print("1. View all products and prices")
    print("2. Add new product")
    print("3. Update price")
    print("4. Mark product as out of stock")
    print("5. Mark product as back in stock")
    print("6. View stock status")
    print("7. Calculate total value")
    print("8. Exit")

    choice = int(input("\nEnter your choice (1-8): "))

    if choice == 1:
        view_products()
    elif choice == 2:
        add_products()
    elif choice == 3:
        update_price()
    elif choice == 4:
        mark_out_of_stock()
    elif choice == 5:
        mark_in_stock()
    elif choice == 6:
        view_stock_status()
    elif choice == 7:
        total_price()
    elif choice == 8:
        print("\n👋 Thank you for using Shop Inventory!")
        keep_running = False
    else:
        print("❌ Invalid choice! Please enter (1-8)")

print("\nProgram ended.")