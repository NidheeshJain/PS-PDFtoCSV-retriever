import csv
array = []
final_array = []

print("1. Use this to convert pdf to excel. https://smallpdf.com/pdf-to-excel")
print("2. Open the above downloaded file in excel, and save as downloadedPDF.csv - comma delimited in the folder of script itself")
print("3. The downloadedPDF.csv should look like downloadedPDF-sample.csv as in the script folder")
cc = input("4. Once you are done with above steps, press Enter")

print("Please go through following basic checks before proceeding further \n")
print("1. There's a base.csv file present in the folder this script is run")
print("2. There's a downloadedPDF.csv file present in the folder this script is run")
print("3. Make a safe copy of downloadedPDF.csv so that no data is lost in case of mishap.")
print("4. The downloadedPDF.csv should not have any header rows having BITS Pilani logo or anything. The very first row should be station only, and it's 2nd column should contain the name of stations.")

continuee = input("Hoping you have completed the above checks, press Enter to continue.")


with open('downloadedPDF.csv') as pdf_file:
    csv_reader = csv.reader(pdf_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
            array.append(row[1])
            line_count += 1

for element in array:
    found = False
    with open('base.csv') as tbu_file:
        csv_reader = csv.reader(tbu_file, delimiter=',')
        for company in csv_reader:
            if company[1].strip() == element.strip() :
                company[1] = element
                final_array.append(company)
                found = True
    if not found:
        print (f"{element} was not found automatically. Please locate it manually in base CSV.")
        row_no = int(input('Enter row number from base csv'))

        if row_no > 0:
            with open('base.csv') as tbu1_file:
                csv1_reader = csv.reader(tbu1_file, delimiter=',')
                for company in csv1_reader:
                    if (row_no == 1):
                        company[1] = element
                        print(company)
                        print("appended\n\n")
                        final_array.append(company)
                        break
                    else:
                        row_no -= 1
 
with open('StationDetails.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Station ID",	"Company Name",	"Location",	"Industry Domain",	"Preferred Branches",	"Stipend (UG)",	"Stipend (PG)",	"Have Accommodation?(Y or N)"])
    writer.writerows(final_array)

print("The process is completed. Some duplicates might have been introduced, which can be removed from excel -> Data -> Remove Diuplicates")
print("Please check that there are as many rows as total number of station in base.csv using check.py")
