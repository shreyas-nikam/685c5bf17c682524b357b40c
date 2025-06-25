
# data/education_data.py

EDUCATION_LEVEL_FACTORS = {
    "PhD": 0.85,
    "Master's": 0.90,
    "Bachelor's": 1.00,
    "Associate's": 1.10,
    "High School": 1.20,
}

EDUCATION_FIELD_FACTORS = {
    "Tech/Engineering/Quantitative Science": 0.90,
    "Business/Finance": 1.00,
    "Healthcare/Medicine": 0.95,
    "Social Sciences/Humanities": 1.10,
    "Arts/Design": 1.15,
    "Education": 1.05,
    "Law": 1.05,
    "Trades/Vocational": 1.10,
    "Other": 1.00,
}

SCHOOL_TIER_FACTORS = {
    "Tier 1 (Top 100 Global)": 0.90,
    "Tier 2 (Top 500 Global)": 0.95,
    "Tier 3 (Reputable National)": 1.00,
    "Tier 4 (Regional/Local)": 1.05,
    "Tier 5 (Online/Other)": 1.10,
}
