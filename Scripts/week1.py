# Preppin Data 2023w1 (some workings have been left in comments to show process)

import pandas as pd
import numpy as np

# Input the data 

df = pd.read_csv(
    'C:\\Users\\Adam\\Documents\\GitHub\\Preppin Data\\Inputs\\PD 2023 Wk 1 Input.csv')

# print(df.info())
# print(df.describe())
# print(df.dtypes)
# Split the Transaction Code to extract the letters at the start of the transaction code. These identify the bank who processes the transaction 

df['Bank'] = df['Transaction Code'].str.split('-', expand=True)[0]

# Rename the values in the Online or In-person field, Online of the 1 values and In-Person for the 2 values.

df['Location'] = np.where(df['Online or In-Person']
                          == 1, 'Online', 'In-Person')

# Change the date to be the day of the week 

df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
df['Day of the Week'] = df['Transaction Date'].dt.day_name()

# Different levels of detail are required in the outputs. You will need to sum up the values of the transactions in three ways:
# 1. Total Values of Transactions by each bank

output_1 = df.groupby('Bank', as_index=False)['Value'].sum()


# 2. Total Values by Bank, Day of the Week and Type of Transaction (Online or In-Person)

output_2 = df.groupby(['Bank', 'Day of the Week', 'Location'], as_index=False)[
    'Value'].sum()


# 3. Total Values by Bank and Customer Code

output_3 = df.groupby(['Bank', 'Customer Code'], as_index=False)[
    'Value'].sum()

print(output_1)
print(output_2)
print(output_3)

output_1.to_csv(
    'C:\\Users\\Adam\\Documents\GitHub\\Preppin Data\\Outputs\\2023w1output1', index=False)
output_2.to_csv(
    'C:\\Users\\Adam\\Documents\GitHub\\Preppin Data\\Outputs\\2023w1output2', index=False)
output_3.to_csv(
    'C:\\Users\\Adam\\Documents\GitHub\\Preppin Data\\Outputs\\2023w1output3', index=False)

print('done')
