
# data/occupation_data.py
# Synthetic data for occupations, roles, companies

OCCUPATION_HAZARDS = {
    "Administrative Assistant": 70,
    "Paralegal": 65,
    "Accountant": 60,
    "Data Entry Clerk": 75,
    "Customer Service Representative": 68,
    "Truck Driver": 55,
    "Retail Sales Associate": 58,
    "Financial Analyst": 45,
    "Software Engineer": 40,
    "UX/UI Designer": 38,
    "Marketing Manager": 42,
    "HR Specialist": 50,
    "Senior Research Scientist": 30,
    "Machine Learning Engineer": 25,
    "Data Scientist": 35,
    "Physician": 10,
    "Teacher": 20,
    "Construction Manager": 48,
    "Graphic Designer": 52,
    "Cybersecurity Analyst": 32,
    "AI Ethicist": 15
}

ROLE_MULTIPLIERS = {
    "Administrative Assistant": 1.35,
    "Paralegal": 1.30,
    "Accountant": 1.25,
    "Data Entry Clerk": 1.40,
    "Customer Service Representative": 1.32,
    "Truck Driver": 1.20,
    "Retail Sales Associate": 1.22,
    "Financial Analyst": 1.00,
    "Software Engineer": 0.90,
    "UX/UI Designer": 0.92,
    "Marketing Manager": 0.95,
    "HR Specialist": 1.05,
    "Senior Research Scientist": 0.80,
    "Machine Learning Engineer": 0.70,
    "Data Scientist": 0.85,
    "Physician": 0.60,
    "Teacher": 0.75,
    "Construction Manager": 1.10,
    "Graphic Designer": 1.15,
    "Cybersecurity Analyst": 0.88,
    "AI Ethicist": 0.65
}

COMPANY_TYPE_FACTORS = {
    "Big Firm (Stable)": {"sentiment": 0.95, "financial": 0.90, "growth": 0.90},
    "Mid-size Firm (Growth)": {"sentiment": 1.00, "financial": 1.00, "growth": 1.05},
    "Startup (High Risk/Reward)": {"sentiment": 1.10, "financial": 1.15, "growth": 1.20},
    "Government/Non-Profit": {"sentiment": 0.85, "financial": 0.80, "growth": 0.85}
}
