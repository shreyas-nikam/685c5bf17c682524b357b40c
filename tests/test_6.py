import pytest
from definition_e0f519145a154e4ca8d0d7dcbc9f798c import calculate_systematic_risk

@pytest.mark.parametrize("H_base_t, w_econ, M_econ, w_inno, I_AI, expected", [
    # Normal cases
    (50.0, 0.5, 1.0, 0.5, 1.0, 50.0 * (0.5*1.0 + 0.5*1.0)),      # equal weights, neutral modifiers
    (40.0, 0.8, 0.9, 0.2, 1.1, 40.0 * (0.8*0.9 + 0.2*1.1)),      # weights sum to 1, modifiers within expected ranges
    (30.5, 0.3, 1.2, 0.7, 0.8, 30.5 * (0.3*1.2 + 0.7*0.8)),

    # Weights at extremes (all on one)
    (25.0, 1.0, 1.1, 0.0, 1.5, 25.0 * (1.0*1.1 + 0.0*1.5)),
    (25.0, 0.0, 1.1, 1.0, 1.5, 25.0 * (0.0*1.1 + 1.0*1.5)),

    # Edge economic / innovation modifiers
    (60.0, 0.6, 0.0, 0.4, 0.0, 60.0 * (0.6*0.0 + 0.4*0.0)),      # zero modifiers
    (60.0, 0.6, -0.5, 0.4, 2.0, 60.0 * (0.6*(-0.5) + 0.4*2.0)),  # negative econ modifier, valid though unusual
    (60.0, 0.6, 1.5, 0.4, -1.0, 60.0 * (0.6*1.5 + 0.4*(-1.0))),  # negative innovation index

    # H_base_t zero or negative
    (0.0, 0.5, 1.0, 0.5, 1.0, 0.0),
    (-10.0, 0.5, 1.0, 0.5, 1.0, -10.0 * (0.5*1.0 + 0.5*1.0)),

    # Weights don't sum to 1 (should still compute linearly)
    (50.0, 0.7, 1.0, 0.4, 1.0, 50.0 * (0.7*1.0 + 0.4*1.0)),
    (50.0, -0.5, 1.0, 1.6, 1.0, 50.0 * (-0.5*1.0 + 1.6*1.0)),

    # Types and invalid inputs
    ("50", 0.5, 1.0, 0.5, 1.0, TypeError),            # H_base_t as string
    (50.0, "0.5", 1.0, 0.5, 1.0, TypeError),          # w_econ as string
    (50.0, 0.5, "1.0", 0.5, 1.0, TypeError),          # M_econ as string
    (50.0, 0.5, 1.0, "0.5", 1.0, TypeError),          # w_inno as string
    (50.0, 0.5, 1.0, 0.5, "1.0", TypeError),          # I_AI as string
    (None, 0.5, 1.0, 0.5, 1.0, TypeError),            # H_base_t is None
    (50.0, None, 1.0, 0.5, 1.0, TypeError),           # w_econ is None
    (50.0, 0.5, None, 0.5, 1.0, TypeError),           # M_econ is None
    (50.0, 0.5, 1.0, None, 1.0, TypeError),           # w_inno is None
    (50.0, 0.5, 1.0, 0.5, None, TypeError),           # I_AI is None

    # Values out of typical ranges but float
    (50.0, -1.0, 2.0, 1.5, -3.0, 50.0 * (-1.0*2.0 + 1.5*(-3.0))),
])
def test_calculate_systematic_risk(H_base_t, w_econ, M_econ, w_inno, I_AI, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calculate_systematic_risk(H_base_t, w_econ, M_econ, w_inno, I_AI)
    else:
        result = calculate_systematic_risk(H_base_t, w_econ, M_econ, w_inno, I_AI)
        # Allow slight float precision tolerance
        assert abs(result - expected) < 1e-7

