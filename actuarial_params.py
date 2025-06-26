
# actuarial_params.py
# Constants for actuarial parameters

BETA_SYSTEMIC = 0.10
BETA_INDIVIDUAL = 0.50
LOADING_FACTOR = 1.5
MIN_PREMIUM = 20.00
TTV_PERIOD_MONTHS = 12 # Time-to-Value period in months

# Weights for Idiosyncratic Risk
W_CR = 0.4 # Weight for Company Risk Factor
W_US = 0.6 # Weight for Upskilling Factor

# Weights for Upskilling Factor (gamma_gen > gamma_spec ensures portable skills are rewarded more)
GAMMA_GEN = 0.7
GAMMA_SPEC = 0.3

# Weights for Systematic Risk
W_ECON = 0.5 # Weight for Economic Climate Modifier
W_INNO = 0.5 # Weight for AI Innovation Index
