
# ISM2411 Lab 12
# Name: Aliyah Fisher

# REFLECTION 1:
# Python allows you to automate repetitive data cleaning and calculations . 
# Especially with large datasets .Excel is easier to quickly view, edit and 
# create visual charts.

# REFLECTION 2:
# A business might have an append-mode log 
# of daily sales reports. Append mode is helpful, 
# because it adds new records without deleting previous 
# ones, preserving a history .

import csv
from datetime import datetime

# EXERCISE 1: SETUP
file_path = "data/sales.csv"

# EXERCISE 2: READ AND PRINT RAW ROWS
print("EXERCISE 2: RAW ROWS")

with open(file_path, "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# EXERCISE 3: SKIP THE HEADER
print("\nEXERCISE 3: HEADER AND DATA")

with open(file_path, "r", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)


# EXERCISE 4: COMPUTE TOTALS
print("\nEXERCISE 4: SALES TOTALS")

total_revenue = 0

with open(file_path, "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(
            f"{product}: {quantity} units × "
            f"${price:.2f} = ${total:.2f}"
        )

print(f"Total Revenue: ${total_revenue:.2f}")


# EXERCISE 5: FILTER AND WRITE
print("\nEXERCISE 5: CLEANED CSV")

original_count = 0
cleaned_count = 0

with open(file_path, "r", newline="") as infile:
    reader = csv.reader(infile)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total = price * quantity

            if total > 100:
                writer.writerow([
                    product,
                    f"{price:.2f}",
                    quantity,
                    f"{total:.2f}"
                ])
                cleaned_count += 1

print(f"Original rows: {original_count}")
print(f"Cleaned rows written: {cleaned_count}")


# EXERCISE 6: DICTREADER
print("\nEXERCISE 6: DICTREADER TOTALS")

# csv.reader is useful for simple files when column order is known.
# DictReader is better when column names make data easier to access.

dict_total_revenue = 0

with open(file_path, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total_revenue += total

        print(f"{product}: ${total:.2f}")

print(f"DictReader Total Revenue: ${dict_total_revenue:.2f}")


# EXERCISE 7: SALES SUMMARY BY PRODUCT
print("\nEXERCISE 7: PRODUCT SUMMARY")

sales_summary = {}

with open(file_path, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")


# EXERCISE 8: APPEND MODE LOG
print("\nEXERCISE 8: RUN LOG")

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as file:
    file.write(
        f"{current_time} - Total Revenue: "
        f"${total_revenue:.2f}\n"
    )

print("Run log updated successfully.")
