import re


def extract_emails(text):
    # Regular expression pattern to match email addresses
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    # Using re.findall to extract all email addresses from the text
    emails = re.findall(email_pattern, text)
    return emails


def save_emails_to_file(emails, filename):
    existing_emails = set()
    try:
        # Read existing emails from file
        with open(filename, "r") as file:
            existing_emails = set(file.read().splitlines())
    except FileNotFoundError:
        pass

    # Append only new emails to the file
    with open(filename, "a") as file:
        for email in emails:
            # Exclude emails ending with "@sbu.ac.in"
            if not email.endswith("@sbu.ac.in") and email not in existing_emails:
                file.write(email + "\n")
                existing_emails.add(email)


def main():
    # Sample text containing email addresses
    text = """ Skip to main contentTurn off continuous scrolling
Accessibility help
instagram.com @gmail.com fashion shop USA
DM or valeria.shkyra@gmail.com. Shop my outfits ⬇️. www.shopltk.com/explore/valeriashkyra + 1. Press's profile picture. Press. NYFW FW24's ...

Kitty (@kittycowell) • Instagram photos and videos

iamkittycowell@gmail.com LDN.

Instagram · vibhaamitt
56.5T+ followers

google.co.in
https://books.google.co.in › books
Lakshmi Menon, ‎Aysha Afrin, ‎Akansha Choudary · 2022 · ‎ Young Adult Fiction
... us @info.betales@gmail.com. Official Website : https://thestoriesfromunic.wixsite.com/website Instagram Profile : https://www.instagram.com/betalesforteens/

 - Update location """  # Extract email addresses from the text
    extracted_emails = extract_emails(text)
    # Print the extracted email addresses
    print("Extracted email addresses:")
    for email in extracted_emails:
        print(email)

    # Save extracted emails to a file
    save_emails_to_file(extracted_emails, "extracted_emails.txt")


if __name__ == "__main__":
    main()
