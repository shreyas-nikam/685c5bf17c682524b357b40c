
# data_utils.py
import pandas as pd
import numpy as np

from data.occupation_data import OCCUPATION_HAZARDS, ROLE_MULTIPLIERS, COMPANY_TYPE_FACTORS
from data.education_data import EDUCATION_LEVEL_FACTORS, EDUCATION_FIELD_FACTORS, SCHOOL_TIER_FACTORS
from data.skill_data import SKILL_CATEGORIES, LEARNING_RESOURCES, OCCUPATION_RECOMMENDED_SKILLS
from data.environmental_data import ECONOMIC_CLIMATE_SCENARIOS, AI_INNOVATION_SCENARIOS

def get_occupation_hazards():
    return OCCUPATION_HAZARDS

def get_role_multipliers():
    return ROLE_MULTIPLIERS

def get_company_type_factors():
    return COMPANY_TYPE_FACTORS

def get_education_level_factors():
    return EDUCATION_LEVEL_FACTORS

def get_education_field_factors():
    return EDUCATION_FIELD_FACTORS

def get_school_tier_factors():
    return SCHOOL_TIER_FACTORS

def get_skill_categories():
    return SKILL_CATEGORIES

def get_learning_resources():
    return LEARNING_RESOURCES

def get_occupation_recommended_skills():
    return OCCUPATION_RECOMMENDED_SKILLS

def get_economic_climate_scenarios():
    return ECONOMIC_CLIMATE_SCENARIOS

def get_ai_innovation_scenarios():
    return AI_INNOVATION_SCENARIOS

def get_all_occupations():
    return sorted(list(OCCUPATION_HAZARDS.keys()))

def get_all_education_levels():
    return sorted(list(EDUCATION_LEVEL_FACTORS.keys()))

def get_all_education_fields():
    return sorted(list(EDUCATION_FIELD_FACTORS.keys()))

def get_all_school_tiers():
    return sorted(list(SCHOOL_TIER_FACTORS.keys()))

def get_all_company_types():
    return sorted(list(COMPANY_TYPE_FACTORS.keys()))

def get_all_economic_scenarios():
    return sorted(list(ECONOMIC_CLIMATE_SCENARIOS.keys()))

def get_all_ai_scenarios():
    return sorted(list(AI_INNOVATION_SCENARIOS.keys()))

def get_fcr_value(company_type: str) -> float:
    """
    Retrieves the Company Risk Factor (FCR) value based on the company type.
    """
    return COMPANY_TYPE_FACTORS.get(company_type, 1.0) # Default to 1.0 if not found

def get_h_base_value(occupation: str) -> float:
    """
    Retrieves the Base Occupational Hazard (H_base) value for a given occupation.
    """
    return OCCUPATION_HAZARDS.get(occupation, 50) # Default to 50 if not found

def get_role_multiplier_value(role: str) -> float:
    """
    Retrieves the Role Multiplier (f_role) value.
    """
    return ROLE_MULTIPLIERS.get(role, 1.0)

def get_education_level_value(level: str) -> float:
    """
    Retrieves the Education Level Factor (f_level) value.
    """
    return EDUCATION_LEVEL_FACTORS.get(level, 1.0)

def get_education_field_value(field: str) -> float:
    """
    Retrieves the Education Field Factor (f_field) value.
    """
    return EDUCATION_FIELD_FACTORS.get(field, 1.0)

def get_school_tier_value(tier: str) -> float:
    """
    Retrieves the Institution Tier Factor (f_school) value.
    """
    return SCHOOL_TIER_FACTORS.get(tier, 1.0)

def get_economic_modifier_value(scenario: str) -> float:
    """
    Retrieves the Economic Climate Modifier (M_econ) value.
    """
    return ECONOMIC_CLIMATE_SCENARIOS.get(scenario, 1.0)

def get_ai_innovation_modifier_value(scenario: str) -> float:
    """
    Retrieves the AI Innovation Index (I_AI) value.
    """
    return AI_INNOVATION_SCENARIOS.get(scenario, 1.0)

def get_recommended_skills_for_occupation(occupation: str):
    """
    Returns recommended general and firm-specific skills for a given occupation.
    """
    return OCCUPATION_RECOMMENDED_SKILLS.get(occupation, {"general": [], "firm-specific": []})

def filter_learning_resources(skill_list, skill_type=None):
    """
    Filters learning resources based on a list of skills and optionally by skill type.
    """
    filtered_df = LEARNING_RESOURCES[LEARNING_RESOURCES['Skill'].isin(skill_list)]
    if skill_type:
        filtered_df = filtered_df[filtered_df['Type'] == skill_type]
    return filtered_df
