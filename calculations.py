# calculations.py
# All AI-Q score and premium calculation functions

import numpy as np
from actuarial_params import *
from data.occupation_data import ROLE_MULTIPLIERS, OCCUPATION_HAZARDS, COMPANY_TYPE_FACTORS
from data.education_data import EDUCATION_LEVEL_FACTORS, EDUCATION_FIELD_FACTORS, SCHOOL_TIER_FACTORS
from data.environmental_data import ECONOMIC_CLIMATE_SCENARIOS, AI_INNOVATION_SCENARIOS

def calculate_fexp(years_experience: float) -> float:
    """
    Calculates the Experience Factor (f_exp).
    Formula: f_exp = 1 - (0.015 * min(years_experience, 20))
    """
    return 1 - (0.015 * min(years_experience, 20))

def calculate_fhc(
    occupation: str,
    years_experience: float,
    education_level: str,
    education_field: str,
    school_tier: str
) -> float:
    """
    Calculates the Human Capital Factor (FHC).
    Formula: FHC = f_role * f_level * f_field * f_school * f_exp
    """
    f_role = ROLE_MULTIPLIERS.get(occupation, 1.0) # Default to 1.0 if not found
    f_level = EDUCATION_LEVEL_FACTORS.get(education_level, 1.0)
    f_field = EDUCATION_FIELD_FACTORS.get(education_field, 1.0)
    f_school = SCHOOL_TIER_FACTORS.get(school_tier, 1.0)
    f_exp = calculate_fexp(years_experience)

    fhc_raw = f_role * f_level * f_field * f_school * f_exp
    return fhc_raw

def calculate_fcr(company_type: str) -> float:
    """
    Calculates the Company Risk Factor (FCR).
    Formula: FCR = w1 * S_senti + w2 * S_fin + w3 * S_growth
    (Uses synthetic lookup based on company_type for S_senti, S_fin, S_growth)
    """
    factors = COMPANY_TYPE_FACTORS.get(company_type, {"sentiment": 1.0, "financial": 1.0, "growth": 1.0})
    # As per prompt, interpret COMPANY_TYPE_FACTORS directly for FCR, where higher is riskier.
    # The example values (0.95, 1.00, 1.10) for FCR in the spec (if they were FCR) match this.
    # Since the internal factors (sentiment, financial, growth) are given, and no explicit weights,
    # let's assume they contribute equally to a combined FCR for simplicity in this synthetic data context.
    # Higher values in factors means higher risk.
    return (factors["sentiment"] + factors["financial"] + factors["growth"]) / 3.0

def calculate_fus(p_gen: float, p_spec: float) -> float:
    """
    Calculates the Upskilling Factor (F_US).
    Formula: F_US = 1 - (gamma_gen * P_gen(t) + gamma_spec * P_spec(t))
    p_gen and p_spec are 0-100%, convert to 0-1.
    """
    p_gen_norm = p_gen / 100.0
    p_spec_norm = p_spec / 100.0
    return 1 - (GAMMA_GEN * p_gen_norm + GAMMA_SPEC * p_spec_norm)

def calculate_idiosyncratic_risk(fhc: float, fcr: float, fus: float) -> float:
    """
    Calculates the Idiosyncratic Risk (V_i(t)).
    Formula: V_raw = FHC * (w_CR * FCR + w_US * FUS)
    Final V_i(t) = min(100.0, max(5.0, V_raw * 50.0))
    """
    v_raw = fhc * (W_CR * fcr + W_US * fus)
    v_i_t = min(100.0, max(5.0, v_raw * 50.0))
    return v_i_t

def calculate_h_base(
    current_occupation: str,
    target_occupation: str = None,
    months_elapsed_transition: int = 0
) -> float:
    """
    Calculates the Base Occupational Hazard (H_base(t)).
    If transitioning, H_base(k) = (1 - k/TTV) * H_current + (k/TTV) * H_target
    """
    h_current = OCCUPATION_HAZARDS.get(current_occupation, 50) # Default to 50
    if target_occupation and months_elapsed_transition > 0 and target_occupation in OCCUPATION_HAZARDS:
        h_target = OCCUPATION_HAZARDS.get(target_occupation, h_current)
        k = min(months_elapsed_transition, TTV_PERIOD_MONTHS) # Cap k at TTV_PERIOD_MONTHS
        h_base_k = (1 - k / TTV_PERIOD_MONTHS) * h_current + (k / TTV_PERIOD_MONTHS) * h_target
        return h_base_k
    return h_current

def calculate_systematic_risk(
    h_base: float,
    economic_climate: str,
    ai_innovation_pace: str
) -> float:
    """
    Calculates the Systematic Risk (H_i).
    Formula: H_i = H_base(t) * (w_econ * M_econ + w_inno * I_AI)
    """
    m_econ = ECONOMIC_CLIMATE_SCENARIOS.get(economic_climate, 1.0)
    i_ai = AI_INNOVATION_SCENARIOS.get(ai_innovation_pace, 1.0)

    h_i = h_base * (W_ECON * m_econ + W_INNO * i_ai)
    return h_i

def calculate_p_systemic(h_i: float) -> float:
    """
    Calculates the Probability of a Systemic Displacement Event (P_systemic).
    Formula: P_systemic = H_i / 100 * Beta_systemic
    """
    return (h_i / 100.0) * BETA_SYSTEMIC

def calculate_p_individual_given_systemic(v_i_t: float) -> float:
    """
    Calculates the Conditional Probability of Job Loss (P_individual|systemic).
    Formula: P_individual|systemic = V_i(t) / 100 * Beta_individual
    """
    return (v_i_t / 100.0) * BETA_INDIVIDUAL

def calculate_annual_claim_probability(p_systemic: float, p_individual_given_systemic: float) -> float:
    """
    Calculates the Annual Claim Probability (P_claim).
    Formula: P_claim = P_systemic * P_individual|systemic
    """
    return p_systemic * p_individual_given_systemic

def calculate_l_payout(annual_salary: float, coverage_duration_months: int, coverage_percentage: float) -> float:
    """
    Calculates the Total Payout Amount if a claim is triggered (L_payout).
    Formula: L_payout = (Annual Salary / 12 * Coverage Duration) * Coverage Percentage / 100
    (Coverage Percentage is 0-100, convert to 0-1)
    """
    return (annual_salary / 12.0 * coverage_duration_months) * (coverage_percentage / 100.0)

def calculate_expected_loss(p_claim: float, l_payout: float) -> float:
    """
    Calculates the Annual Expected Loss (E[Loss]).
    Formula: E[Loss] = P_claim * L_payout
    """
    return p_claim * l_payout

def calculate_monthly_premium(e_loss: float) -> float:
    """
    Calculates the Monthly Premium (P_monthly).
    Formula: P_monthly = max(E[Loss] * lambda / 12, P_min)
    """
    return max((e_loss * LOADING_FACTOR) / 12.0, MIN_PREMIUM)
