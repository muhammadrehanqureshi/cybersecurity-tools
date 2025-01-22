import re
from urllib.parse import urlparse

def detect_phishing(email_content):
    """
    Detects potential phishing attempts in an email content.
    """
    phishing_keywords = ['password', 'login', 'verify', 'bank', 'update', 'urgent', 'suspended']
    suspicious_links = []
    flags = 0

    # Check for phishing keywords
    for keyword in phishing_keywords:
        if keyword.lower() in email_content.lower():
            flags += 1
            print(f"[WARNING] Found phishing keyword: {keyword}")

    # Find and analyze URLs in the email
    urls = re.findall(r'(https?://[^\s]+)', email_content)
    for url in urls:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if "bit.ly" in domain or "tinyurl" in domain or not domain.endswith(("com", "org", "net")):
            suspicious_links.append(url)
            flags += 1
            print(f"[WARNING] Found suspicious URL: {url}")

    # Provide results
    print("\nAnalysis Results:")
    if flags > 0:
        print(f"The email is potentially a phishing attempt. ({flags} red flags found)")
        if suspicious_links:
            print("Suspicious links found:")
            for link in suspicious_links:
                print(f" - {link}")
    else:
        print("The email appears to be safe.")

# Example usage
if __name__ == "__main__":
    print("=== Phishing Email Detector ===")
    file_path = input("Enter the path to the email content file (.txt): ")
    try:
        with open(file_path, 'r') as file:
            email_content = file.read()
            detect_phishing(email_content)
    except FileNotFoundError:
        print("Error: File not found. Please check the path and try again.")
