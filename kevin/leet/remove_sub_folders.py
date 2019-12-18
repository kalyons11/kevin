# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution:

    def remove_sub_folders(self, folder):
        # Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing.
        # If a folder[i] is located within another folder[j], it is called a sub-folder of it.
        # The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

        # Approach:
        # 0. Create root node, map from folder to leaf nodes
        root = FolderNode('/', False)
        current = root
        leaves = dict()

        # 1. Split all folders into their respective parts
        for fold in folder:
            # Go down the split parts and create nodes
            folder_list = self.__folder_to_list(fold)
            for i, subdir in enumerate(folder_list):
                is_leaf = i == len(folder_list) - 1
                current = current.add_child(subdir, is_leaf)

            # Map this folder to current node as leaf
            leaves[fold] = current

            # Reset current
            current = root

        result = list()

        # 2. Check all leaves to see if any parents are also folders
        for fold, leaf in leaves.items():
            ignore = False
            parent = leaf.get_parent()
            while parent is not None:
                if parent.is_leaf():
                    # Do not include - simply break and ignore
                    ignore = True
                    break

                # Update parent
                parent = parent.get_parent()

            if not ignore:
                result.append(fold)

        return result

    def __folder_to_list(self, folder):
        # Split a path name into individual directory names
        parts = folder.split('/')

        # Remove empty strings
        return list(filter(lambda part: part != '', parts))

class FolderNode:
    def __init__(self, name, is_leaf, parent=None):
        self.__name = name
        self.__is_leaf = is_leaf
        self.__parent = parent
        self.__children = dict()

    def add_child(self, child_name, is_leaf):
        if child_name in self.__children:
            result = self.__children[child_name]
            if is_leaf:
                result.make_leaf()
            return result

        self.__children[child_name] = FolderNode(child_name, is_leaf, self)
        return self.__children[child_name]

    def make_leaf(self):
        self.__is_leaf = True

    def __str__(self):
        return self._str_helper(0)

    def _str_helper(self, depth):
        result = depth * '-'
        result += self.__name + (' *' if self.__is_leaf else '') + '\n'

        for child in self.__children.values():
            result += child._str_helper(depth + 1)

        return result

    def is_leaf(self):
        return self.__is_leaf

    def get_parent(self):
        return self.__parent
