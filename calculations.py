
import numpy as np
from actuarial_params import BETA_SYSTEMIC, BETA_INDIVIDUAL, LAMBDA, P_MIN, TTV, W_CR, W_US, GAMMA_GEN, GAMMA_SPEC, W_ECON, W_INNO

def calculate_fexp(years_experience: float) -> float:
    """
    Calculates the Experience Factor (f_exp).
    $f_{exp} = 1 - (0.015 \cdot \min(	ext{years\_experience}, 20))$
    """
    return 1 - (0.015 * min(years_experience, 20))

def calculate_fhc(f_role: float, f_level: float, f_field: float, f_school: float, f_exp: float) -> float:
    """
    Calculates the Human Capital Factor (FHC).
    $FHC = f_{role} \cdot f_{level} \cdot f_{field} \cdot f_{school} \cdot f_{exp}$
    """
    return f_role * f_level * f_field * f_school * f_exp

def calculate_fus(p_gen: float, p_spec: float, gamma_gen: float = GAMMA_GEN, gamma_spec: float = GAMMA_SPEC) -> float:
    """
    Calculates the Upskilling Factor (F_US).
    $F_{US} = 1 - (\gamma_{gen} P_{gen}(t) + \gamma_{spec} P_{spec}(t))$
    """
    return 1 - (gamma_gen * p_gen + gamma_spec * p_spec)

def calculate_fcr(s_senti: float, s_fin: float, s_growth: float, w1: float = 0.33, w2: float = 0.34, w3: float = 0.33) -> float:
    """
    Calculates the Company Risk Factor (FCR).
    $FCR = w_{1} \cdot S_{senti} + w_{2} \cdot S_{fin} + w_{3} \cdot S_{growth}$
    For simplicity, S_senti, S_fin, S_growth are pre-calculated as part of COMPANY_TYPE_FACTORS in data.
    So, this function will take the pre-calculated FCR directly from the lookup.
    """
    # In this implementation, FCR is directly looked up from COMPANY_TYPE_FACTORS
    # For a more detailed FCR calculation, the individual sentiment, financial, and growth scores
    # would need to be provided as inputs.
    return s_senti # Renamed s_senti to simply fcr_value as it directly represents the FCR from lookup

def calculate_v_idiosyncratic_raw(fhc: float, fcr: float, fus: float, w_cr: float = W_CR, w_us: float = W_US) -> float:
    """
    Calculates the raw Idiosyncratic Risk (V_raw).
    $V_{raw} = FHC \cdot (w_{CR} \cdot FCR + w_{US} \cdot FUS)$
    """
    return fhc * (w_cr * fcr + w_us * fus)

def calculate_v_idiosyncratic_normalized(v_raw: float) -> float:
    """
    Normalizes the Idiosyncratic Risk score (V_i(t)) to a scale of 0-100.
    $V_{i}(t) = \min(100.0, \max(5.0, V_{raw} \cdot 50.0))$
    """
    return min(100.0, max(5.0, v_raw * 50.0))

def calculate_h_base_ttv(h_current: float, h_target: float, k: int, ttv: int = TTV) -> float:
    """
    Calculates the Base Occupational Hazard (H_base(k)) adjusted for career transitions using TTV.
    $H_{base}(k) = \left(1 - \frac{k}{TTV}\right) \cdot H_{current} + \left(\frac{k}{TTV}\right) \cdot H_{target}$
    """
    if k > ttv: # If months elapsed exceed TTV, assume full transition to target hazard
        return h_target
    return (1 - k/ttv) * h_current + (k/ttv) * h_target

def calculate_systematic_risk(h_base: float, m_econ: float, i_ai: float, w_econ: float = W_ECON, w_inno: float = W_INNO) -> float:
    """
    Calculates the Systematic Risk score (H_i).
    $H_{i} = H_{base}(t) \cdot (w_{econ} M_{econ} + w_{inno} I_{AI})$
    """
    return h_base * (w_econ * m_econ + w_inno * i_ai)

def calculate_p_systemic(h_i: float, beta_systemic: float = BETA_SYSTEMIC) -> float:
    """
    Calculates the Probability of a systemic displacement event (P_systemic).
    $P_{systemic} = \frac{H_{i}}{100} \cdot eta_{systemic}$
    """
    return (h_i / 100.0) * beta_systemic

def calculate_p_individual_conditional(v_i_t: float, beta_individual: float = BETA_INDIVIDUAL) -> float:
    """
    Calculates the Conditional probability of job loss for the individual (P_individual|systemic).
    $P_{individual|systemic} = \frac{V_{i}(t)}{100} \cdot eta_{individual}$
    """
    return (v_i_t / 100.0) * beta_individual

def calculate_p_claim(p_systemic: float, p_individual_conditional: float) -> float:
    """
    Calculates the Annual Claim Probability (P_claim).
    $P_{claim} = P_{systemic} \cdot P_{individual|systemic}$
    """
    return p_systemic * p_individual_conditional

def calculate_l_payout(annual_salary: float, coverage_duration_months: int, coverage_percentage: float) -> float:
    """
    Calculates the Total payout amount if a claim is triggered (L_payout).
    $L_{payout} = \left(\frac{	ext{Annual Salary}}{12} \cdot 	ext{Coverage Duration}\right) \cdot 	ext{Coverage Percentage}$
    """
    return (annual_salary / 12.0 * coverage_duration_months) * coverage_percentage

def calculate_expected_loss(p_claim: float, l_payout: float) -> float:
    """
    Calculates the Annual Expected Loss (E[Loss]).
    $E[Loss] = P_{claim} \cdot L_{payout}$
    """
    return p_claim * l_payout

def calculate_monthly_premium(e_loss: float, lambd: float = LAMBDA, p_min: float = P_MIN) -> float:
    """
    Calculates the Monthly Premium (P_monthly).
    $P_{monthly} = \max\left(\frac{E[Loss] \cdot \lambda}{12}, P_{min}\right)$
    """
    return max((e_loss * lambd) / 12.0, p_min)

