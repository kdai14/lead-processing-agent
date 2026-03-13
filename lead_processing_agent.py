from enum import Enum
from dataclasses import dataclass
import sqlite3
import random
from datetime import datetime, timedelta

class LeadQuality(Enum):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'

@dataclass
class Lead:
    name: str
    email: str
    phone: str
    score: int = 0
    quality: LeadQuality = LeadQuality.LOW

class LeadDatabase:
    def __init__(self, db_name='leads.db'):
        self.connection = sqlite3.connect(db_name)
        self.create_table()
    
    def create_table(self):
        with self.connection:
            self.connection.execute('''CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                phone TEXT,
                score INTEGER,
                quality TEXT
            )''')

    def insert_lead(self, lead: Lead):
        with self.connection:
            self.connection.execute('INSERT INTO leads (name, email, phone, score, quality) VALUES (?, ?, ?, ?, ?)', 
                                    (lead.name, lead.email, lead.phone, lead.score, lead.quality.value))

    def fetch_leads(self):
        with self.connection:
            return self.connection.execute('SELECT * FROM leads').fetchall()

class LeadProcessingAgent:
    def __init__(self, database: LeadDatabase):
        self.database = database

    def process_leads(self, leads: list):
        for lead in leads:
            self.analyze_lead_risk(lead)
            self.database.insert_lead(lead)

    def analyze_lead_risk(self, lead: Lead):
        # Simple scoring logic
        lead.score = random.randint(1, 100)
        if lead.score > 75:
            lead.quality = LeadQuality.HIGH
        elif lead.score > 50:
            lead.quality = LeadQuality.MEDIUM
        else:
            lead.quality = LeadQuality.LOW

    def generate_engagement_message(self, lead: Lead):
        return f"Hello {lead.name}, we have some great offers for you!"

    def schedule_follow_up(self, lead: Lead, days: int):
        follow_up_date = datetime.now() + timedelta(days=days)
        return follow_up_date.strftime('%Y-%m-%d')

    def batch_process(self, leads: list):
        self.process_leads(leads)

    def daily_follow_ups(self):
        # This would be an actual implementation for scheduling follow-ups
        return "Follow-ups scheduled!"

    def interactive_chat(self, lead: Lead):
        return f"Chat initiated for {lead.name}"

def demo_agent():
    leads = [
        Lead(name="John Doe", email="john@example.com", phone="123-456-7890"),
        Lead(name="Jane Smith", email="jane@example.com", phone="098-765-4321"),
        Lead(name="Alice Johnson", email="alice@example.com", phone="555-000-1111")
    ]
    agent = LeadProcessingAgent(LeadDatabase())
    agent.batch_process(leads)
    for lead in leads:
        print(agent.generate_engagement_message(lead))

if __name__ == '__main__':
    demo_agent()