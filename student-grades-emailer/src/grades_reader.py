def read_grades(file_path):
    import pandas as pd

    # Read the Excel file
    df = pd.read_excel(file_path)

    # Assuming the Excel file has columns 'Student Name' and 'Grade'
    grades = df[['Student Name', 'Grade']].to_dict(orient='records')

    return grades