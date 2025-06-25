
# actuarial_params.py

# Weights for Idiosyncratic Risk (V_raw)
W_CR = 0.4  # Weight for Company Risk Factor
W_US = 0.6  # Weight for Upskilling Factor

# Weights for Upskilling Factor (F_US) - gamma_gen > gamma_spec
GAMMA_GEN = 0.7 # Weight for general/portable skills
GAMMA_SPEC = 0.3 # Weight for firm-specific skills

# Weights for Systematic Risk (H_i)
W_ECON = 0.5 # Weight for Economic Climate Modifier
W_INNO = 0.5 # Weight for AI Innovation Index

# Base Probabilities for Claim Calculation
BETA_SYSTEMIC = 0.10 # Systemic Event Base Probability
BETA_INDIVIDUAL = 0.50 # Individual Loss Base Probability

# Actuarial Parameters for Premium Calculation
LOADING_FACTOR = 1.5 # Lambda (λ) - standard insurance multiplier
MIN_PREMIUM = 20.00 # P_min - minimum monthly premium

# Time-to-Value (TTV) for Base Occupational Hazard transition
TTV_MONTHS = 12 # Total number of months in the Time-to-Value period (e.g., 12 months)
