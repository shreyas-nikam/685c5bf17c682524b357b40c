
# Constants for actuarial parameters

_BETA_SYSTEMIC = 0.10  # Systemic Event Base Probability
_BETA_INDIVIDUAL = 0.50  # Individual Loss Base Probability
_LOADING_FACTOR = 1.5   # Standard insurance multiplier
_MIN_PREMIUM = 20.00    # Minimum Premium in USD
_TTV = 12               # Total number of months in the Time-to-Value period (e.g., 12 months)
_W_CR = 0.4             # Weight for Company Risk Factor in V_raw
_W_US = 0.6             # Weight for Upskilling Factor in V_raw
_GAMMA_GEN = 0.005      # Weighting parameter for general skills (e.g., 0.005 for 0-100 scale, so 0.5 for 0-1 scale after division by 100)
_GAMMA_SPEC = 0.002     # Weighting parameter for firm-specific skills (e.g., 0.002 for 0-100 scale, so 0.2 for 0-1 scale after division by 100)
_W_ECON = 0.5           # Calibration weight for Economic Climate Modifier
_W_INNO = 0.5           # Calibration weight for AI Innovation Index
