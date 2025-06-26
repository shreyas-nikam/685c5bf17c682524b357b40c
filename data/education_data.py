
# data/education_data.py
# Synthetic data for education levels, fields, schools

EDUCATION_LEVEL_FACTORS = {
    "PhD": 0.85,
    "Master's": 0.90,
    "Bachelor's": 1.00,
    "Associate's": 1.10,
    "High School": 1.20
}

EDUCATION_FIELD_FACTORS = {
    "Tech/Engineering/Quantitative Science": 0.90,
    "Business/Finance": 0.95,
    "Healthcare/Life Sciences": 0.88,
    "Education/Social Sciences": 1.05,
    "Liberal Arts/Humanities": 1.10,
    "Creative Arts/Design": 1.00
}

SCHOOL_TIER_FACTORS = {
    "Tier 1 (Top University)": 0.95,
    "Tier 2 (Reputable University)": 1.00,
    "Tier 3 (Other University/College)": 1.05,
    "N/A (No Degree)": 1.10
}
