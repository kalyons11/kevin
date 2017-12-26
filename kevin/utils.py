"""
Quick package utils script.
"""

import numpy as np


def strip_str(inp):
    """Helper method to strip a string of all non alphanumeric characters.

    Args:
        inp (str): -

    Returns:
        str: stripped output

    >>> x = 'Test-string123__:'
    >>> y = strip_str(x)
    >>> y
    'teststring123'
    """

    return ''.join(ch.lower() for ch in inp if ch.isalnum())


def validate_iter(obj):
    """Helper method to validate that an object is at least a list
        or np.ndarray.

    Args:
        obj (unknown): any input

    Returns:
        2-tuple: iterable version of obj and bool indicator of whether
            or not obj was already an iterable
    """
    if isinstance(obj, (list, np.ndarray)):
        return obj, True

    return [obj], False


def reshape_image(img, data_format='channels_last'):
    """Helper method to reshape a 3D image/4D batch of images into the correct
    format. Assumes square image input size on at least 2 axes.

    Args:
        img (np.ndarray or list[np.ndarray]): image input
        data_format (str, optional): following keras specification

    Returns:
        object: either list or np.ndarray with correct output format
    """
    def internal_reshape_3d(mat, data_format):
        """Internal method to reshape a 3D matrix.

        Args:
            mat (np.ndarray): 3D numpy array, for sure
        """
        # Parse shape
        assert mat.ndim == 3, mat.ndim
        one, two, three = mat.shape

        if data_format == 'channels_last':
            # tf ordering - (h, w, c)
            if one == two:
                return mat
            else:
                # was (c, h, w)
                mat_new = np.swapaxes(mat, 0, 2)  # (w, h, c)
                mat_new = np.swapaxes(mat_new, 0, 1)  # (h, w, c)
                return mat_new

        elif data_format == 'channels_first':
            # th ordering - (c, h, w)
            if two == three:
                return mat
            else:
                # was (h, w, c)
                mat_new = np.swapaxes(mat, 0, 2)  # (c, w, h)
                mat_new = np.swapaxes(mat_new, 1, 2)  # (c, h, w)
                return mat_new

    def internal_reshape_alld(mat, data_format):
        """Internal method to reshape a matrix of any shape.

        Args:
            mat (np.ndarray): -
            data_format (str): -

        Returns:
            np.ndarray: correct output shape

        Raises:
            NotImplementedError: for invalid input type
        """
        if mat.ndim == 4:
            # Batch case
            batches_new = [internal_reshape_3d(img, data_format) for img in mat]
            batches_new = np.array(batches_new)
            return batches_new
        elif mat.ndim == 3:
            # Simple case
            return internal_reshape_3d(mat, data_format)
        elif mat.ndim == 2:
            # One slice - expand
            mat_expanded = np.expand_dims(mat, axis=-1)
            return internal_reshape_3d(mat_expanded, data_format)
        else:
            raise NotImplementedError(
                "Image shape ndim must be in range [2, 4].")

    # Validate inputs
    assert data_format in {'channels_first', 'channels_last'}, \
        'Invalid data_format param {}.".format(data_format)'

    # Figure out input type
    if isinstance(img, list):
        # Apply to each element in list
        return [internal_reshape_alld(mat, data_format) for mat in img]

    elif isinstance(img, np.ndarray):
        # Just this one matrix
        return internal_reshape_alld(img, data_format)

    else:
        raise NotImplementedError("Invalid img input type!")
