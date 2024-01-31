# Compliance News Scraper

Automated Python script for scraping weekly compliance news related to any AML, KYC, and CFT news in Australia from reputable sources, such as AUSTRAC, ASIC, APRA, CCMC, ACAMS, and AFR. The script sends a summary of the news directly to your email address every Monday at 9:00 AM.

## Prerequisites

Before using the script, make sure you have Python installed. You can install the required libraries using the following command:

```bash
pip install requests beautifulsoup4 schedule
```

## Configuration

1. **Email Setup:**
   - Replace `'test@gmail.com'` with your email address.
   - Replace `'email_password'` with your email password.
   - Note: Consider using environment variables or a more secure method for handling credentials in a production environment.

2. **Email Recipient:**
   - Change the `'test@gmail.com'` email address to your private Gmail address.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/compliance-news-scraper.git
cd compliance-news-scraper
```

2. Run the script:

```bash
python compliance_news_scraper.py
```

3. The script will execute every Monday at 9:00 AM (Melbourne, Australia time) and send an email with the latest AUSTRAC, ASIC, APRA, CCMC, ACAMS, and AFR compliance news.

## Disclaimer

This script is provided as a sample and should be used responsibly. Ensure compliance with the terms of use of the respective websites and consider security implications, especially when handling credentials.
Similarly, if there is any further feedback to improve this script, please feel free to let me know.
