import os
import re
from datetime import datetime
from sqlalchemy.orm import Session
from models import Company, engine  # adjust the import according to your project structure
from datetime import datetime

# Initialize the DataFrame.
data = []

columns = ['Filename', 'Official Name', 'GEMH Number', 'Website', 'Date of Registration']



# Get current working directory
cwd = os.getcwd()

# Define the directory
directory = "app/text_files"

# Build the full path
directory = os.path.join(cwd, directory)


# Define regular expressions for extracting information.
gemh_pattern = re.compile(r'(?i)Γ\.?Ε\.?ΜΗ\.?[:\s]*([\d_]+)')
name_pattern = re.compile(r'(?:επωνυμία|ΕΠΩΝΥΜΙΑ)[:\s]*«?([Α-Ω΢A-Z0-9\s\.-]+)»?')
website_pattern = re.compile(r'(?:ιστοσελίδας|ιςτοςελίδασ|Ιστοσελίδα:)[:\s]*((?:https?://)?[\w/\-?=%.]+\.[\w/\-?=%.]+)')
date_pattern = re.compile(r'Αθήνα, (\d{2}-\d{2}-\d{4})')
def parse_date(input_string):
    date_string, _, _ = input_string.partition('_')
    
    if date_string.lower() == 'null':
        return None
    
    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError as e:
        return datetime.strptime(date_string, "%d-%m-%Y").date()

# Loop over all files in the directory.
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        filepath = os.path.join(directory, filename)
        
        # Extract the date from the filename.
        try:
            date = filename.split('kataxorisi istoselidas_')[1].split('.')[0].split(' ')[0]
            date = parse_date(date)
        except IndexError:
            date = None  # Handle cases where the date is not present in the filename.
           
        
        # Open each file and read the content.
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

            # Search for the patterns in the content.
            gemh_match = gemh_pattern.search(content)
            name_match = name_pattern.search(content)
            website_match = website_pattern.search(content)

            if date == None:
                date_match = date_pattern.search(content)
                if date_match:
                    date = date_match.group(1)  # Extract date from file content.
                    date = parse_date(date)
            # Extract the matched information.
            gemh = gemh_match.group(1) if gemh_match else None
            name = name_match.group(1) if name_match else None
            if name_match:
                name = re.sub(r'\n', '', name_match.group(1).strip())  # Removing \n and stripping leading and trailing whitespaces.
                name = re.sub(r'ΔΙΑΚΡΙΤΙΚΟΣ ΤΙΤΛΟΣ', '', name)  # Remove the unwanted string.
                name = name.strip()  # Remove any leading/trailing whitespace that may have been left.
            website = website_match.group(1) if website_match else None
            # Append the extracted information to the data list.
            data.append({
                'Filename': filename,
                'Official Name': name,
                'GEMH Number': gemh,
                'Website': website,
                'Date of Registration': date
            })

# Start the session.
session = Session(bind=engine)

for item in data:
   

    
   # Check if a company with the same gemh_number already exists
    existing_company = session.query(Company).filter_by(gemh_number=item['GEMH Number']).first()
    
    if existing_company is None:
        # If no duplicate is found, add the new company
        company = Company(
            name=item['Official Name'],
            gemh_number=item['GEMH Number'],
            website=item['Website'],
            registration_date=item['Date of Registration']
        )
        session.add(company)
    else:
        # Optionally, if the company exists, update the existing entry
        existing_company.name = item['Official Name']
        existing_company.website = item['Website']
        existing_company.registration_date = item['Date of Registration']

    # Commit the changes to the session.
    session.commit()

# Close the session.
session.close()