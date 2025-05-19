def format_email_content(student_name, grades):
    """Formats the email content for sending student grades."""
    content = f"Dear {student_name},\n\nHere are your grades:\n"
    for subject, grade in grades.items():
        content += f"{subject}: {grade}\n"
    content += "\nBest regards,\nYour School"
    return content

def handle_exception(exception):
    """Handles exceptions and logs them."""
    print(f"An error occurred: {exception}")