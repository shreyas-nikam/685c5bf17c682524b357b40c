import pytest
from definition_05f2150a34ca405bba9cd56d928940b7 import calculate_p_individual_given_systemic

@pytest.mark.parametrize("V_i_t, beta_individual, expected", [
    # Normal cases within range
    (0.0, 0.5, 0.0),
    (50.0, 0.5, 0.25),
    (100.0, 0.5, 0.5),

    # Edge cases on boundaries of V_i_t
    (5.0, 0.1, 0.005),
    (100.0, 1.0, 1.0),

    # Edge cases on beta_individual boundaries
    (50.0, 0.0, 0.0),
    (50.0, 1.0, 0.5),

    # Test float precision
    (33.3333, 0.3333, 33.3333 / 100 * 0.3333),
    (99.9999, 0.9999, 99.9999 / 100 * 0.9999),

    # Invalid negative inputs
    (-10.0, 0.5, ValueError),
    (50.0, -0.1, ValueError),

    # Inputs greater than normal max for V_i_t (should still compute mathematically)
    (150.0, 0.5, 150.0 / 100 * 0.5),

    # Non-float inputs that can be cast to float
    (25, 0.5, 25 / 100 * 0.5),

    # Completely invalid types
    ("50", 0.5, TypeError),
    (50.0, "0.5", TypeError),
    (None, 0.5, TypeError),
    (50.0, None, TypeError),

    # Both params invalid types
    ("abc", None, TypeError),
])
def test_calculate_p_individual_given_systemic(V_i_t, beta_individual, expected):
    try:
        result = calculate_p_individual_given_systemic(V_i_t, beta_individual)
        if isinstance(expected, type) and issubclass(expected, Exception):
            pytest.fail(f"Expected exception {expected} but got result {result}")
        else:
            assert abs(result - expected) < 1e-6
    except Exception as e:
        assert isinstance(e, expected)
