import pytest
from definition_c6d91bdb6c47480794d6ff56faa7ab23 import calculate_fus

@pytest.mark.parametrize("p_gen, p_spec, gamma_gen, gamma_spec, expected", [
    # Typical valid inputs: zero progress
    (0.0, 0.0, 0.7, 0.3, 1.0),
    # Full progress, general skills weighted higher than firm-specific
    (1.0, 0.0, 0.7, 0.3, 1 - 0.7*1.0 - 0.3*0.0),
    (0.0, 1.0, 0.7, 0.3, 1 - 0.7*0.0 - 0.3*1.0),
    (1.0, 1.0, 0.7, 0.3, 1 - 0.7*1.0 - 0.3*1.0),
    # Intermediate progress values
    (0.5, 0.5, 0.7, 0.3, 1 - (0.7*0.5 + 0.3*0.5)),
    (0.3, 0.6, 0.8, 0.2, 1 - (0.8*0.3 + 0.2*0.6)),
    # Gamma general greater than gamma spec (enforced by user, check output correct)
    (0.7, 0.4, 0.9, 0.5, 1 - (0.9*0.7 + 0.5*0.4)),
    # Edge cases - minimal gamma values
    (0.0, 0.0, 0.0, 0.0, 1.0),
    (1.0, 1.0, 0.0, 0.0, 1.0),
    # Edge cases - negative progress (should be handled, expect an error)
    (-0.1, 0.0, 0.7, 0.3, ValueError),
    (0.0, -0.1, 0.7, 0.3, ValueError),
    # Edge cases - progress > 1 (should be handled, expect an error)
    (1.1, 0.0, 0.7, 0.3, ValueError),
    (0.0, 1.1, 0.7, 0.3, ValueError),
    # Edge cases - gamma values negative or zero or >1 (should allow zero but not negative)
    (0.5, 0.5, 0.0, 0.0, 1 - (0.0*0.5 + 0.0*0.5)),
    (0.5, 0.5, -0.1, 0.3, ValueError),
    (0.5, 0.5, 0.7, -0.1, ValueError),
    (0.5, 0.5, 1.5, 0.3, ValueError),  # gamma_gen > 1 possible? Depending on spec, disallow >1.
    (0.5, 0.5, 0.7, 1.5, ValueError),
    # Non-float types for progress and gamma (should raise TypeError)
    ("0.5", 0.5, 0.7, 0.3, TypeError),
    (0.5, "0.5", 0.7, 0.3, TypeError),
    (0.5, 0.5, "0.7", 0.3, TypeError),
    (0.5, 0.5, 0.7, "0.3", TypeError),
    (None, 0.5, 0.7, 0.3, TypeError),
    (0.5, None, 0.7, 0.3, TypeError),
    (0.5, 0.5, None, 0.3, TypeError),
    (0.5, 0.5, 0.7, None, TypeError),
])
def test_calculate_fus(p_gen, p_spec, gamma_gen, gamma_spec, expected):
    # Before calling, perform input validation expected in calculate_fus
    # If function does not have input validation, this test expects exceptions accordingly
    # Both p_gen, p_spec must be floats between 0 and 1 inclusive
    # gamma_gen, gamma_spec must be non-negative floats; typically gamma_gen > gamma_spec
    
    def is_float_and_between_0_1(x):
        return isinstance(x, (float,int)) and 0.0 <= x <= 1.0
    
    def is_non_negative_float(x):
        return isinstance(x, (float,int)) and x >= 0.0
    
    # Validate expected exceptions for validation test cases
    if expected in (ValueError, TypeError):
        with pytest.raises(expected):
            # We try to simulate validation inside or let calculate_fus raise
            # The tested function may or may not raise exception; test fails if not
            
            # So call function only if inputs are all floats, otherwise expect error
            # We call the function assuming it will validate inputs internally
            
            # Direct call
            calculate_fus(p_gen, p_spec, gamma_gen, gamma_spec)
    else:
        # For valid inputs check output numeric value within floating point tolerance
        result = calculate_fus(p_gen, p_spec, gamma_gen, gamma_spec)
        assert isinstance(result, float)
        assert abs(result - expected) < 1e-8
        # Check result is between -Infinity and 1.0 (per formula max 1.0, but can be negative if no bounds)
        # Optionally result should not be less than 0, unless formula allows negative
        # From formula: 1 - (gamma_gen*p_gen + gamma_spec*p_spec), can be negative if sum > 1
        # But since p_gen and p_spec in [0,1], and gamma_gen, gamma_spec non-negative, can be > 1 sum.
        # So allow negative results, but in use-case should be validated externally.
