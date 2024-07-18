import read
import write
import operation
while True:
    print("\t----------------------------------------------------------------------\t")
    print("\t-------------------Welcome to Techno Property Nepal-------------------\t")
    print("\t----------------------------------------------------------------------\t")
    while True:
        print("Select operation:")
        print("1. Choose 1 to Show all the data")
        print("2. Choose 2 to Rent a Land")
        print("3. Choose 3 to Return a Land")
        print("4. Choose 4 to Exit")
        # Using exception handling to ensure valid input
        try:
            choice = int(input("Enter choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        if choice == 1:
            read.show_data()
        elif choice == 2:
            read.available_land()
            print("\t----------------------------------------------------------------------\t")
            print("\t-------------------Please provide us your details---------------------\t")
            print("\t----------------------------------------------------------------------\t")
            name = input("Enter your Name: ")
            address = input("Enter address: ")
            kitta_no = input("Enter Kitta Number that you want to rent: ")
            with open("file.txt", "r") as f:
        
                for line in f:
                    record = line.strip().split(", ")
                    if record[0] == kitta_no:
                        record[-1]="Not Available"
                        print("Invalid Kitta no")
                        break
                    else:
                        months = input("Enter numbers of months you want to rent: ") 
                        write.rent_Info(kitta_no, name, address, months)
                        read.take_data(name, address, kitta_no, months)
                        operation.update_status(kitta_no)
                        write.write_record(name, address, kitta_no, months)
        
                        break  # Break out of the inner loop to return to the main menu
        elif choice == 3:
            print("\t----------------------------------------------------------------------\t")
            print("\t-------------------Please provide us your details---------------------\t")
            print("\t----------------------------------------------------------------------\t")
            name = input("Enter your Name: ")
            address = input("Enter address: ")
            kitta_no=input("Enter Kitta Number that you want to return: ")
            delay_month=input("Enter number of months you were  delay: ")
            read.return_info(name, address, delay_month)
            operation.return_status(kitta_no)
            break  # Break out of the inner loop to return to the main menu
        elif choice == 4:
            print('Thank you for renting from Techno Property Nepal')
            exit()  # Exit the program
        else:
            print('Invalid Option')
            continue

        # Ask user if they want to perform more operations
        while True:
            print("Do you want to perform more operation: ")
            print("1. Yes")
            print("2. No")
            try:
                choice = input("Enter choice (1-2): ")
            except ValueError:
                print("Invalide choice please enter number 1 or 2")
            if choice == "1":
                continue_status=True
                break
            elif choice == "2":
                print("Thank you for renting from Techno Property Nepal")
                continue_status = False
                break
            else:
                print("Invalid choice")
                choice = input("Enter choice (1-2): ")
        if not continue_status:
            break

