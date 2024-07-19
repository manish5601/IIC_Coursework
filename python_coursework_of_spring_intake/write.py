import operation
import datetime

def buy_product():
    operation.available_product()
    
    updated_records = []
    found = False

    while not found:  # Continue until a valid product ID is entered
        try:
            unique_id = int(input('Enter id of the product: '))
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer for product ID.")
            continue
        
        try:
            buy_quantity = int(input(f"Enter quantity of product '{unique_id}' you buy: "))
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer for buy quantity.")
            continue

        with open("file.txt", "r") as f:
            lines = f.readlines()

        for line in lines:
            record = line.strip().split(",")
            if unique_id == int(record[0]):  
                current_stock = int(record[-2])
                new_stock = current_stock + buy_quantity
                record[-2] = str(new_stock)  # Update stock in record
                
                # Calculate price and update price field if needed
                price_str = record[-1].strip().lstrip('$')
                try:
                    float_price = float(price_str)
                except ValueError:
                    print(f"Error: Unable to convert price '{price_str}' to float.")
                    break
                updated_records.append(",".join(record))
                found = True

                # Generate invoice content for the current transaction
                invoice_content = (
                    f"=====================================\n"
                    f"Buying Invoice:\n"
                    f"=====================================\n"
                    f'Invoice Date: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
                    f'-------------------------------------\n'
                    f'Buyer name: BRJ Furniture Store\n'
                    f'-------------------------------------\n'
                    f'Manufacturer name: {record[1]}\n'
                    f'-------------------------------------\n'
                    f'ID: {record[0]}\n'  # Correctly use the product ID of the current record
                    f'-------------------------------------\n'
                    f'Product Name: {record[2]}\n'
                    f'-------------------------------------\n'
                    f'Quantity: {buy_quantity}\n'
                    f'-------------------------------------\n'
                    f'Unit price: {record[-1]}\n'
                    f'-------------------------------------\n'
                    f'Total price: {buy_quantity * float_price}\n'  # Calculate total price
                    f'=====================================\n'
                )

                # Display invoice in terminal
                print(invoice_content)

                # Write invoice details to a file (append mode)
                with open(f'Buying_Invoice_{record[0]}.txt', "a") as f:
                    f.write(invoice_content + '\n')

            else:
                updated_records.append(",".join(record))

        if not found:
            print("Invalid product ID! Please enter a valid ID.")
            return

    # Write all records back to the file
    with open("file.txt", "w") as f:
        for updated_record in updated_records:
            f.write(updated_record + "\n")

    print(f"Successfully bought {buy_quantity} units of product with ID '{unique_id}'.")



import operation
import datetime

def sell_product():
    operation.available_product()
    
    updated_records = []
    found = False

    while not found:  # Continue until a valid product ID is entered
        try:
            selling_id = int(input('Enter id of the product: '))
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer for product ID.")
            continue
        
        try:
            sell_quantity = int(input(f"Enter quantity of product '{selling_id}' you sell: "))
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer for sell quantity.")
            continue

        with open("file.txt", "r") as f:
            lines = f.readlines()

        for line in lines:
            record = line.strip().split(",")
            if selling_id == int(record[0]):  
                current_stock = int(record[-2])
                if sell_quantity <= current_stock:
                    new_stock = current_stock - sell_quantity
                    record[-2] = str(new_stock)  # Update stock in record
                    
                    # Update other details if needed (customer name, address, etc.)
                    try:
                        price_str = record[-1].strip().lstrip('$')
                        float_price = float(price_str)
                    except ValueError:
                        print(f"Error: Unable to convert price '{price_str}' to float.")
                        break
                    
                    price = sell_quantity * float_price
                    vat = (price / 100) * 13
                    total_price = price + vat
                    
                    # Input customer name and address as strings
                    while True:
                        name = input("Enter customer name: ")
                        if isinstance(name, str):
                            break
                        else:
                            print("Error: Please enter a valid string for customer name.")
                    
                    while True:
                        address = input("Enter customer address: ")
                        if isinstance(address, str):
                            break
                        else:
                            print("Error: Please enter a valid string for customer address.")
                    
                    # Update the line with the new information
                    record[-1] = f"${total_price}"  # Update the price (assuming it's the last element)
                    
                    # Join the record back into a string and add to updated_records
                    updated_records.append(",".join(record) + "\n")
                    found = True

                    # Generate invoice content for the current transaction
                    invoice_content = (
                        f"=====================================\n"
                        f"Selling Invoice:\n"
                        f"=====================================\n"
                        f'Invoice Date: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
                        f'-------------------------------------\n'
                        f'Customer name: {name}\n'
                        f'-------------------------------------\n'
                        f'Customer address: {address}\n'
                        f'-------------------------------------\n'
                        f'Product ID: {record[0]}\n'  # Correctly use the product ID of the current record
                        f'-------------------------------------\n'
                        f'Product Name: {record[2]}\n'
                        f'-------------------------------------\n'
                        f'Quantity: {sell_quantity}\n'
                        f'-------------------------------------\n'
                        f'Unit price: {record[-1]}\n'
                        f'-------------------------------------\n'
                        f'Price: {price}\n'
                        f'-------------------------------------\n'
                        f'VAT amount: {vat}\n'
                        f'-------------------------------------\n'
                        f'Total price: {total_price}\n'
                        f'=====================================\n'
                    )

                    # Display invoice in terminal
                    print(invoice_content)

                    # Write invoice details to a file (append mode)
                    with open(f'Selling_Invoice_{name}.txt', "a") as f:
                        f.write(invoice_content + '\n')

                else:
                    print(f"Error: Insufficient stock for product '{record[2]}'")
                    updated_records.append(line)  # Append the original line
            else:
                updated_records.append(line)  # Append the original line

        if not found:
            print("Invalid product ID! Please enter a valid ID.")

    # Write all records back to the file
    with open("file.txt", "w") as f:
        f.writelines(updated_records)

