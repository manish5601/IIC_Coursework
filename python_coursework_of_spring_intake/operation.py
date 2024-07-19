

#Function to show available furniture data
def available_product():
    # Header for the table
    print("========================================================================================================")
    print("|    ID |        Manufacturer                 |    Product         |    Stock |    Price |")
    print("========================================================================================================")
    
    # Open file for reading
    with open("file.txt", "r") as f:
        for line in f:
            cont = line.strip().split(",")
            stock = int(cont[3].strip())
            if stock > 0:  # Only display if stock is greater than 0
                # Extracting individual fields
                product_id = cont[0].strip()
                manufacturer = cont[1].strip()
                product_name = cont[2].strip()
                price = cont[4].strip()
                
                # Printing formatted row
                print(f"| {product_id.ljust(5)} | {manufacturer.ljust(30)} | {product_name.ljust(20)} | {str(stock).ljust(6)} | {price.ljust(8)} |")
                print("--------------------------------------------------------------------------------------------------------")
    
    # Footer for the table
    print("========================================================================================================")





