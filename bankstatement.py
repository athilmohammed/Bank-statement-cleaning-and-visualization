import pandas as pd

# Load the file (adjust path method as needed)
df = pd.read_excel("C:/Users/athil/Desktop/Python/bankstatement.xlsx")


# Transforing the column DESCRIPTION
df['Description'] = df['Description'].str.replace('TO TRANSFER-UPI.*', 'TO UPI TRANSFER', regex = True)
df['Description'] = df['Description'].str.replace('BY TRANSFER-UPI.*', 'BY UPI TRANSFER', regex = True)
df['Description'] = df['Description'].str.replace('WITHDRAWAL TRANSFER.*', 'TO LOAN REPAYMENT', regex = True)
df['Description'] = df['Description'].str.replace('BY TRANSFER-NEFT.*', 'BY NEFT TRANSFER', regex = True)
df['Description'] = df['Description'].str.replace('TO TRANSFER-INB.*', 'TO IMPS TRANSFER', regex = True)
df['Description'] = df['Description'].str.replace('BY TRANSFER-INB.*', 'BY IMPS TRANSFER', regex = True)
df['Description'] = df['Description'].str.replace('CASH DEPOSIT.*', 'CASH DEPOSIT', regex = True)
df['Description'] = df['Description'].str.replace('CREDIT INTEREST.*', 'INTEREST CREDITED', regex = True)
df['Description'] = df['Description'].str.replace('AMC Debit Card.*', 'DEBIT-CARD AMC', regex = True)
df['Description'] = df['Description'].str.replace('ATM WDL.*', 'ATM WITHDRAWAL', regex = True)
df['Description'] = df['Description'].str.replace('by debit card.*', 'TO DEBIT CARD POS', regex = True)
df['Description'] = df['Description'].str.replace('BY TRANSFER-SBI.*', 'BY IMPS TRANSFER', regex = True)

# Transforming the column Txn Date
df['Txn Date'] = pd.to_datetime(df['Txn Date'])
df['Txn Date'] = df['Txn Date'].dt.strftime('%d-%b-%Y')


#Exporting as Excel file
df.to_excel("C:/Users/athil/Desktop/cleanedbankstatement.xlsx", index=False)