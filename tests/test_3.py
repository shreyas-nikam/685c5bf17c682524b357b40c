import pytest
from definition_fc3da2f6720c4b24bb7e3f8262f427c5 import calculate_idiosyncratic_risk

@pytest.mark.parametrize(
    "FHC, FCR, FUS, w_CR, w_US, expected",
    [
        # Normal cases with typical float inputs
        (1.0, 1.0, 1.0, 0.4, 0.6, 50.0),  # Vraw = 1*(0.4*1 + 0.6*1) = 1.0; V = 50*1=50 clamp(5,100) -> 50
        (0.5, 0.8, 0.7, 0.4, 0.6, 50.0*0.5*(0.4*0.8 + 0.6*0.7)),
        (2.0, 1.0, 0.0, 0.5, 0.5, 100.0),  # Vraw=2*(0.5*1 +0.5*0)=1.0; V=50*1=50 < 100
        (10.0, 5.0, 1.0, 0.4, 0.6, 100.0),  # large numbers clipped to 100
        # Boundary values for weights summing to arbitrary values
        (1.0, 1.0, 1.0, 0.0, 1.0, 50.0),  # only w_US weight
        (1.0, 1.0, 1.0, 1.0, 0.0, 50.0),  # only w_CR weight
        # Test with zero and negative weights (should still compute but may produce unexpected, test coverage)
        (1.0, 1.0, 1.0, 0.0, 0.0, 5.0),  # Vraw=0 -> clamp to 5
        (1.0, 1.0, 1.0, -0.5, 1.0, 5.0), # negative weight reduces risk, but clamp applies
        # Test edge values for factors (minimum zero and max plausibles)
        (0.0, 0.0, 0.0, 0.4, 0.6, 5.0),
        (100.0, 100.0, 100.0, 0.4, 0.6, 100.0),
    ],
)
def test_calculate_idiosyncratic_risk(FHC, FCR, FUS, w_CR, w_US, expected):
    result = calculate_idiosyncratic_risk(FHC, FCR, FUS, w_CR, w_US)
    # Because of multiplication and clipping, allow small float precision differences
    assert abs(result - expected) < 1e-6

@pytest.mark.parametrize(
    "inputs",
    [
        # Non-float inputs for FHC
        ("string", 1.0, 1.0, 0.4, 0.6),
        (None, 1.0, 1.0, 0.4, 0.6),
        ([], 1.0, 1.0, 0.4, 0.6),
        # Non-float inputs for FCR
        (1.0, "string", 1.0, 0.4, 0.6),
        (1.0, None, 1.0, 0.4, 0.6),
        (1.0, [], 1.0, 0.4, 0.6),
        # Non-float inputs for FUS
        (1.0, 1.0, "string", 0.4, 0.6),
        (1.0, 1.0, None, 0.4, 0.6),
        (1.0, 1.0, [], 0.4, 0.6),
        # Non-float inputs for weights
        (1.0, 1.0, 1.0, "0.4", 0.6),
        (1.0, 1.0, 1.0, 0.4, "0.6"),
        (1.0, 1.0, 1.0, None, 0.6),
        (1.0, 1.0, 1.0, 0.4, None),
        # None for all
        (None, None, None, None, None),
    ],
)
def test_calculate_idiosyncratic_risk_invalid_types(inputs):
    FHC, FCR, FUS, w_CR, w_US = inputs
    with pytest.raises((TypeError, ValueError)):
        calculate_idiosyncratic_risk(FHC, FCR, FUS, w_CR, w_US)

@pytest.mark.parametrize(
    "FHC, FCR, FUS, w_CR, w_US",
    [
        # Edge cases for weights that do not sum to 1: function should accept and compute
        (1.0, 1.0, 1.0, 0.0, 0.0),
        (1.0, 1.0, 1.0, -1.0, 2.0),
        (1.0, 1.0, 1.0, 1.5, 1.5),
    ]
)
def test_calculate_idiosyncratic_risk_weights_edge(FHC, FCR, FUS, w_CR, w_US):
    # The function should compute without error, applying formula and clipping result
    result = calculate_idiosyncratic_risk(FHC, FCR, FUS, w_CR, w_US)
    assert isinstance(result, float)
    assert 5.0 <= result <= 100.0

