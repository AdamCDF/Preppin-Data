import pandas as pd
import numpy as np

df = pd.read_csv(
    'C:\\Users\\Adam\\Documents\\GitHub\\Preppin Data\\Inputs\\PDW2\\Transactions.csv')
df2 = pd.read_csv(
    'C:\\Users\\Adam\\Documents\\GitHub\\Preppin Data\\Inputs\\PDW2\\Swift Codes.csv')

# In the Transactions table, there is a Sort Code field which contains dashes. We need to remove these so just have a 6 digit string

df['Sort Code'] = df['Sort Code'].str.replace("-", "")
print(df)

# Use the SWIFT Bank Code lookup table to bring in additional information about the SWIFT code and Check Digits of the receiving bank account

# df3 = df.set_index('Bank').join(df2.set_index('Bank'))
df3 = df.join(df2.set_index('Bank'), on='Bank')

# Add a field for the Country Code 

df3['Country Code'] = 'GB'

# Create the IBAN as above 

df3['IBAN'] = df3['Country Code'] + df3['Check Digits'].astype(str) + \
    df3['SWIFT code'].astype(str) + df3['Sort Code'].astype(str) + \
    df3['Account Number'].astype(str)
print(df3)

df4 = df3.drop(['Account Number', 'Sort Code', 'Bank',
               'SWIFT code', 'Check Digits', 'Country Code'], axis=1)
print(df4)

# Hint: watch out for trying to combine sting fields with numeric fields - check data types
# Remove unnecessary fields 


print('Done')
