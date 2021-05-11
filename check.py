import csv
with open('base.csv') as pdf_file:
    csv_reader = csv.reader(pdf_file, delimiter=',')
    for row in csv_reader:
        found = False
        with open('StationDetails.csv') as new_file:
            cc_reader = csv.reader(new_file, delimiter=',')
            for roww in cc_reader:
                if (row[0] == roww[0]):
                    found = True
                    break
            if not found:
                print(row)