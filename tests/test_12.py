import pytest
from definition_d2c6f8a790e44192bf115bbe32ff7f8f import calculate_monthly_premium

@pytest.mark.parametrize("E_loss, loading_factor, P_min, expected", [
    # Normal cases
    (1200.0, 1.5, 20.0, max((1200.0 * 1.5) / 12, 20.0)),
    (0.0, 1.0, 15.0, 15.0),                     # Zero expected loss, premium should be floored at P_min
    (1000.0, 1.0, 0.0, max((1000.0 * 1.0) / 12, 0.0)),  # Zero minimum premium, monthly premium just calculated
    (500.0, 2.0, 50.0, max((500.0 * 2.0) / 12, 50.0)),
    (500.0, 0.0, 25.0, 25.0),                   # Zero loading factor, premium floored at P_min
    (1000.0, 1.25, 1000.0, 1000.0),             # Very high P_min, premium floored
    (144.0, 1.5, 10.0, max((144.0 * 1.5) / 12, 10.0)),

    # Edge cases for E_loss
    (0.0001, 1.5, 5.0, max((0.0001 * 1.5)/12, 5.0)),    # Very small positive expected loss
    (1e9, 1.0, 1000000.0, max((1e9 * 1.0)/12, 1000000.0)), # Very large expected loss

    # Edge cases for loading_factor
    (1000.0, 0.0001, 20.0, max((1000.0 * 0.0001)/12, 20.0)), # Very small loading factor
    (1000.0, 1e6, 2000.0, max((1000.0 * 1e6)/12, 2000.0)),   # Very large loading factor

    # Edge cases for P_min
    (1000.0, 1.0, 0.0, max((1000.0 * 1.0)/12, 0.0)),
    (1000.0, 1.0, -10.0, max((1000.0 * 1.0)/12, -10.0)),     # Negative P_min (should not happen, test robustness)
])
def test_calculate_monthly_premium(E_loss, loading_factor, P_min, expected):
    result = calculate_monthly_premium(E_loss, loading_factor, P_min)
    assert isinstance(result, float), "Result should be a float"
    # Since floating point math may cause minuscule differences, allow small tolerance
    assert abs(result - expected) < 1e-6

@pytest.mark.parametrize("E_loss, loading_factor, P_min", [
    # Invalid types
    ("1000.0", 1.5, 20.0),   # E_loss as string
    (1000.0, "1.5", 20.0),   # loading_factor as string
    (1000.0, 1.5, "20.0"),   # P_min as string
    ([1000.0], 1.5, 20.0),   # E_loss as list
    (1000.0, None, 20.0),    # loading_factor as None
    (None, 1.5, 20.0),       # E_loss as None
    (1000.0, 1.5, None),     # P_min as None
])
def test_calculate_monthly_premium_invalid_types(E_loss, loading_factor, P_min):
    with pytest.raises((TypeError, ValueError)):
        calculate_monthly_premium(E_loss, loading_factor, P_min)

@pytest.mark.parametrize("E_loss, loading_factor, P_min", [
    # Negative numeric inputs (assuming function should raise)
    (-1000.0, 1.5, 20.0),
    (1000.0, -1.5, 20.0),
    (1000.0, 1.5, -20.0),   # Already tested above but checking if error raised instead of silent flooring
])
def test_calculate_monthly_premium_negative_values(E_loss, loading_factor, P_min):
    with pytest.raises(ValueError):
        calculate_monthly_premium(E_loss, loading_factor, P_min)