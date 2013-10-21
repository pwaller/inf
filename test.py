# Because infinity needs testing.

from nose.tools import (raises, assert_equal)

import inf

@raises(ZeroDivisionError)
def test_infdiv_zero_zero():
    inf.div(0.0, 0.0)

def test_infdiv_normal():
    cases = [(1.0, 2.0, 0.5),
             (0.0, 2.0, 0.0),
             (1, 2, 0.5),
             (0, 2, 0.0)]

    def one(p, q, expected):
        assert_equal(inf.div(p, q), expected)

    for p, q, expected in cases:
        yield one, p, q, expected

def test_infdiv_infinity():
    cases = [
        (1.0, 0.0, inf),
        (-1.0, 0.0, -inf),
        (-1.0, -0.0, inf),
        (1.0, -0.0, -inf),
    ]

    def one(p, q, expected):
        assert_equal(inf.div(p, q), expected)

    for p, q, expected in cases:
        yield one, p, q, expected
