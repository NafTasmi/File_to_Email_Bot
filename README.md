# File-to-Email Bot

A simple Python script that reads the contents of a text file and sends it as an email using Gmail's SMTP server with secure TLS encryption.

## 📁 Repository: `file-to-email-bot`

## 🚀 One-Line Summary
Reads a text file and emails its contents using Gmail's STARTTLS secure connection.

## ✨ Features
- **File Reading**: Reads content from any text file
- **Secure Email Sending**: Uses STARTTLS encryption (port 587)
- **Minimal Code**: Clean, straightforward implementation
- **Error Handling**: Comprehensive try-catch blocks
- **Gmail Integration**: Works with Gmail's SMTP service

## 📋 Prerequisites
- Python 3.x
- Gmail account with App Password enabled
- A text file named `test.txt` in the same directory

## ⚙️ Setup

### 1. Enable Gmail App Password
1. Enable **2-Factor Authentication** on your Google Account
2. Generate an **App Password**:
   - Go to: https://myaccount.google.com/apppasswords
   - Select "Mail" → Choose device → Generate
   - Copy the 16-character password

### 2. Configure Script
Edit these variables in the script:
```python
sender = "your_email@gmail.com"          # Your Gmail address
password = "your_app_password_here"      # Your 16-char App Password
receiver = "recipient@example.com"       # Recipient email
```

### 3. Prepare Your File
Create a file named `test.txt` in the same directory:
```bash
echo "This is test file content" > test.txt
```
Or create manually with any text editor.

## 🚀 Usage

### Basic Usage
```bash
python file_to_email.py
```

### File Format
The script will read `test.txt` and send its **entire content** as the email body.

### Expected Output
```
✅ Email sent using port 587!
```
OR
```
❌ Error: [error message]
```

## 🔧 How It Works

1. **File Reading**: Opens `test.txt` and reads all content
2. **Email Creation**: Creates MIME message with file content as body
3. **Secure Connection**: Establishes TLS-secured SMTP connection
4. **Authentication**: Logs into Gmail using App Password
5. **Sending**: Transmits the email with file contents

## 📊 Technical Details

| Component | Details |
|-----------|---------|
| **Port** | 587 (STARTTLS) |
| **Security** | TLS encryption |
| **SMTP Server** | smtp.gmail.com |
| **Authentication** | Gmail App Password |
| **File Encoding** | Default system encoding |

## ⚠️ Security Notes

### **IMPORTANT WARNING**
```python
# ❌ NEVER commit with real credentials:
password = "your_app_password_here  # HARDCODED PASSWORD

# ✅ SECURE Alternatives:
# 1. Environment variables
import os
password = os.getenv("GMAIL_APP_PASSWORD")

# 2. Interactive input
password = input("Enter Gmail App Password: ")

# 3. Configuration file
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
password = config['EMAIL']['password']
```

### **Before Sharing/Committing:**
1. Replace all email addresses with placeholders
2. Remove actual passwords
3. Add to `.gitignore`:
   ```
   test.txt
   config.ini
   *.env
   ```

## 🐛 Troubleshooting

### Common Issues & Solutions

| Error | Likely Cause | Solution |
|-------|-------------|----------|
| `FileNotFoundError` | `test.txt` doesn't exist | Create file in script directory |
| `SMTPAuthenticationError` | Wrong password | Use App Password, not regular password |
| `ConnectionRefusedError` | Firewall blocking | Try port 465 with SMTP_SSL |
| `SSLError` | TLS issues | Update Python/OpenSSL |
| `TimeoutError` | Network issues | Check internet connection |

### Alternative: Port 465 (SSL)
If port 587 fails, use this modification:
```python
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender, password)
    server.send_message(msg)
```

## 📝 Customization

### 1. Change File Name
```python
with open("different_file.txt", "r") as f:
    content = f.read()
```

### 2. Change Email Subject
```python
msg['Subject'] = 'Your Custom Subject Here'
```

### 3. Add HTML Formatting
```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart('alternative')
msg.attach(MIMEText(content, 'plain'))
msg.attach(MIMEText(f"<pre>{content}</pre>", 'html'))
```

## 📁 Project Structure
```
file-to-email-bot/
├── file_to_email.py    # Main script
├── test.txt           # Sample text file (ignored in git)
├── .gitignore         # Git ignore file
├── requirements.txt   # Python dependencies (none needed)
└── README.md          # This file
```

## 📈 Use Cases
- Automated log file reporting
- Sending configuration files
- Daily report distribution
- Backup notification emails
- Educational demonstrations of file I/O + email

## 🧪 Testing
1. **Test File**: Create `test.txt` with sample content
2. **Self-Test**: Send to your own email first
3. **Verify**: Check spam folder if email doesn't arrive
4. **Content**: Ensure file contains appropriate data

### Sample Test File
```txt
System Report - $(date)
----------------------
Status: Operational
Users: 42
Uptime: 99.9%
Last backup: Complete
```

## 📄 License
For educational purposes only. Users must comply with:
- Gmail's Terms of Service
- Applicable anti-spam laws
- Data privacy regulations

## 🔍 Quick Start Checklist
- [ ] Enable Google 2FA
- [ ] Generate App Password
- [ ] Update script credentials
- [ ] Create `test.txt` file
- [ ] Test with self-email
- [ ] Remove hardcoded passwords before committing

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to branch
5. Open pull request

---

**⚠️ Security Reminder**: Always use environment variables or secure credential storage in production. Never store passwords in plain text files or version control systems.
