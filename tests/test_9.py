import pytest
from definition_9ba1fb388e09468e9b10700c195523c0 import calculate_annual_claim_probability

@pytest.mark.parametrize("P_systemic, P_individual_given_systemic, expected", [
    # Normal valid probabilities
    (0.0, 0.0, 0.0),
    (0.0, 1.0, 0.0),
    (1.0, 0.0, 0.0),
    (1.0, 1.0, 1.0),
    (0.5, 0.5, 0.25),
    (0.1, 0.9, 0.09),
    (0.9, 0.1, 0.09),
    (0.3, 0.7, 0.21),

    # Edge cases: values very close to 0 and 1
    (1e-10, 1e-10, 1e-20),
    (1 - 1e-10, 1 - 1e-10, (1 - 1e-10)**2),

    # Invalid cases: probabilities less than 0
    (-0.1, 0.5, ValueError),
    (0.5, -0.1, ValueError),
    (-0.1, -0.1, ValueError),

    # Invalid cases: probabilities greater than 1
    (1.1, 0.5, ValueError),
    (0.5, 1.1, ValueError),
    (1.1, 1.1, ValueError),

    # Invalid types: non-float inputs
    ("0.5", 0.5, TypeError),
    (0.5, "0.5", TypeError),
    (None, 0.5, TypeError),
    (0.5, None, TypeError),
    ([0.5], 0.5, TypeError),
    (0.5, [0.5], TypeError),
    ({}, {}, TypeError),
])

def test_calculate_annual_claim_probability(P_systemic, P_individual_given_systemic, expected):
    try:
        result = calculate_annual_claim_probability(P_systemic, P_individual_given_systemic)
        if isinstance(expected, float):
            # Allow for floating point small delta tolerance
            assert abs(result - expected) < 1e-9
        else:
            # If expected is an exception type but no exception was raised, test fails
            pytest.fail(f"Expected exception {expected}, but got result {result}")
    except Exception as e:
        assert isinstance(e, expected)
