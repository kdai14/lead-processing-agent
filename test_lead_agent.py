import pytest

# Assuming LeadAgent is the class responsible for processing leads
from lead_processing_agent import LeadAgent

# Sample test data for leads
sample_leads = [
    {'name': 'John Doe', 'email': 'john.doe@example.com', 'status': 'new'},
    {'name': 'Jane Smith', 'email': 'jane.smith@example.com', 'status': 'contacted'},
]

# Test for initialization of LeadAgent

def test_lead_agent_initialization():
    agent = LeadAgent(sample_leads)
    assert agent.leads == sample_leads, "Leads not initialized correctly."

# Test for processing leads

def test_process_leads():
    agent = LeadAgent(sample_leads)
    agent.process_leads()  # Assuming this method processes the leads
    for lead in agent.leads:
        assert lead['status'] in ['new', 'contacted', 'qualified', 'unqualified'], "Lead status not updated correctly."

# Test for a specific lead processing

def test_specific_lead_processing():
    lead = {'name': 'Alice Johnson', 'email': 'alice.johnson@example.com', 'status': 'new'}
    agent = LeadAgent([lead])
    agent.process_leads()  # Process the lead
    assert lead['status'] == 'qualified', "Lead status should be 'qualified' after processing."

# Test for invalid lead input

def test_invalid_lead():
    invalid_lead = {'name': '', 'email': 'invalid.email', 'status': 'new'}
    agent = LeadAgent([invalid_lead])
    with pytest.raises(ValueError) as excinfo:
        agent.process_leads()  # Process the invalid lead
    assert "Invalid lead data!" in str(excinfo.value), "Should raise ValueError for invalid lead."

if __name__ == "__main__":
    pytest.main()