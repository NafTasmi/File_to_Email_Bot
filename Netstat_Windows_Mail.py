import smtplib
from email.mime.text import MIMEText

sender = "nafisatasmiya@gmail.com"
password = "ilrh rtxm wpvm qwsf"
receiver = "tasmiyanafisa12@gmail.com"

try:
    # Read file
    with open("test.txt", "r") as f:
        content = f.read()
    
    # Create email
    msg = MIMEText(content)
    msg['Subject'] = 'test.txt file'
    msg['From'] = sender
    msg['To'] = receiver
    
    # Send using STARTTLS on port 587
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Upgrade connection to secure
        server.login(sender, password)
        server.send_message(msg)
    
    print("✅ Email sent using port 587!")
    
except Exception as e:
    print(f"❌ Error: {e}")