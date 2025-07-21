import csv
from io import StringIO

def csv_total(file_obj, value_field):
    file_obj.seek(0)
    reader = csv.DictReader(file_obj)
    total = 0
    for row in reader:
        total += float(row[value_field])
    print(f"Total: {total}")
    return total

def csv_total_mult(file_obj, cost_field, qty_field):
    file_obj.seek(0)
    reader = csv.DictReader(file_obj)
    total = 0
    for row in reader:
        multiply = float(row[cost_field]) * float(row[qty_field])
        total += float(multiply)
    print(f"Total: ${round(total,2)}")
    return total

if __name__ == "__main__":
    csv_content = "Net Total\n10\n20\n30\n"
    f = StringIO(csv_content)
    csv_total(f, "Net Total")
    csv_content2 = "Cost,Quantity\n5,2\n3,4\n"
    f2 = StringIO(csv_content2)
    csv_total_mult(f2, "Cost", "Quantity") 