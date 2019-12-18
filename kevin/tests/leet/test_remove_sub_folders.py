"""
LeetCode remove sub folders test script.
"""

from unittest import TestCase

from kevin.leet import remove_sub_folders


class TestRemoveSubFolders(TestCase):

    def _validate_folder(self, expected, actual):
        # Validate that expected folder set equals actual folder set.
        assert set(expected) == set(actual)

    def test_remove_subfolders_easy(self):
        inp = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
        expected = ["/a", "/c/d", "/c/f"]
        sol = remove_sub_folders.Solution()
        actual = sol.remove_sub_folders(inp)
        self._validate_folder(expected, actual)

    def test_remove_subfolders_medium(self):
        inp = ["/a", "/a/b/c", "/a/b/d"]
        expected = ["/a"]
        sol = remove_sub_folders.Solution()
        actual = sol.remove_sub_folders(inp)
        self._validate_folder(expected, actual)

    def test_remove_subfolders_hard(self):
        inp = ["/a/b/c", "/a/b/ca", "/a/b/d"]
        expected = ["/a/b/c", "/a/b/ca", "/a/b/d"]
        sol = remove_sub_folders.Solution()
        actual = sol.remove_sub_folders(inp)
        self._validate_folder(expected, actual)

    def test_remove_subfolders_order(self):
        inp = ["/ah/al/am", "/ah/al"]
        expected = ["/ah/al"]
        sol = remove_sub_folders.Solution()
        actual = sol.remove_sub_folders(inp)
        self._validate_folder(expected, actual)
