import operation
import read
import write

while True:
    print("\t----------------------------------------------------------------------\t")
    print("\t--------------------Welcome to BRJ Furniture Store--------------------\t")
    print("\t----------------------------------------------------------------------\t")

    while True:
        print("\t------------------------------")
        print("\tSelect an operation:")
        print("\t------------------------------")
        print("\t1. To Show all data")
        print("\t2. To Get available stock")
        print("\t3. To Buy product")
        print("\t4. To Sell product")
        print("\t5. To Exit program")
        print("\t-----------------------------")

        try:
            choice = int(input("Enter 1, 2, 3, 4 or 5: "))
            if choice == 1:
                read.show_data()
                break
            elif choice == 2:
                operation.available_product()
                break
            elif choice == 3:
                write.buy_product()
                break
            elif choice == 4:
                write.sell_product()
                break
            elif choice == 5:
                print('Exiting program.....')
                break
            else:
                print('Invalid options. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')
    if choice == 5:
        break

    while True:            
        print("Do you want to perform more operations?")
        print("1. Yes")
        print("2. No")

        try:
            enter = int(input('Enter 1 or 2: '))
            if enter == 1:
                continue_status = True
                break
            elif enter == 2:
                continue_status = False
                break
            else:
                print("Invalid option. Please re-enter.")
        except ValueError:
            print('Invalid input. Please enter 1 or 2.')

    if not continue_status:
        print("Program ended.")
        break
