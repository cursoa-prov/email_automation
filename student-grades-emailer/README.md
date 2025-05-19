# Student Grades Emailer

This project automates the process of sending student grades via email. It reads student grades and email contacts from Excel spreadsheets and sends the grades to the respective students.

## Project Structure

```
student-grades-emailer
├── src
│   ├── main.py          # Entry point of the application
│   ├── emailer.py       # Contains the Emailer class for sending emails
│   ├── grades_reader.py  # Reads student grades from Excel
│   ├── contacts_reader.py # Reads email contacts from Excel
│   └── utils.py         # Utility functions for the project
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd student-grades-emailer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Prepare your Excel files:
   - Create an Excel file for student grades with appropriate columns (e.g., Student Name, Grade).
   - Create another Excel file for email contacts with a column for email addresses.

2. Update the file paths in `src/main.py` to point to your Excel files.

3. Run the application:
   ```
   python src/main.py
   ```

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.