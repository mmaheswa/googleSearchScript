from googlesearch import search
import csv
import pandas as pd
import re
from datetime import datetime

pageData = []
print('================================================')
print('GOOGLE COMPANY SEARCH')
print('================================================')

# Get company names in CSV format
csvInputFileName = input('Enter your CSV file name:')
print('Please wait. Your request is being processed. \n')

#Read company CSV
with open(csvInputFileName, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        try:
            resultLinks = []
            # Search the company name in google. It will return 10 results. 
            results = search(row[0], num_results=10)
            companyName = row[0]
            resultLinks.append(companyName)
            matchSite = False
            # Search the company domain in the result list.
            for companySite in results:
                companyKeyword = companyName.split(" ",1)
                if(companyKeyword[0] in companyKeyword):
                    matchedDomain = re.match( r'(http:\/\/|https:\/\/|http:\/\/www.|https:\/\/www.)('+companyKeyword[0]+')', companySite, re.M|re.I)
                    if matchedDomain:
                        resultLinks.append(companySite)
                        matchSite = True
                        break
                    else:
                        continue
            if(matchSite == False):
                resultLinks.append("Website N/A")
            pageData.append(resultLinks)
        except:
            continue
# Convert result into data frame.
df = pd.DataFrame(pageData)
now = datetime.now()
outputFileName = 'companyListOutput' + now.strftime("%d-%m-%Y") + '.csv'
# Write output in CSV format.
df.to_csv(outputFileName,mode='a', encoding='utf-8', index=False , header=False)
print('================================================\n')
print('Your data has been processed successfully!!. Please check the output in the below file!!\n')
print(outputFileName + '\n')
print('================================================\n')
