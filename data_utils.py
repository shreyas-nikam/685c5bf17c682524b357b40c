
import pandas as pd
from data.occupation_data import OCCUPATION_HAZARDS, ROLE_MULTIPLIERS, COMPANY_TYPE_FACTORS
from data.education_data import EDUCATION_LEVEL_FACTORS, EDUCATION_FIELD_FACTORS, SCHOOL_TIER_FACTORS
from data.skill_data import SKILL_CATEGORIES, LEARNING_RESOURCES
from data.environmental_data import ECONOMIC_CLIMATE_SCENARIOS, AI_INNOVATION_SCENARIOS

def get_occupation_hazard(occupation: str) -> float:
    """Fetches the base occupational hazard for a given occupation."""
    return OCCUPATION_HAZARDS.get(occupation, 50.0) # Default to 50 if not found

def get_role_multiplier(occupation: str) -> float:
    """Fetches the role multiplier for a given occupation."""
    return ROLE_MULTIPLIERS.get(occupation, 1.0) # Default to 1.0 if not found

def get_company_type_factor(company_type: str) -> float:
    """Fetches the company risk factor for a given company type."""
    return COMPANY_TYPE_FACTORS.get(company_type, 1.0) # Default to 1.0 if not found

def get_education_level_factor(level: str) -> float:
    """Fetches the education level factor."""
    return EDUCATION_LEVEL_FACTORS.get(level, 1.0) # Default to 1.0

def get_education_field_factor(field: str) -> float:
    """Fetches the education field factor."""
    return EDUCATION_FIELD_FACTORS.get(field, 1.0) # Default to 1.0

def get_school_tier_factor(tier: str) -> float:
    """Fetches the school tier factor."""
    return SCHOOL_TIER_FACTORS.get(tier, 1.0) # Default to 1.0

def get_economic_climate_modifier(scenario: str) -> float:
    """Fetches the economic climate modifier for a given scenario."""
    return ECONOMIC_CLIMATE_SCENARIOS.get(scenario, 1.0)

def get_ai_innovation_index(scenario: str) -> float:
    """Fetches the AI innovation index for a given scenario."""
    return AI_INNOVATION_SCENARIOS.get(scenario, 1.0)

def get_learning_resources_by_skill_type(skill_type: str) -> pd.DataFrame:
    """Filters learning resources by skill type (general or firm-specific)."""
    return LEARNING_RESOURCES[LEARNING_RESOURCES['Type'] == skill_type]

def get_skills_for_occupation(occupation: str):
    """
    Placeholder function to suggest high-impact skills for an occupation.
    In a real app, this would be a more sophisticated lookup or ML model.
    """
    # For demonstration, we'll return a mix of general and specific skills
    # based on the occupation.
    if "Engineer" in occupation or "Analyst" in occupation:
        return {
            "general": ["Python", "Data Analysis", "Machine Learning", "Cloud Computing", "SQL", "Project Management"],
            "firm-specific": ["Proprietary CRM Software", "Company-specific Financial Models"]
        }
    elif "Paralegal" in occupation or "HR" in occupation:
        return {
            "general": ["Communication", "Problem Solving", "Critical Thinking", "Project Management", "Negotiation"],
            "firm-specific": ["Internal Compliance Procedures", "Legacy System Maintenance"]
        }
    elif "Financial Advisor" in occupation:
        return {
            "general": ["Data Analysis", "Critical Thinking", "Communication", "Advanced Excel"],
            "firm-specific": ["Company-specific Financial Models", "Internal Compliance Procedures"]
        }
    elif "Customer Service" in occupation:
        return {
            "general": ["Communication", "Problem Solving", "Critical Thinking"],
            "firm-specific": ["Proprietary CRM Software", "Internal Compliance Procedures"]
        }
    else:
        return {
            "general": ["Python", "Data Analysis", "Project Management", "Communication"],
            "firm-specific": ["Internal Compliance Procedures", "Proprietary CRM Software"]
        }
