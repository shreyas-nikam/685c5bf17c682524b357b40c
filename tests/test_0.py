import pytest
from definition_b7afec7a037c444ca96676947f088598 import calculate_fhc

@pytest.mark.parametrize(
    "f_role, f_level, f_field, f_school, f_exp, expected",
    [
        # Typical valid inputs (positive floats)
        (1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
        (1.2, 0.9, 1.1, 0.95, 0.7, 1.2 * 0.9 * 1.1 * 0.95 * 0.7),
        (0.5, 0.8, 1.0, 1.0, 0.9, 0.5 * 0.8 * 1.0 * 1.0 * 0.9),
        # Edge case: zero factors (should produce zero result)
        (0.0, 1.0, 1.0, 1.0, 1.0, 0.0),
        (1.0, 0.0, 1.0, 1.0, 1.0, 0.0),
        (1.0, 1.0, 0.0, 1.0, 1.0, 0.0),
        (1.0, 1.0, 1.0, 0.0, 1.0, 0.0),
        (1.0, 1.0, 1.0, 1.0, 0.0, 0.0),
        # Edge case: very small numbers (close to zero but positive)
        (1e-9, 1.0, 1.0, 1.0, 1.0, 1e-9),
        (1.0, 1e-9, 1.0, 1.0, 1.0, 1e-9),
        (1.0, 1.0, 1e-9, 1.0, 1.0, 1e-9),
        (1.0, 1.0, 1.0, 1e-9, 1.0, 1e-9),
        (1.0, 1.0, 1.0, 1.0, 1e-9, 1e-9),
        # Edge case: large numbers
        (1e6, 1e2, 1e3, 1e-1, 1e0, 1e6 * 1e2 * 1e3 * 1e-1 * 1e0),
        # Edge case: floating point numbers with high precision
        (1.123456789, 0.987654321, 1.111111111, 0.999999999, 0.888888888,
         1.123456789 * 0.987654321 * 1.111111111 * 0.999999999 * 0.888888888),
        # Edge case: negative values (should raise ValueError)
        (-1.0, 1.0, 1.0, 1.0, 1.0, ValueError),
        (1.0, -1.0, 1.0, 1.0, 1.0, ValueError),
        (1.0, 1.0, -1.0, 1.0, 1.0, ValueError),
        (1.0, 1.0, 1.0, -1.0, 1.0, ValueError),
        (1.0, 1.0, 1.0, 1.0, -1.0, ValueError),
        # Edge case: non-numeric types (should raise TypeError)
        ("1.0", 1.0, 1.0, 1.0, 1.0, TypeError),
        (1.0, "1.0", 1.0, 1.0, 1.0, TypeError),
        (1.0, 1.0, None, 1.0, 1.0, TypeError),
        (1.0, 1.0, 1.0, [], 1.0, TypeError),
        (1.0, 1.0, 1.0, 1.0, {}, TypeError),
        # Edge case: None inputs (should raise TypeError)
        (None, 1.0, 1.0, 1.0, 1.0, TypeError),
        (1.0, None, 1.0, 1.0, 1.0, TypeError),
        (1.0, 1.0, None, 1.0, 1.0, TypeError),
        (1.0, 1.0, 1.0, None, 1.0, TypeError),
        (1.0, 1.0, 1.0, 1.0, None, TypeError),
    ],
)
def test_calculate_fhc(f_role, f_level, f_field, f_school, f_exp, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calculate_fhc(f_role, f_level, f_field, f_school, f_exp)
    else:
        result = calculate_fhc(f_role, f_level, f_field, f_school, f_exp)
        assert isinstance(result, float)
        # For floating point comparisons allow a relative tolerance
        assert pytest.approx(result, rel=1e-9) == expected
