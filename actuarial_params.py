
# actuarial_params.py

# Constants for actuarial parameters
BETA_SYSTEMIC = 0.10  # Systemic Event Base Probability
BETA_INDIVIDUAL = 0.50  # Individual Loss Base Probability
LAMBDA_LOADING_FACTOR = 1.5  # Loading Factor, a standard insurance multiplier
P_MIN = 20.00  # Minimum Premium (e.g., $20.00) to ensure policy viability
TTV_MONTHS = 12  # Total number of months in the Time-to-Value period (e.g., 12 months)

# Weights for Idiosyncratic Risk (V_raw)
W_CR = 0.4  # Weight for Company Risk Factor
W_US = 0.6  # Weight for Upskilling Factor

# Weights for Upskilling Factor (F_US)
GAMMA_GEN = 0.7  # Weighting parameter for general skills (must be > gamma_spec)
GAMMA_SPEC = 0.3  # Weighting parameter for firm-specific skills

# Weights for Systematic Risk (H_i)
W_ECON = 0.5  # Calibration weight for Economic Climate Modifier
W_INNO = 0.5  # Calibration weight for AI Innovation Index
