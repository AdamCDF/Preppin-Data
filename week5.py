import pandas as pd
import numpy as np

# Input data

df = pd.read_csv('Preppin Data\Inputs\PD 2023 Wk 1 Input.csv')

# Create the bank code by splitting out off the letters from the Transaction code, call this field 'Bank'

df['Bank'] = df['Transaction Code'].str.split('-', expand=True)[0]

# Change transaction date to the just be the month of the transaction

df['Transaction Month'] = df['Transaction Date'].str.split('/', expand=True)[1]

# Total up the transaction values so you have one row for each bank and month combination

df2 = df.groupby(['Bank', 'Transaction Month'], as_index=False)['Value'].sum()

# Rank each bank for their value of transactions each month against the other banks. 1st is the highest value of transactions, 3rd the lowest.

# for method in ['dense']:
#     df2[f'{method}_rank'] = df2.groupby('Transaction Month')[
#         'Value'].rank(method)

df2['rank'] = df2.groupby('Transaction Month')['Value'].rank(ascending=False)

print(df2)

# Without losing all of the other data fields, find:
# The average rank a bank has across all of the months, call this field 'Avg Rank per Bank'

df = df[['Bank', 'Transaction Month', 'Transaction Code', 'Value',
        'Customer Code', 'Online or In-Person', 'Transaction Date']]
# print(df)
df['Bank'] = df['Bank'].astype(str)
df2['Bank'] = df2['Bank'].astype(str)
df3 = df.merge(df2, on='Bank', how='left')

df4 = df3.groupby(['Bank'], as_index=False)['rank'].mean()

# print(df4)

# The average transaction value per rank, call this field 'Avg Transaction Value per Rank'

df5 = df2.groupby(['rank'], as_index=False)['Value'].mean()

print(df5)

df6 = df2.merge(df5, on='rank', how='left')

print(df6)

df7 = df6.join(df4.set_index('Bank'), on='Bank', lsuffix=' avg')

# Output the data

print(df7)
print('done')
