'''
helper functions for the main code in project_codes.py
example_function() illustrates the structure of a numpy docstring
moving_average() illustrates a specific case of a numpy docstring
'''
import numpy as np

def example_function():
    '''
    One line description of the function.

    Detailed description of the function.
    
    Parameters
    -----
    None.

    Returns
    -------
    None.

    Raises
    ------
    None.

    Examples
    --------
    >>> example_function()
    
    Notes
    -----
    None.
    '''
    print('example function')
    return None

def moving_average(data, window_size):
    """
    Compute the moving average of a 1D array using a specified window size.

    Parameters
    ----------
    data : array_like
        Input array containing numerical data.
    window_size : int
        The size of the moving average window. Must be a positive integer.

    Returns
    -------
    numpy.ndarray
        An array containing the moving average of the input data.

    Raises
    ------
    ValueError
        If `window_size` is not a positive integer or greater than the length of `data`.

    Examples
    --------
    >>> import numpy as np
    >>> data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    >>> moving_average(data, 3)
    array([2., 3., 4., 5., 6., 7., 8., 9.])

    Notes
    -----
    This function uses `numpy.convolve` with a uniform kernel to compute the moving average.
    """
    if not isinstance(window_size, int) or window_size <= 0:
        raise ValueError("window_size must be a positive integer.")
    if window_size > len(data):
        raise ValueError("window_size must be smaller than or equal to the length of data.")

    kernel = np.ones(window_size) / window_size
    return np.convolve(data, kernel, mode='valid')