"""
https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
"""

class Solution:

    def remove_sub_folders(self, folder):
        """
        Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing.

        If a folder[i] is located within another folder[j], it is called a sub-folder of it.

        The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.
        """
        # Approach:
        # 1. Split folders into their directories by path
        # 2. Create nodes for each folder, marking when a node is child
        # 3. Check when a parent node is a child - if so, remove that path?
        pass

