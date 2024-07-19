def show_data():
    # Header for the table
    print("========================================================================================================")
    print("|    ID |        Manufacturer                 |    Product         |    Stock |    Price |")
    print("========================================================================================================")
    
    # Open file for reading
    with open("file.txt", "r") as f:
        contents = f.readlines()
        for content in contents:
            cont = content.strip().split(",")
            # Extracting individual fields
            product_id = cont[0].strip()
            manufacturer = cont[1].strip()
            product_name = cont[2].strip()
            stock = cont[3].strip()
            price = cont[4].strip()
            
            # Printing formatted row
            print(f"| {product_id.ljust(5)} | {manufacturer.ljust(30)} | {product_name.ljust(20)} | {stock.ljust(6)} | {price.ljust(8)} |")
            print("--------------------------------------------------------------------------------------------------------")

    # Footer for the table
    print("========================================================================================================")
