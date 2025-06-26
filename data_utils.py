
# data_utils.py
# Data loading, lookups, and utility functions

import pandas as pd
from data.occupation_data import OCCUPATION_HAZARDS, ROLE_MULTIPLIERS, COMPANY_TYPE_FACTORS
from data.education_data import EDUCATION_LEVEL_FACTORS, EDUCATION_FIELD_FACTORS, SCHOOL_TIER_FACTORS
from data.skill_data import SKILL_CATEGORIES, LEARNING_RESOURCES
from data.environmental_data import ECONOMIC_CLIMATE_SCENARIOS, AI_INNOVATION_SCENARIOS
import collections

def get_occupation_list():
    return sorted(list(OCCUPATION_HAZARDS.keys()))

def get_education_level_list():
    return sorted(list(EDUCATION_LEVEL_FACTORS.keys()))

def get_education_field_list():
    return sorted(list(EDUCATION_FIELD_FACTORS.keys()))

def get_school_tier_list():
    return sorted(list(SCHOOL_TIER_FACTORS.keys()))

def get_company_type_list():
    return sorted(list(COMPANY_TYPE_FACTORS.keys()))

def get_economic_climate_scenarios():
    return sorted(list(ECONOMIC_CLIMATE_SCENARIOS.keys()))

def get_ai_innovation_scenarios():
    return sorted(list(AI_INNOVATION_SCENARIOS.keys()))

def get_skill_types():
    return sorted(list(set(SKILL_CATEGORIES.values())))

def get_skills_by_type(skill_type: str):
    return sorted([skill for skill, s_type in SKILL_CATEGORIES.items() if s_type == skill_type])

def get_learning_resources(skill_type: str = None, skills: list = None) -> pd.DataFrame:
    df = LEARNING_RESOURCES.copy()
    if skill_type:
        df = df[df['Type'] == skill_type]
    if skills:
        df = df[df.index.isin(skills)]
    return df

def get_high_impact_skills_for_occupation(occupation: str):
    # This is a simplified function. In a real app, this would be more sophisticated,
    # potentially linking job descriptions to skill taxonomies.
    # For now, let's suggest general skills that are broadly useful for most roles
    # and maybe a couple of 'firm-specific' concepts related to the occupation.
    general_skills = [
        "Python Programming", "Data Analysis (SQL, Pandas)", "Machine Learning Concepts",
        "Cloud Computing (AWS/Azure/GCP)", "Project Management", "Communication Skills",
        "Critical Thinking", "Generative AI Tools (e.g., ChatGPT, Midjourney)",
        "Ethical AI Principles", "Cybersecurity Best Practices", "Agile Methodologies"
    ]
    firm_specific_skills = []

    if "Accountant" in occupation:
        firm_specific_skills.append("Company-specific Financial Modeling")
    elif "HR Specialist" in occupation:
        firm_specific_skills.append("Internal HR System (Workday)")
    elif "Sales" in occupation:
        firm_specific_skills.append("Proprietary CRM Software (Salesforce)")
    elif "Engineer" in occupation or "Scientist" in occupation:
        firm_specific_skills.append("Legacy System Maintenance") # Placeholder for specific tech debt
        firm_specific_skills.append("Niche Industry Regulations") # Could apply to many
    elif "Designer" in occupation:
        firm_specific_skills.append("Brand-specific Marketing Strategy") # as designers often work on branding

    # Filter to only include skills that actually exist in SKILL_CATEGORIES
    general_skills = [s for s in general_skills if SKILL_CATEGORIES.get(s) == "general"]
    firm_specific_skills = [s for s in firm_specific_skills if SKILL_CATEGORIES.get(s) == "firm-specific"]


    return {
        "general": general_skills,
        "firm_specific": firm_specific_skills
    }

def get_all_skills():
    return sorted(list(SKILL_CATEGORIES.keys()))

