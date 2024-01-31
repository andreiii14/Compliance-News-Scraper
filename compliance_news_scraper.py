import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time
from datetime import datetime
import pytz

def get_australian_compliance_news():
    # List of websites for compliance news
    websites = [
        'https://www.austrac.gov.au/',
        'https://asic.gov.au/',
        'https://www.apra.gov.au/',
        'https://www.ccmc.org.au/',
        'https://www.acams.org/australia/',
        'https://www.afr.com/business/banking-and-finance'
    ]

    # Initialize an empty list to store news headlines
    news_headlines = []

    # Iterate through the list of websites
    for url in websites:
        # Send a request to the website and get the HTML content
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant information (e.g., headlines or summaries)
        news_headlines.extend([headline.text.strip() for headline in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])])

    return news_headlines

def send_email(subject, body, to_email):
    # Email configuration for any email provider
    smtp_server = 'your_smtp_server' # Replace with your email provider (gmail, outlook, etc)
    smtp_port = 587
    smtp_username = 'your_email@example.com'  # Replace with your email address
    smtp_password = 'email_password'  # Replace with your email password

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body of the email
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, msg.as_string())

def job():
    # Get current time in Melbourne timezone
    melbourne_tz = pytz.timezone('Australia/Melbourne')
    melbourne_time = datetime.now(melbourne_tz)

    # Check if it's Monday at 9:00 AM in Melbourne time
    if melbourne_time.weekday() == 0 and melbourne_time.hour == 9 and melbourne_time.minute == 0:
        # Get Australian compliance news headlines
        australian_compliance_news = get_australian_compliance_news()

        # Check if there are any new headlines
        if australian_compliance_news:
            # Prepare email content
            email_subject = "Weekly Australian Compliance News Update"
            email_body = "\n".join(australian_compliance_news)

            try:
                # Send email to the private email address
                send_email(email_subject, email_body, 'your_email@example.com')
                print("Email sent with the latest Australian compliance news.")
            except Exception as e:
                print(f"Error sending email: {e}")
        else:
            print("No new Australian compliance news at the moment.")

# Schedule the job to run every Monday at 9:00 AM in Melbourne time
schedule.every().monday.at("09:00").do(job)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
