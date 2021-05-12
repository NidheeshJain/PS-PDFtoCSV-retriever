# PS-PDFtoCSV-retriever
Just have your PDF and no csv? Make csv using just your pdf.
## Instructions to use:
1. Use this to convert your downloaded pdf to excel. https://smallpdf.com/pdf-to-excel
2. Open the above downloaded file in excel, and save as downloadedPDF.csv - comma delimited in the folder of script itself.
3. The downloadedPDF.csv should look like downloadedPDF-sample.csv as in the script folder.
4. (Optional) It's preferrable that you make your own latest base.csv by -g command over https://github.com/rutvora/PS_Helper and then renaming it. This would ensure that station list is consistent with PSD database.

## Go through following basic checks before proceeding further
1. There's a base.csv file present in the folder this script is run.
2. There's a downloadedPDF.csv file present in the folder this script is run.
3. Make a safe copy of downloadedPDF.csv so that no data is lost in case of mishap.
4. The downloadedPDF.csv should not have any header rows having BITS Pilani logo or anything. The very first row should be station only, and it's 2nd column should contain the name of stations.

## After the script execution is done:
Time for some cleaning:
1. Open the generated StationDetails.csv in excel.
2. Some duplicates might have been introduced, which can be removed from excel -> Data -> Remove Diuplicates (Select all range).
3. Please check that there are as many rows as total number of station in base.csv using check.py
4. If any station is missing, copy the row from base.csv manually and paste it in StationDetails.csv
5. Use https://github.com/rutvora/PS_Helper or https://chrome.google.com/webstore/detail/ps-companion/jaleeakcpipiimnpmbjlimcgmojdjdad to upload the generated csv to PSD website.
