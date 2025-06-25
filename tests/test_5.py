import pytest
from definition_a8a6403e9cfb4bb08822a8048c4c6ae3 import calculate_h_base

@pytest.mark.parametrize(
    "k, TTV, H_current, H_target, expected",
    [
        # Normal cases, k in [0, TTV]
        (0, 12, 50.0, 30.0, 50.0),              # k=0, expect H_current
        (6, 12, 50.0, 30.0, 40.0),              # midpoint, average of H_current and H_target
        (12, 12, 50.0, 30.0, 30.0),             # k=TTV, expect H_target
        (3, 12, 100.0, 80.0, 95.0),             # quarter way
        (9, 12, 10.0, 20.0, 17.5),              # three quarters

        # Edge cases: k greater than TTV, should clamp or behave gracefully
        (13, 12, 50.0, 30.0, 30.0),             # k > TTV, treated as k=TTV (assumption)
        (100, 100, 40.0, 60.0, 60.0),           # k = TTV large
        (101, 100, 40.0, 60.0, 60.0),           # k > TTV large

        # Edge case: k negative, should clamp at 0 (assumption)
        (-1, 12, 50.0, 30.0, 50.0),

        # Edge case: TTV = 0 (division by zero avoided?), expect return H_current or error
        (0, 0, 50.0, 30.0, 50.0),                # TTV=0 means immediate transition?
        (5, 0, 50.0, 30.0, 50.0),

        # Edge case: float inputs (should be cast or raise error)
        (6.5, 12.0, 50.0, 30.0, 44.583333333333336), # (1 - 6.5/12)*50 + (6.5/12)*30

        # Edge case: inputs as string (expect TypeError)
        pytest.param("6", 12, 50.0, 30.0, TypeError, marks=pytest.mark.xfail(raises=TypeError)),
        pytest.param(6, "12", 50.0, 30.0, TypeError, marks=pytest.mark.xfail(raises=TypeError)),
        pytest.param(6, 12, "50", 30.0, TypeError, marks=pytest.mark.xfail(raises=TypeError)),
        pytest.param(6, 12, 50.0, "30", TypeError, marks=pytest.mark.xfail(raises=TypeError)),

        # Edge case: None inputs (expect TypeError)
        pytest.param(None, 12, 50.0, 30.0, TypeError, marks=pytest.mark.xfail(raises=TypeError)),
        pytest.param(6, None, 50.0, 30.0, TypeError, marks=pytest.mark.xfail(raises=TypeError)),
        pytest.param(6, 12, None, 30.0, TypeError, marks=pytest.mark.xfail(raises=TypeError)),
        pytest.param(6, 12, 50.0, None, TypeError, marks=pytest.mark.xfail(raises=TypeError)),

        # Edge case: TTV negative (invalid), expect ValueError or handle gracefully
        pytest.param(6, -12, 50.0, 30.0, ValueError, marks=pytest.mark.xfail(raises=ValueError)),
        pytest.param(0, -1, 50.0, 30.0, ValueError, marks=pytest.mark.xfail(raises=ValueError)),

        # Edge case: H_current/H_target negative hazard (possible? expect normal calculation or error)
        (6, 12, -50.0, 30.0, -10.0),
        (6, 12, 50.0, -30.0, 10.0),
    ],
)
def test_calculate_h_base(k, TTV, H_current, H_target, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calculate_h_base(k, TTV, H_current, H_target)
    else:
        result = calculate_h_base(k, TTV, H_current, H_target)
        # Use approx for float comparisons
        assert result == pytest.approx(expected, rel=1e-9)
