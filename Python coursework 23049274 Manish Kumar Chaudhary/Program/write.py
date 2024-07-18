import datetime

def write_record(Name, Address, Kitta_no, Months):
    with open('file.txt', 'r') as f:
        container = f.readlines()
        found_status = False
        for contents in container:
            content = contents.strip().split(',')
            if content[0] == Kitta_no:
                content[4] = int(content[4]) * int(Months)
                # Creating invoice content
                invoice_content = (
                    f'-------------------------------------\n'
                    f'Invoice Date: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
                    f'-------------------------------------\n'
                    f'Customer Name: {Name}\n'
                    f'-------------------------------------\n'
                    f'Customer Address: {Address}\n'
                    f'-------------------------------------\n'
                    f'Kitta Number: {content[0]}\n'
                    f'-------------------------------------\n'
                    f'City/District: {content[1]}\n'
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

              

                # Writing invoice to a file
                invoice_filename = f'Invoice_{Kitta_no}_{Name.replace(" ", "_")}.txt'
                with open(invoice_filename, 'w') as invoice_file:
                    invoice_file.write(invoice_content)
                found_status = True
                break
        if not found_status:
            print("Kitta Number is not found, please enter valid one")

def rent_Info(Kitta_no, Name, Address, Months):
    with open("C:\\Users\\User\\Downloads\\Python CourseWork\\file.txt", "r") as f:
        rent = f.readlines()
        
    with open('RentData.txt', 'a') as f:  # Open file in write mode ('w') outside the loop
        for contents in rent:             
            content = contents.strip().split(",")
            if content[0] == Kitta_no: 
                content[4]= int(content[4])*int(Months)
                f.write(f'{Name},{Address},{Kitta_no},{content[4]},{Months}\n')  # Write data for each entry on a new line
                break