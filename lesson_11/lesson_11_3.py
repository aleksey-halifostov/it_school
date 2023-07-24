import openpyxl
import csv

book = openpyxl.Workbook()
sheet = book["Sheet"]

with open("02.csv") as file:
    file = csv.reader(file)

    for ind, elem in enumerate(file):
        line = 1

        if ind:
            elem.insert(0, f"user{ind}")
        else:
            elem.insert(0, "")

        for value in elem:
            if not elem.index(value) == 3:
                cell = sheet.cell(row=line, column=ind+1)
                cell.value = value
                line += 1


book.save("03.xlsx")
