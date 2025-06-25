import pytest
from definition_dc75d65d904e47679fee87745449bc96 import calculate_L_payout

@pytest.mark.parametrize("annual_salary, coverage_duration, coverage_percentage, expected", [
    # Normal cases
    (120000, 6, 0.5, (120000 / 12) * 6 * 0.5),
    (0, 12, 1.0, 0.0),
    (50000, 1, 0.1, (50000 / 12) * 1 * 0.1),
    (100000, 0, 0.8, 0.0),
    (100000, 12, 0, 0.0),
    (100000, 12, 1, (100000 / 12) * 12 * 1),

    # Edge cases: coverage_percentage exactly 0 and 1
    (75000, 3, 0, 0.0),
    (75000, 3, 1, (75000 / 12) * 3 * 1),

    # Edge cases: coverage_duration zero and large values
    (60000, 0, 0.5, 0.0),
    (60000, 24, 0.25, (60000 / 12) * 24 * 0.25),

    # Edge cases: annual_salary zero or very small
    (0, 12, 0.5, 0.0),
    (0.01, 12, 0.5, (0.01 /12) * 12 * 0.5),

    # Invalid inputs: negative values should raise ValueError
    (-1000, 12, 0.5, ValueError),
    (100000, -1, 0.5, ValueError),
    (100000, 12, -0.1, ValueError),
    (100000, 12, 1.1, ValueError),

    # Invalid types
    ("100000", 12, 0.5, TypeError),
    (100000, "12", 0.5, TypeError),
    (100000, 12, "0.5", TypeError),
    (None, 12, 0.5, TypeError),
    (100000, None, 0.5, TypeError),
    (100000, 12, None, TypeError),
])
def test_calculate_L_payout(annual_salary, coverage_duration, coverage_percentage, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calculate_L_payout(annual_salary, coverage_duration, coverage_percentage)
    else:
        result = calculate_L_payout(annual_salary, coverage_duration, coverage_percentage)
        assert isinstance(result, float) or isinstance(result, int)
        assert abs(result - expected) < 1e-6

