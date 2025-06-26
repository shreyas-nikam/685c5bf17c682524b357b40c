
# actuarial_params.py

# Constants for Annual Claim Probability
BETA_SYSTEMIC = 0.10
BETA_INDIVIDUAL = 0.50

# Constants for Monthly Premium
LOADING_FACTOR = 1.5
MIN_PREMIUM = 20.00

# Constants for Base Occupational Hazard (with TTV Modifier)
TTV_MONTHS = 12 # Total number of months in the Time-to-Value period

# Constants for Idiosyncratic Risk (Vulnerability)
W_CR = 0.4 # Weight for Company Risk Factor
W_US = 0.6 # Weight for Upskilling Factor

# Constants for Upskilling Factor
GAMMA_GEN = 0.7 # Weighting parameter for general skills (must be > GAMMA_SPEC)
GAMMA_SPEC = 0.3 # Weighting parameter for firm-specific skills

# Constants for Systematic Risk (Hazard)
W_ECON = 0.5 # Calibration weight for Economic Climate Modifier
W_INNO = 0.5 # Calibration weight for AI Innovation Index
