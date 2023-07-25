import numpy as np
import pandas as pd
import openpyxl

# reading actual excel files required the installation of openpyxl (as in open python excel) and then using read_excel
# then to read all the sheets together, specify sheet_name = None or list all the sheets

df1 = pd.read_excel(
    'C:\\Users\\Adam\\Documents\\GitHub\\Preppin Data\\Inputs\\New Customers.xlsx', sheet_name=None)

# Union all the sheets together

df2 = pd.concat(df1, join='outer', ignore_index=True)

# df2 shows how i did it before looking at solution, my way worked as expected for a union, this data has deliberately mispelled columns names
# so mine created new columns for these, in solution below, it both creates a field for the tab name (month in this case)
# and to fix the mispelled field names it simply specifies all the columns so it just unions them on position and renames them

df3 = []
for tab_name, df in df1.items():
    df.columns = ['ID', 'Joining Day', 'Demographic', 'Value']
    df['sheet_name'] = tab_name
    df3.append(df)
    df4 = pd.concat(df3, ignore_index=True)

# Make a Joining Date field based on the Joining Day, Table Names and the year 2023

df4['month'] = pd.to_datetime(
    df4['sheet_name'], format='%B').dt.strftime('%m').astype(int)
df4['year'] = 2023
df4['day'] = df4['Joining Day']
df4['Joining Date'] = pd.to_datetime(df4[['year', 'month', 'day']])

df4 = df4.drop(['year', 'month', 'day',
               'sheet_name'], axis=1)

# Now we want to reshape our data so we have a field for each demographic, for each new customer

df5 = pd.pivot(data=df4, index=['ID', 'Joining Date'],
               columns='Demographic', values='Value').reset_index()

# Make sure all the data types are correct for each field

df5['Date of Birth'] = pd.to_datetime(df5['Date of Birth'], format='%m/%d/%Y')

# remove duplicate rows

df5 = df5.sort_values(by=['Joining Date'])

df6 = df5.drop_duplicates(
    subset=['ID', 'Account Type', 'Date of Birth', 'Ethnicity'])
print(df6)
df78 = df6.loc[df6['ID'] == 878212]
print(df78)

print('done')
