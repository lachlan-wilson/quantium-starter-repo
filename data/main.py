# Reads the data, organises it and outputs it
def process_data():
    data = []   # Initialise data as an empty array
    for i in range(3):  # Loop 3 times (3 files)
        with open(f"daily_sales_data_{i}.csv", "r") as file:   # Open the file
            rows = file.read().splitlines()     # Split the file into an array of rows
            for row in rows:    # Loop for each row
                split_row = row.split(",")  # Split the row into entries
                if split_row[0] == "pink morsel":   # If the product is a pink morsel
                    price = float(split_row[1][1:])     # Store the price as a float (removing the £ sign)
                    data.append((price * int(split_row[2]), split_row[3], split_row[4]))    # Add this row's relevant data to the data array

    with open("processed_data", "w") as file:
        for row in data:
            file.write(f"{row[0]},{row[1]},{row[2]}\n")

process_data()






