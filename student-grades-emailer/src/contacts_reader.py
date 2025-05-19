def read_contacts(file_path):
    import pandas as pd
    
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Assuming the email addresses are in a column named 'Email'
    return df['Email'].tolist()