
# data/education_data.py

EDUCATION_LEVEL_FACTORS = {
    "No Degree": 1.20,
    "High School": 1.15,
    "Associate's Degree": 1.10,
    "Bachelor's Degree": 1.00,
    "Master's Degree": 0.90,
    "PhD": 0.85,
}

EDUCATION_FIELD_FACTORS = {
    "STEM (Science, Tech, Engineering, Math)": 0.90,
    "Business/Finance": 0.95,
    "Healthcare": 0.88,
    "Arts/Humanities": 1.10,
    "Social Sciences": 1.05,
    "Law": 1.00,
    "Education": 0.98,
}

SCHOOL_TIER_FACTORS = {
    "Tier 1 (Top University)": 0.90,
    "Tier 2 (Reputable University)": 0.95,
    "Tier 3 (Standard University/College)": 1.00,
    "Tier 4 (Vocational/Other)": 1.05,
}
