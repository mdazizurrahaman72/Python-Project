def setup_files():
    try:
        file = open("DATA/Catagories.txt","r")
        file.close
    except:
        file = open("DATA/Catagories.txt","w")
        file.write("Food\nTransport\nShopping\nUtilities\n")
        file.close()
        print("Catagories file created")
    
    try:
        file = open("DATA/Transactions.txt","r")
        file.close
    except:
        file = open("DATA/Transactions.txt","w")
        file.write("Data|Type|Catagori|Amount|Description")
        file.close()
        print("Transactions file created")





def main():
    setup_files()
    print("\n Welcome to Personal Finance Manager!")
    
    while True:
        choice = int(input("Enter your choice (1-8) : "))

        if choice == 1:
            print("1. ")
        elif choice == 2:
            print("2.")
        elif choice == 3:
            print("3.")
        elif choice == 4:
            print("4.")
        elif choice == 5:
            print("5.")
        elif choice == 6:
            print("6.")
        elif choice == 7:
            print("7.")
        elif choice == 8:
            print("8.")
        
main()