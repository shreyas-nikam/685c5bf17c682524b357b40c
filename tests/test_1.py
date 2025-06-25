import pytest
from definition_1b6d8b7ac6894bc384a8273623aba765 import calculate_fcr

@pytest.mark.parametrize("S_senti, S_fin, S_growth, w_1, w_2, w_3, expected", [
    # Typical cases
    (0.5, 0.7, 0.9, 0.3, 0.4, 0.3, 0.5*0.3 + 0.7*0.4 + 0.9*0.3),
    (1.0, 1.0, 1.0, 0.2, 0.3, 0.5, 1.0*0.2 + 1.0*0.3 + 1.0*0.5),
    (0.0, 0.0, 0.0, 0.4, 0.4, 0.2, 0.0),
    
    # Weights sum > 1 but function is linear sum; should still compute sum
    (0.4, 0.6, 0.8, 0.5, 0.5, 0.5, 0.4*0.5 + 0.6*0.5 + 0.8*0.5),

    # Weights sum < 1
    (0.5, 0.4, 0.1, 0.2, 0.3, 0.1, 0.5*0.2 + 0.4*0.3 + 0.1*0.1),

    # Negative values for scores (should be handled - either accepted or error)
    (-0.1, 0.5, 0.5, 0.3, 0.3, 0.4, -0.1*0.3 + 0.5*0.3 + 0.5*0.4),

    # Negative weights (likely invalid but test handling)
    (0.5, 0.5, 0.5, -0.3, 0.3, 0.3, 0.5*(-0.3) + 0.5*0.3 + 0.5*0.3),

    # Zero weights (result should be zero)
    (0.8, 0.7, 0.6, 0, 0, 0, 0.0),

    # Large weights and scores
    (100, 200, 300, 0.1, 0.2, 0.3, 100*0.1 + 200*0.2 + 300*0.3),

    # Non-float inputs should raise TypeError
    ("0.5", 0.7, 0.9, 0.3, 0.4, 0.3, TypeError),
    (0.5, "0.7", 0.9, 0.3, 0.4, 0.3, TypeError),
    (0.5, 0.7, "0.9", 0.3, 0.4, 0.3, TypeError),
    (0.5, 0.7, 0.9, "0.3", 0.4, 0.3, TypeError),
    (0.5, 0.7, 0.9, 0.3, "0.4", 0.3, TypeError),
    (0.5, 0.7, 0.9, 0.3, 0.4, "0.3", TypeError),

    # None inputs should raise TypeError or ValueError
    (None, 0.7, 0.9, 0.3, 0.4, 0.3, TypeError),
    (0.5, None, 0.9, 0.3, 0.4, 0.3, TypeError),
    (0.5, 0.7, None, 0.3, 0.4, 0.3, TypeError),
    (0.5, 0.7, 0.9, None, 0.4, 0.3, TypeError),
    (0.5, 0.7, 0.9, 0.3, None, 0.3, TypeError),
    (0.5, 0.7, 0.9, 0.3, 0.4, None, TypeError),
])
def test_calculate_fcr(S_senti, S_fin, S_growth, w_1, w_2, w_3, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calculate_fcr(S_senti, S_fin, S_growth, w_1, w_2, w_3)
    else:
        result = calculate_fcr(S_senti, S_fin, S_growth, w_1, w_2, w_3)
        assert isinstance(result, float) or isinstance(result, int)
        # Allow floating point small differences
        assert abs(result - expected) < 1e-7

