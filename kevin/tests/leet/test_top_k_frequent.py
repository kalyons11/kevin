# LeetCode top k frequent test script.

from unittest import TestCase

from kevin.leet import top_k_frequent


class TestTopKFrequent(TestCase):

    def test_top_k_frequent_multi(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expected = [1, 2]
        sol = top_k_frequent.Solution()
        actual = sol.top_k_frequent(nums, k)
        assert expected == actual

    def test_top_k_frequent_single(self):
        nums = [1]
        k = 1
        expected = [1]
        sol = top_k_frequent.Solution()
        actual = sol.top_k_frequent(nums, k)
        assert expected == actual

    def test_top_k_frequent_neg_regression(self):
        nums = [4, 1, -1, 2, -1, 2, 3]
        k = 2
        expected = [-1, 2]
        sol = top_k_frequent.Solution()
        actual = sol.top_k_frequent(nums, k)
        assert expected == actual, actual
