import pandas as pd

# Input data
data = """USERNAME EMAIL@EMAIL.com;
USERNAME EMAIL@EMAIL.com;
USERNAME EMAIL@EMAIL.com;
USERNAME EMAIL@EMAIL.com;
USERNAME EMAIL@EMAIL.com;
"""

# Splitting the data into individual entries
entries = data.split(';')

# Preparing the data for the DataFrame
names = [] # Creates list named names - empty
emails = [] # Creates list named emails - empty
for entry in entries: # Loop through each entry in entries
    entry = entry.strip() # Remove leading and trailing whitespaces
    if entry: # If entry is not empty
        parts = entry.rsplit(' ', 1)  # Split into name and email
        name, email = parts[0], parts[1] # Assign name and email to parts
        names.append(name) # Append name to names list
        emails.append(email) # Append email to emails list

# Creating a DataFrame
df = pd.DataFrame({ # Create a DataFrame
    'Name': names, # Column Name with names
    'Email': emails # Column Email with emails
})

# Exporting the DataFrame to an Excel file
df.to_excel('names_and_emails.xlsx', index=False)
