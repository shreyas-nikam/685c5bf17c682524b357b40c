
# calculations.py
import numpy as np

# Import constants from actuarial_params
from actuarial_params import (
    W_CR, W_US, GAMMA_GEN, GAMMA_SPEC, W_ECON, W_INNO,
    BETA_SYSTEMIC, BETA_INDIVIDUAL, LOADING_FACTOR, MIN_PREMIUM, TTV_MONTHS
)

def calculate_fexp(years_experience: float) -> float:
    """
    Calculates the Experience Factor (f_exp).
    Formula: f_exp = 1 - (0.015 * min(years_experience, 20))
    """
    return 1 - (0.015 * min(years_experience, 20))

def calculate_fhc(f_role: float, f_level: float, f_field: float, f_school: float, f_exp: float) -> float:
    """
    Calculates the Human Capital Factor (FHC).
    Formula: FHC = f_role * f_level * f_field * f_school * f_exp
    """
    return f_role * f_level * f_field * f_school * f_exp

def calculate_fcr(s_senti: float) -> float: # Simplified as per spec that FCR is a direct lookup
    """
    Calculates the Company Risk Factor (FCR).
    For synthetic data, this will be a direct lookup value.
    The detailed formula FCR = w1 * S_senti + w2 * S_fin + w3 * S_growth is for conceptual understanding.
    This function returns the pre-calculated FCR value.
    """
    return s_senti # s_senti is effectively the pre-calculated FCR from lookup

def calculate_fus(p_gen: float, p_spec: float, gamma_gen: float = GAMMA_GEN, gamma_spec: float = GAMMA_SPEC) -> float:
    """
    Calculates the Upskilling Factor (F_US).
    Formula: F_US = 1 - (gamma_gen * p_gen + gamma_spec * p_spec)
    p_gen and p_spec should be between 0 and 1 (representing 0-100% progress).
    """
    return 1 - (gamma_gen * p_gen + gamma_spec * p_spec)

def calculate_idiosyncratic_risk_raw(fhc: float, fcr: float, fus: float, w_cr: float = W_CR, w_us: float = W_US) -> float:
    """
    Calculates the raw Idiosyncratic Risk (V_raw).
    Formula: V_raw = FHC * (w_CR * FCR + w_US * FUS)
    """
    return fhc * (w_cr * fcr + w_us * fus)

def calculate_idiosyncratic_risk(v_raw: float) -> float:
    """
    Normalizes the raw Idiosyncratic Risk score.
    Formula: V_i(t) = min(100.0, max(5.0, V_raw * 50.0))
    """
    return min(100.0, max(5.0, v_raw * 50.0))

def calculate_h_base_transition(k: int, ttv: int, h_current: float, h_target: float) -> float:
    """
    Calculates the Base Occupational Hazard adjusted for career transitions (H_base(k)).
    Formula: H_base(k) = (1 - k/TTV) * H_current + (k/TTV) * H_target
    k: Number of months elapsed since transition pathway completion.
    TTV: Total number of months in the Time-to-Value period.
    """
    if k >= ttv: # If months elapsed is equal or more than TTV, consider transition complete
        return h_target
    return (1 - k / ttv) * h_current + (k / ttv) * h_target

def calculate_systematic_risk(h_base_t: float, m_econ: float, i_ai: float, w_econ: float = W_ECON, w_inno: float = W_INNO) -> float:
    """
    Calculates the Systematic Risk score (H_i).
    Formula: H_i = H_base(t) * (w_econ * M_econ + w_inno * I_AI)
    """
    return h_base_t * (w_econ * m_econ + w_inno * i_ai)

def calculate_p_systemic(h_i: float, beta_systemic: float = BETA_SYSTEMIC) -> float:
    """
    Calculates the probability of a systemic displacement event (P_systemic).
    Formula: P_systemic = H_i / 100 * beta_systemic
    """
    return (h_i / 100.0) * beta_systemic

def calculate_p_individual_given_systemic(v_i_t: float, beta_individual: float = BETA_INDIVIDUAL) -> float:
    """
    Calculates the conditional probability of job loss for the individual, given a systemic event (P_individual|systemic).
    Formula: P_individual|systemic = V_i(t) / 100 * beta_individual
    """
    return (v_i_t / 100.0) * beta_individual

def calculate_annual_claim_probability(p_systemic: float, p_individual_given_systemic: float) -> float:
    """
    Calculates the annual probability of a claim (P_claim).
    Formula: P_claim = P_systemic * P_individual|systemic
    """
    return p_systemic * p_individual_given_systemic

def calculate_l_payout(annual_salary: float, coverage_duration_months: int, coverage_percentage: float) -> float:
    """
    Calculates the total payout amount if a claim is triggered (L_payout).
    Formula: L_payout = (Annual Salary / 12 * Coverage Duration) * Coverage Percentage
    """
    return (annual_salary / 12.0 * coverage_duration_months) * (coverage_percentage / 100.0)

def calculate_expected_loss(p_claim: float, l_payout: float) -> float:
    """
    Calculates the Annual Expected Loss (E[Loss]).
    Formula: E[Loss] = P_claim * L_payout
    """
    return p_claim * l_payout

def calculate_monthly_premium(e_loss: float, loading_factor: float = LOADING_FACTOR, min_premium: float = MIN_PREMIUM) -> float:
    """
    Calculates the monthly premium (P_monthly).
    Formula: P_monthly = max(E[Loss] * lambda / 12, P_min)
    """
    return max((e_loss * loading_factor) / 12.0, min_premium)
