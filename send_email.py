import smtplib
from email.message import EmailMessage
import os

def send_email(subject, body, to_email, filename):
    """
    Sends an email with the specified subject, body, and attachment to the provided email address.
    
    Parameters:
    - subject (str): The subject of the email.
    - body (str): The body content of the email.
    - to_email (str): The recipient's email address.
    - filename (str): The file to attach to the email.
    """
    
    # Replace with your email details
    from_email = "dung.ngt1988@gmail.com"
    email_password = "Maian2018@"
    
    # Create the email message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(body)
    
    # Attach the file
    with open(filename, 'rb') as file:
        file_data = file.read()
        file_name = os.path.basename(filename)
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    
    # Send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(from_email, email_password)
            smtp.send_message(msg)
        return {"status": "success", "message": f"Email sent to {to_email} with attachment {filename}."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Example usage
# result = send_email("Test Subject", "This is a test email body.", "recipient@example.com", "conversation_summary.docx")
# print(result)
