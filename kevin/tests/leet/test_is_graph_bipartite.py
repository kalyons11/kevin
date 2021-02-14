"""
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3639/
"""

from unittest import TestCase

from kevin.leet.is_graph_bipartite import Solution


class TestIsGraphBipartite(TestCase):
    def _base_test_is_graph_bipartite(self, graph, expected):
        sol = Solution()
        actual = sol.is_bipartite(graph)
        assert expected == actual, (expected, actual)

    def test_is_graph_bipartite_small_no(self):
        graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
        expected = False
        self._base_test_is_graph_bipartite(graph, expected)

    def test_is_graph_bipartite_small_yes(self):
        graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
        expected = True
        self._base_test_is_graph_bipartite(graph, expected)

    def test_is_graph_bipartite_big_no_disconnected(self):
        graph = [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9],
                [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9], [2, 4, 5, 6, 7,
                8]]
        expected = False
        self._base_test_is_graph_bipartite(graph, expected)

    def test_is_graph_bipartite_medium_yes_disconnected(self):
        graph = [[4], [], [4], [4], [0, 2, 3]]
        expected = True
        self._base_test_is_graph_bipartite(graph, expected)
