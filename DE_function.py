import pandas as pd
import numpy as np
import os


current_directory = os.path.dirname(os.path.realpath(__file__))
 
files_in_directory = os.listdir(current_directory)
# Get the names of all sheets in the Excel file
files = [file for file in files_in_directory if file.endswith('.xlsx') or file.endswith('.xls')]
print (files)

# Get the latest file
if (len(files) != 1):
    latest_file = max(files, key=os.path.getctime)
else:
    latest_file = files[0]
print(latest_file)
# Specify the sheet names you want to select
selected_sheet_names = 'Recipient chars - over time'
# Read the Excel file and store each sheet in a dictionary

summary_df = pd.read_excel(os.path.join(current_directory, latest_file), sheet_name=selected_sheet_names)



# Assume the second table starts at row 0 and ends at row 10, and the second table starts at row 12
first_table = summary_df.iloc[0:26]
second_table = summary_df.iloc[28:]

# Now you have two separate dataframes for the two tables


def process_and_melt_table(table, recipient_characteristic):
    # Process the table
    table_transpose = table.transpose()
    table_transpose.reset_index(drop=True, inplace=True)
    table_transpose = table_transpose.drop(table_transpose.columns[0], axis=1)
    table_transpose = table_transpose.drop(table_transpose.index[0])
    table_transpose = table_transpose.drop(table_transpose.columns[0], axis=1)
    table_transpose.columns = table_transpose.iloc[0]
    table_transpose = table_transpose.drop(table_transpose.index[0])
    table_transpose.columns = table_transpose.columns.to_series().replace(np.nan, pd.NA).ffill()

    # Get the values of the second row
    second_row_values = table_transpose.iloc[0]

    # Create a boolean mask where True indicates NaN values in the second row
    mask = second_row_values.isna()

    # Replace column names with second row values, but keep original names where mask is True
    table_transpose.columns = np.where(mask, table_transpose.columns, second_row_values)

    # Now the column names are replaced with second row values, except where the second row had NaN
    table_transpose = table_transpose.drop(table_transpose.index[0])

    # Rename the first column to 'Date'
    table_transpose.rename(columns={table_transpose.columns[0]: 'Date'}, inplace=True)

    # Melt the table
    df_final = pd.DataFrame()
    categories = {
        "Gender": ['Male', 'Female', 'Gender Diverse'],
        "Receipt of additional support": ['Accommodation Supplement', 'Disability Allowance', 'Temporary Additional Support/Special Benefit'],
        "Age Group": ['Under 60 years', '60-64 years', '65-69 years', '70-74 years', '75-79 years', '80-84 years', '85-89 years', '90 years and over'],
        "Ethinicity": ['European', 'Māori', 'Pacific Peoples', 'Asian', 'Middle Eastern/Latin American/African', 'Other ethnicity', 'Ethnicity not specified']
    }
    for category, col_melt in categories.items():
        df_melted = table_transpose.melt(id_vars="Date", value_vars=col_melt, var_name='Subtype', value_name='Observation')
        df_melted["Type"] = category
        df_melted["Recipient Characteristic"] = recipient_characteristic
        df_final = pd.concat([df_final, df_melted])

    return df_final

first_table_processed = process_and_melt_table(first_table, "New Zealand Superannuation")
second_table_processed = process_and_melt_table(second_table, "Veteran's Pension")




df_final = pd.concat([first_table_processed, second_table_processed])

# Specify the new column order
new_column_order = ['Date', 'Recipient Characteristic', 'Type', 'Subtype', 'Observation']

# Reorder the columns
df_final = df_final.reindex(columns=new_column_order)

df_final = df_final.fillna("0")

df_final.to_csv(r'D:\\OneDrive - University of Canterbury\\1-2024\Data Engineering\DE individual assignmnet\\de_clean_data.csv', index=False)




