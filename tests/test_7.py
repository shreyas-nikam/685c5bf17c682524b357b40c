import pytest
from definition_71cb6052ee2b4945a1c84588f0095c2c import calculate_p_systemic

@pytest.mark.parametrize(
    "H_i, beta_systemic, expected",
    [
        # Valid inputs - typical values
        (50.0, 0.1, 50.0 / 100 * 0.1),
        (100.0, 0.2, 100.0 / 100 * 0.2),
        (0.0, 0.5, 0.0),
        (25.5, 0.0, 0.0),
        (75.25, 1.0, 75.25 / 100 * 1.0),

        # Edge values at boundaries
        (0.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (100.0, 0.0, 0.0),
        (100.0, 1.0, 1.0),

        # Float precision checks
        (33.3333, 0.3333, 33.3333 / 100 * 0.3333),

        # Negative values (should handle or raise error)
        (-10.0, 0.1, ValueError),
        (50.0, -0.1, ValueError),
        (-5.0, -0.5, ValueError),

        # Values exceeding normal range (should handle or raise error)
        (150.0, 0.1, ValueError),
        (50.0, 1.5, ValueError),
        (200.0, 2.0, ValueError),

        # Non-numeric types
        ("50", 0.1, TypeError),
        (50.0, "0.1", TypeError),
        (None, 0.1, TypeError),
        (50.0, None, TypeError),

        # Passing completely wrong types
        ([], 0.1, TypeError),
        (50.0, {}, TypeError),
        ({}, [], TypeError),

    ]
)
def test_calculate_p_systemic(H_i, beta_systemic, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calculate_p_systemic(H_i, beta_systemic)
    else:
        result = calculate_p_systemic(H_i, beta_systemic)
        assert isinstance(result, float)
        # Floating point comparison with tolerance
        assert abs(result - expected) < 1e-6
