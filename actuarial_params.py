
# Constants for actuarial parameters
BETA_SYSTEMIC = 0.10  # Systemic Event Base Probability
BETA_INDIVIDUAL = 0.50  # Individual Loss Base Probability
LAMBDA = 1.5  # Loading Factor
P_MIN = 20.00  # Minimum Premium
TTV = 12  # Time-to-Value period in months (for H_base transition)
W_CR = 0.4  # Weight for Company Risk Factor in V_raw
W_US = 0.6  # Weight for Upskilling Factor in V_raw
GAMMA_GEN = 0.7  # Weighting parameter for general skills in F_US
GAMMA_SPEC = 0.3  # Weighting parameter for firm-specific skills in F_US (must be < GAMMA_GEN)
W_ECON = 0.5  # Calibration weight for Economic Climate Modifier in Systematic Risk
W_INNO = 0.5  # Calibration weight for AI Innovation Index in Systematic Risk
