
# Synthetic data for occupations, roles, and companies

OCCUPATION_HAZARDS = {
    "Paralegal": 65,
    "Senior Research Scientist": 30,
    "Software Engineer": 40,
    "Data Scientist": 35,
    "Financial Analyst": 50,
    "Marketing Specialist": 55,
    "HR Manager": 60,
    "Operations Manager": 45,
    "Accountant": 70,
    "Customer Service Representative": 80,
    "Nurse": 20,
    "Teacher": 25,
    "Graphic Designer": 50,
    "Project Manager": 40,
    "Sales Representative": 55,
}

ROLE_MULTIPLIERS = {
    "Paralegal": 1.35,
    "Senior Research Scientist": 0.3,
    "Software Engineer": 0.4,
    "Data Scientist": 0.35,
    "Financial Analyst": 0.5,
    "Marketing Specialist": 0.55,
    "HR Manager": 0.6,
    "Operations Manager": 0.45,
    "Accountant": 0.7,
    "Customer Service Representative": 0.8,
    "Nurse": 0.2,
    "Teacher": 0.25,
    "Graphic Designer": 0.5,
    "Project Manager": 0.4,
    "Sales Representative": 0.55,
}

COMPANY_TYPE_FACTORS = {
    "Big Firm": {"sentiment": 0.95, "financial": 0.9, "growth": 0.85},
    "Mid-size Firm": {"sentiment": 1.00, "financial": 1.0, "growth": 1.0},
    "Startup": {"sentiment": 1.10, "financial": 1.1, "growth": 1.15},
}
