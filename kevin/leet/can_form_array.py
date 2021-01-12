# https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3589/
from typing import List

class Solution:
    def can_form_array(self, arr: List[int], pieces: List[List[int]]) \
                       -> bool:
        # idea: start searching from beginning of arr
        # for each new subset, check if it exists in pieces
        # if it does, try it
        # could have to backtrack here though
        # distinct: all integers in pieces are distinct
        # and, there are exactly the number of unique integers that we need to fill arr
        # could map each element in arr to a piece index
        # then, check that the piece indices align?
        # let's do it
        
        # construct a map from integer to the piece index of that integer
        # we can do this since we know piece flattens to a set of integers
        piece_map = dict()
        for i, piece in enumerate(pieces):
            for item in piece:
                piece_map[item] = i
            
        # map each element in arr to its corresponding piece index
        # if you get a lookup error here, cannot do it
        piece_indices = []
        for item in arr:
            try:
                piece_indices.append(piece_map[item])
            except KeyError:
                return False
        
        # divide the piece indices into unique sublists of matching piece indices
        piece_indices_split = []
        current_sublist = [piece_indices[0]]
        for i in range(len(piece_indices) - 1):
            current_piece_index = piece_indices[i]
            next_piece_index = piece_indices[i + 1]
            if current_piece_index == next_piece_index:
                # add it to the current sublist
                current_sublist.append(next_piece_index)
            else:
                # flush the current sublist and reset
                piece_indices_split.append(current_sublist)
                current_sublist = [next_piece_index]
        
        # handle end case
        piece_indices_split.append(current_sublist)
        
        # first, check that our index sublists match the lengths we need
        for piece_index_sublist in piece_indices_split:
            piece_index = piece_index_sublist[0]
            if len(piece_index_sublist) != len(pieces[piece_index]):
                return False
        
        # finally, need to check that the ordering within pieces is actually correct
        # for each item in the array
        i = 0
        for piece_index_sublist in piece_indices_split:
            for j in range(len(piece_index_sublist)):
                piece_index = piece_index_sublist[0]
                piece_item = pieces[piece_index][j]
                if arr[i + j] != piece_item:
                    return False
            
            i += len(piece_index_sublist)
        
        return True
        
