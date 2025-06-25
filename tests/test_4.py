import pytest
from definition_77c76769683844e3b693d62b4a8b1279 import calculate_fexp

@pytest.mark.parametrize("years_experience, expected", [
    (0, 1.0),                         # no experience
    (1, 1 - 0.015 * 1),
    (10, 1 - 0.015 * 10),
    (19.9999, 1 - 0.015 * 19.9999),
    (20, 1 - 0.015 * 20),            # boundary at 20 should be capped
    (25, 1 - 0.015 * 20),            # above 20 capped at 20
    (100, 1 - 0.015 * 20),           # large value capped at 20
    (20.0001, 1 - 0.015 * 20),       # just above 20 capped
    (-1, 1 + 0.015 * 1),              # negative experience - input edge case, expects handling (returns >1)
    (-100, 1 + 0.015 * 100),          # large negative, potentially invalid input
    ("10", TypeError),                # wrong type string
    (None, TypeError),                # None input
    ([], TypeError),                  # wrong type list
])

def test_calculate_fexp(years_experience, expected):
    try:
        result = calculate_fexp(years_experience)
        assert isinstance(result, float)
        assert abs(result - expected) < 1e-7
    except Exception as e:
        assert isinstance(e, expected)