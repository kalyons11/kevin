"""
Utils test script.
"""

from unittest import TestCase

import kevin.utils


class TestUtils(TestCase):
    def _test_string_method(self):
        x = 'Test-string123__:'
        y = kevin.utils.strip_str(x)
        assert y == 'teststring123'

    def test_iter_method(self):
        x = 'omg'
        x_new, result = kevin.utils.validate_iter(x)
        print(x_new)
        # assert not result
