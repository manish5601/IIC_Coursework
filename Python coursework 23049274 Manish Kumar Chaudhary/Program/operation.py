def update_status(Kitta_no):
    updated_records = []
    with open("C:\\Users\\User\\Downloads\\Python CourseWork\\file.txt", "r") as f:
        for line in f:
            record = line.strip().split(", ")
            if record[0] == Kitta_no:
                record[-1] = "Not Available"
            updated_records.append(", ".join(record))

    with open("file.txt", "w") as f:
        for record in updated_records:
            f.write(record + "\n")


def return_status(Kitta_no):
    update_records = []
    with open("file.txt", "r") as f:
        
        for line in f:
            record = line.strip().split(", ")
            if record[0] == Kitta_no:
                record[-1]="Available"
            update_records.append(", ".join(record))

    with open("file.txt", "w") as f:
        for record in update_records:
            f.write(record + "\n")


                


