
# Synthetic data for education levels, fields, and schools

EDUCATION_LEVEL_FACTORS = {
    "PhD": 0.85,
    "Master's": 0.90,
    "Bachelor's": 1.00,
    "Associate's": 1.10,
    "High School": 1.20,
}

EDUCATION_FIELD_FACTORS = {
    "Tech/Engineering/Quantitative Science": 0.90,
    "Business/Finance": 0.95,
    "Healthcare": 0.88,
    "Liberal Arts/Humanities": 1.10,
    "Education": 1.05,
    "Marketing/Communications": 1.00,
}

SCHOOL_TIER_FACTORS = {
    "Tier 1 (Ivy League, Top Research Uni)": 0.95,
    "Tier 2 (Reputable State Uni, Good Private)": 1.00,
    "Tier 3 (Community College, Vocational)": 1.05,
}
