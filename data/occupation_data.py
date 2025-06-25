
# data/occupation_data.py

OCCUPATION_HAZARDS = {
    "Software Engineer": 40,
    "Data Scientist": 35,
    "DevOps Engineer": 30,
    "AI/ML Engineer": 25,
    "Cybersecurity Analyst": 30,
    "Financial Analyst": 60,
    "Accountant": 70,
    "Customer Service Representative": 80,
    "Truck Driver": 75,
    "Retail Sales Associate": 85,
    "Human Resources Manager": 50,
    "Marketing Specialist": 55,
    "Physician": 10,
    "Teacher": 20,
    "Graphic Designer": 45,
    "Paralegal": 65,
    "Journalist": 50,
    "Manufacturing Worker": 70,
    "Construction Manager": 30,
    "Civil Engineer": 25,
}

ROLE_MULTIPLIERS = {
    "Individual Contributor": 1.0,
    "Team Lead": 0.95,
    "Manager": 0.90,
    "Director": 0.85,
    "VP/Executive": 0.80,
    # Specific role vulnerabilities
    "Paralegal": 1.35, # Higher inherent vulnerability
    "Senior Research Scientist": 0.3, # Lower inherent vulnerability
    "Customer Service Representative": 1.5,
    "Accountant": 1.2,
}

COMPANY_TYPE_FACTORS = {
    "Startup": 1.15,
    "Mid-size Firm": 1.00,
    "Big Firm": 0.95,
    "Government/Non-profit": 0.85,
}
