
# data/education_data.py

EDUCATION_LEVEL_FACTORS = {
    "PhD": 0.85,
    "Master's": 0.90,
    "Bachelor's": 1.00,
    "Associate's": 1.05,
    "High School": 1.10,
}

EDUCATION_FIELD_FACTORS = {
    "Tech/Engineering/Quantitative Science": 0.90,
    "Healthcare/Medicine": 0.95,
    "Business/Finance": 1.00,
    "Social Sciences": 1.05,
    "Liberal Arts/Humanities": 1.10,
    "Creative Arts/Design": 1.00,
    "Trades/Vocational": 1.05,
}

SCHOOL_TIER_FACTORS = {
    "Tier 1 (Top Universities)": 0.95,
    "Tier 2 (Reputable Institutions)": 1.00,
    "Tier 3 (Other Institutions)": 1.05,
}
