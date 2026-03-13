# demo.py

# This script demonstrates the lead processing agent with sample leads

class Lead:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def display_lead(self):
        return f'Lead(Name: {self.name}, Email: {self.email}, Phone: {self.phone})'

# Sample leads
leads = [
    Lead('John Doe', 'john@example.com', '555-555-5555'),
    Lead('Jane Smith', 'jane@example.com', '555-555-1234'),
    Lead('Alice Johnson', 'alice@example.com', '555-555-9876')
]

# Interactive chat mode

for lead in leads:
    print(lead.display_lead())
    response = input('How would you like to interact with this lead? ')    
    print(f'You chose to {response} with {lead.name}.')
