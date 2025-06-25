import pytest
from definition_83f3f3f5b1764ff8aba0aa4b7f12bbaf import calculate_expected_loss

@pytest.mark.parametrize(
    "P_claim, L_payout, expected",
    [
        # Typical valid cases
        (0.0, 0.0, 0.0),
        (0.0, 10000.0, 0.0),
        (0.5, 10000.0, 5000.0),
        (1.0, 10000.0, 10000.0),
        (0.1, 1234.56, 123.456),
        (0.9999, 100.0, 99.99),

        # Edge cases for P_claim (probability bounds)
        (0.0, 50000.0, 0.0),
        (1.0, 50000.0, 50000.0),

        # Edge cases for L_payout (zero or very low payout)
        (0.5, 0.0, 0.0),
        (0.5, 1e-10, 0.5e-10),

        # Testing with floats close to zero
        (1e-9, 10000.0, 1e-5),
        (0.75, 1e-9, 7.5e-10),

        # Large values
        (0.8, 1e9, 8e8),

        # Invalid inputs that should raise errors:
        # Negative probability (invalid)
        ( -0.1, 10000.0, ValueError),

        # Probability greater than 1 (invalid)
        (1.1, 10000.0, ValueError),

        # Negative payout (invalid)
        (0.5, -1000.0, ValueError),

        # Non-numeric types
        ("0.5", 10000.0, TypeError),
        (0.5, "10000", TypeError),

        # None inputs
        (None, 10000.0, TypeError),
        (0.5, None, TypeError),

        # Completely wrong types
        ([], {}, TypeError),
    ]
)
def test_calculate_expected_loss(P_claim, L_payout, expected):
    try:
        result = calculate_expected_loss(P_claim, L_payout)
        if isinstance(expected, type) and issubclass(expected, Exception):
            pytest.fail(f"Expected exception {expected} but got result {result}")
        else:
            # Allow slight float precision variance
            assert abs(result - expected) < 1e-6
    except Exception as e:
        assert isinstance(e, expected)
