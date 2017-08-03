"""
Utils test script.
"""

from unittest import TestCase

import numpy as np

import kevin.utils


class TestUtils(TestCase):
    def test_string_method(self):
        x = 'Test-string123__:'
        y = kevin.utils.strip_str(x)
        assert y == 'teststring123'

    def test_iter_method(self):
        x = 'omg'
        x_new, result = kevin.utils.validate_iter(x)
        assert not result

    def test_reshape_func_easy(self):
        inp = np.random.rand(3, 512, 512)
        out = kevin.utils.reshape_image(inp)
        assert out.shape == (512, 512, 3)

    def test_reshape_func_easy2(self):
        inp = np.random.rand(512, 512, 3)
        out = kevin.utils.reshape_image(inp, data_format='channels_first')
        assert out.shape == (3, 512, 512), out.shape

    def test_reshape_func_med(self):
        inp = np.random.rand(100, 3, 512, 512)
        out = kevin.utils.reshape_image(inp, data_format='channels_last')
        assert out.shape == (100, 512, 512, 3), out.shape

    def test_reshape_func_med2(self):
        inp = np.random.rand(100, 512, 512, 3)
        out = kevin.utils.reshape_image(inp, data_format='channels_first')
        assert out.shape == (100, 3, 512, 512), out.shape

    def test_reshape_func_hard(self):
        inp = [np.random.rand(3, 512, 512) for _ in range(3)]
        out = kevin.utils.reshape_image(inp, data_format='channels_last')
        assert isinstance(out, list)
        assert all(res.shape == (512, 512, 3) for res in out)

    def test_reshape_func_hard2(self):
        inp = [np.random.rand(512, 512, 3) for _ in range(3)]
        out = kevin.utils.reshape_image(inp, data_format='channels_first')
        assert isinstance(out, list)
        assert all(res.shape == (3, 512, 512) for res in out)

    def test_reshape_func_crazy(self):
        inp = [np.random.rand(10, 3, 512, 512) for _ in range(3)]
        out = kevin.utils.reshape_image(inp, data_format='channels_last')
        assert isinstance(out, list)
        assert all(res.shape == (10, 512, 512, 3) for res in out)

    def test_reshape_func_crazy2(self):
        inp = [np.random.rand(10, 512, 512, 3) for _ in range(3)]
        out = kevin.utils.reshape_image(inp, data_format='channels_first')
        assert isinstance(out, list)
        assert all(res.shape == (10, 3, 512, 512) for res in out)
