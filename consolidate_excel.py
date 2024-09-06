import pandas as pd

# File paths
excel_a_path = 'EXCEL_A.xlsx'
excel_b_path = 'EXCEL_B.xlsx'

# Load EXCEL_A
excel_a = pd.ExcelFile(excel_a_path)
if 'Sheet1' in excel_a.sheet_names:
    df_a = pd.read_excel(excel_a_path, sheet_name='Sheet1')
else:
    df_a = pd.DataFrame(columns=['du_id', 'supply_period', 'gcb_id', 'kwh_purchased', 'average_gen_cost'])

# Load all sheets from EXCEL_B
excel_b = pd.ExcelFile(excel_b_path)
all_sheets_data = []

for sheet_name in excel_b.sheet_names:
    df_b = pd.read_excel(excel_b_path, sheet_name=sheet_name)
    all_sheets_data.append(df_b)

# Combine all sheets into a single DataFrame
df_combined = pd.concat(all_sheets_data, ignore_index=True)

# Append combined data to EXCEL_A
df_a = pd.concat([df_a, df_combined], ignore_index=True)

# Save the updated DataFrame back to EXCEL_A
df_a.to_excel(excel_a_path, sheet_name='Sheet1', index=False)
