import datetime


def take_data(Name,Address,Kitta_number,Months):
    with open("file.txt","r")as f:
        container=f.readlines()
        FoundStatus=False
        for contents in container:
            content=contents.strip().split(",")
            if content[0]==Kitta_number:
                content[4]=int(content[4])*int(Months)
                # Creating invoice 
                content[5]='Rented'
                # Create invoice content
                invoice_content = (
                    f'Invoice Date: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
                    f'-------------------------------------\n'
                    f'Customer Name: {Name}\n'
                    f'-------------------------------------\n'
                    f'Customer Address: {Address}\n'
                    f'-------------------------------------\n'
                    f'Kitta Number: {content[0]}\n'
                    f'-------------------------------------\n'
                    f'Place: {content[1]}\n'
                    f'-------------------------------------\n'
                    f'Direction: {content[2]}\n'
                    f'-------------------------------------\n'
                    f'Anna: {content[3]}\n'
                    f'-------------------------------------\n'
                    f'Price: {content[4]}\n'
                    f'-------------------------------------\n'
                    f'Status: {content[5]}\n'
                    f'-------------------------------------\n'
                    f'Months Rented: {Months}\n'
                    f'=====================================\n'
                )

                # Displaying invoice in terminal 
                print("=====================================\n")                      
                print("Rent Invoice:\n")
                print("=====================================\n")
                print(invoice_content)

                FoundStatus=True
                break
        if not FoundStatus:
            print("Entered Kitta Number is not found in the system")

#Function to show recorded data        
def show_data():
    print("=========================================================================================================================================================")
    print("|\tKitta Number\t|\tcity/district\t\t|\tDirection\t|\tAnna\t |  \tPrice\t        |\tAvailability\t        |")
    print("=========================================================================================================================================================")
    with open("file.txt", "r") as f:
        contents = f.readlines()
        for content in contents:
            cont = content.strip().split(",")

            print(f"|\t {cont[0]}          \t|\t {cont[1]}       \t| {cont[2]}            \t|\t {cont[3]}   \t |\t {cont[4]}   \t|\t {cont[5]}      \t|")
            print("---------------------------------------------------------------------------------------------------------------------------------------------------------")

#Function to show available land data
def available_land():
    print("=========================================================================================================================================================")
    print("|\tKitta Number\t|\tcity/district\t\t|\tDirection\t|\tAnna\t |  \tPrice\t        |\tAvailability\t        |")
    print("=========================================================================================================================================================")
    with open("C:\\Users\\User\\Downloads\\Python CourseWork\\file.txt", "r") as f:
        contents = f.readlines()
        for content in contents:
            cont = content.strip().split(",")
            if cont[5].strip().lower() == "available":
                print(f"|\t {cont[0]}          \t|\t {cont[1]}       \t| {cont[2]}            \t|\t {cont[3]}   \t |\t {cont[4]}   \t|\t {cont[5]}      \t|")
            # print("-------------------------------------------------------------------------------------------------------------------------------------")
def return_info(Name,Address,Delaymonth):
        intDelaymonth = int(Delaymonth)  # Ensure Delaymonth is an integer
        TotalPayment = 0
        invoice_contents = []  # This will store each line of the invoice

        with open("RentData.txt", "r") as f:
            records = f.readlines()

        for record in records:
            content = record.strip().split(",")
            if content[0] == Name and content[1] == Address:
                # Calculate payment including the delay penalty
                payment_due = int(content[3]) + 5000 * intDelaymonth
                TotalPayment += payment_due
                # Prepare the invoice details
                invoice_line = (
                    f'Name: {content[0]}\n'
                    f'-------------------------------------\n'
                    f'Address: {content[1]}\n'
                    f'-------------------------------------\n'
                    f'Kitta Number: {content[2]}\n'
                    f'-------------------------------------\n'
                    f'Months Rented: {content[4]}\n'
                    f'-------------------------------------\n'
                    f'Initial Payment: {content[3]}\n'
                    f'-------------------------------------\n'
                    f'Delay Penalty: {5000 * intDelaymonth}\n'
                    f'=====================================\n'
                    # f'Total Payment Due: {payment_due}\n'
                )
                invoice_contents.append(invoice_line)

        # Check if there are any invoices to process
        if invoice_contents:
            # Write the invoice details to a file
            with open(f'Return_Invoice_{Name}.txt', "a") as f:
                for line in invoice_contents:
                    f.write(line + '\n')
        
            # Display the invoice in the terminal
            print("=====================================\n")
            print("Return Invoice: \n")
            print("=====================================\n")
            for line in invoice_contents:
                print(line)
            
            print('-----------------------------------------------------------------------------------------------------')    
            print("Total Payment: ", TotalPayment)
            print('-----------------------------------------------------------------------------------------------------')    

        else:
            print("No such records found, please try again!")
