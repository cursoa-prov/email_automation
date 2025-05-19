# filepath: student-grades-emailer/src/main.py
from grades_reader import read_grades
from contacts_reader import read_contacts
from emailer import Emailer
from utils import format_email_content

def main():
    grades_file = 'path/to/grades.xlsx'  # Update with actual path
    contacts_file = 'path/to/contacts.xlsx'  # Update with actual path

    grades = read_grades(grades_file)
    contacts = read_contacts(contacts_file)

    emailer = Emailer()

    for contact in contacts:
        student_name = contact['name']  # Assuming contact has a 'name' field
        student_grade = grades.get(student_name, 'Grade not found')
        subject = f"Your Grade for the Course"
        body = format_email_content(student_name, student_grade)
        emailer.send_email(contact['email'], subject, body)

if __name__ == "__main__":
    main() 