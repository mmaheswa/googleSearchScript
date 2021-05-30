from googlesearch import search
import xlsxwriter
import csv
import pandas as pd
pageData = []
csvInputFileName = input('Enter your CSV file name: ') #search query

with open(csvInputFileName, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        resultLinks = []
        results = search(row[0], num_results=1)
        resultLinks.append(row[0])
        resultLinks.append(results[0])
        pageData.append(resultLinks)

df = pd.DataFrame(pageData)
df.to_csv('companyListOutput.csv',mode='a', encoding='utf-8', index=False , header=False)
