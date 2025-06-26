
# data/occupation_data.py

OCCUPATION_HAZARDS = {
    "Data Scientist": 35,
    "Software Engineer": 40,
    "Financial Analyst": 55,
    "Marketing Specialist": 60,
    "Customer Service Representative": 75,
    "HR Manager": 50,
    "Graphic Designer": 45,
    "Paralegal": 65,
    "Senior Research Scientist": 30,
    "Accountant": 50,
    "Nurse": 20,
    "Teacher": 25,
    "Manufacturing Worker": 70,
    "Truck Driver": 60,
    "Retail Sales Associate": 80,
    "Construction Manager": 30,
    "Architect": 35,
    "Librarian": 60,
    "Journalist": 55,
    "Chef": 40,
}

ROLE_MULTIPLIERS = {
    "Data Scientist": 0.8,
    "Software Engineer": 0.85,
    "Financial Analyst": 1.0,
    "Marketing Specialist": 1.05,
    "Customer Service Representative": 1.3,
    "HR Manager": 0.95,
    "Graphic Designer": 0.9,
    "Paralegal": 1.35,
    "Senior Research Scientist": 0.3,
    "Accountant": 1.0,
    "Nurse": 0.7,
    "Teacher": 0.75,
    "Manufacturing Worker": 1.2,
    "Truck Driver": 1.15,
    "Retail Sales Associate": 1.4,
    "Construction Manager": 0.7,
    "Architect": 0.8,
    "Librarian": 1.1,
    "Journalist": 1.05,
    "Chef": 0.85,
}

COMPANY_TYPE_FACTORS = {
    "Big Firm (e.g., Fortune 500)": 0.95,
    "Mid-size Firm (e.g., 500-5000 employees)": 1.00,
    "Startup (e.g., <500 employees)": 1.15,
    "Government/Non-Profit": 0.85,
}
