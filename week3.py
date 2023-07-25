import numpy as np
import pandas as pd


df = pd.read_csv(
    'C:\\Users\\Adam\\Documents\\GitHub\\Embedding-tutorial\\Preppin Data\\Inputs\\PD 2023 Wk 1 Input.csv')
df2 = pd.read_csv(
    'C:\\Users\\Adam\\Documents\\GitHub\\Embedding-tutorial\\Preppin Data\\Inputs\\Targets.csv')
# print(df)
# print(df2)

# For the transactions file:
# Filter the transactions to just look at DSB (help)

df['Transaction_Code'] = df['Transaction Code'].str.split('-', expand=True)[0]
# df['Transaction Code'] = np.where(df['Transaction Code']
#                                   == 'DSB')
df.query("Transaction_Code == 'DSB'", inplace=True)

# These will be transactions that contain DSB in the Transaction Code field
# Rename the values in the Online or In-person field, Online of the 1 values and In-Person for the 2 values

df['Online or In-Person'] = np.where(df['Online or In-Person']
                                     == 1, 'Online', 'In-Person')

# Change the date to be the quarter (help)

df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
# df['Quarter'] = pd.PeriodIndex(df['Transaction Date'], freq='Q')
df['Quarter'] = df['Transaction Date'].dt.quarter

# Sum the transaction values for each quarter and for each Type of Transaction (Online or In-Person) (help)

df3 = df.groupby(['Online or In-Person', 'Quarter'],
                 as_index=False)['Value'].sum()


# For the targets file:
# Pivot the quarterly targets so we have a row for each Type of Transaction and each Quarter (help)

df4 = pd.wide_to_long(df2, stubnames='Q', i=[
                      'Online or In-Person'], j='Quarter')
# Rename the fields
# Remove the 'Q' from the quarter field and make the data type numeric (help)

df4 = df4.rename({'Q': 'Value'}, axis=1)

# Join the two datasets together (help)


df5 = df4.merge(df3, how='inner', on='Online or In-Person')
# df5 = df5.rename({'Value_x': 'Target Value',
#                 'Value_y': 'Value'}, axis=1, inplace=True)
# df6 = df5.groupby(['Quarter', 'Online or In-Person'],
#                  as_index=False)['Value'].sum()

print(df)
print(df3)
print(df4)
print(df5)
# print(df6)

# You may need more than one join clause!

# df6 = df5.join(df2.set_index('Bank'), on='Bank')

print('done')


# Remove unnecessary fields
# Calculate the Variance to Target for each row (help)
