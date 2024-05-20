"""
feature_functions.py

Feature functions

Authors:    Jeroen Veen
            Hugo Arends
Date:       October 2023

Copyright:  2023 HAN University of Applied Sciences. All Rights Reserved.
"""
import sys
from os.path import join, dirname, realpath
sys.path.append(join(dirname(realpath(__file__)), '..', '..'))

import config as cfg
import ctypes
from os.path import join, isfile
import feature_functions_c2dll

FEATURES_DLL = join(cfg.PREPROCESSING_FEATURES_DIR_PATH, 'features.dll')

def check_features_dll():
    """
    Create the feature functions dll as soon as needed
    """
    if not isfile(FEATURES_DLL):
        feature_functions_c2dll.main()

def min(data):
    """
    Python wrapper for the feature calculation functions that are also used on
    the microcontroller. Refer to the C-source files for documentation.
    """
    check_features_dll()
    c_lib = ctypes.CDLL(FEATURES_DLL)

    c_lib.min.restype = ctypes.c_float
    n = len(data)
    x = (ctypes.c_float * n)(*data)
    return c_lib.min(ctypes.byref(x), n)

def max(data):
    """
    Python wrapper for the feature calculation functions that are also used on
    the microcontroller. Refer to the C-source files for documentation.
    """
    check_features_dll()
    c_lib = ctypes.CDLL(FEATURES_DLL)

    c_lib.max.restype = ctypes.c_float
    n = len(data)
    x = (ctypes.c_float * n)(*data)
    return c_lib.max(ctypes.byref(x), n)

def mean(data):
    """
    Python wrapper for the feature calculation functions that are also used on
    the microcontroller. Refer to the C-source files for documentation.
    """
    check_features_dll()
    c_lib = ctypes.CDLL(FEATURES_DLL)

    c_lib.mean.restype = ctypes.c_float
    n = len(data)
    x = (ctypes.c_float * n)(*data)
    return c_lib.mean(ctypes.byref(x), n)

def variance(data):
    """
    Python wrapper for the feature calculation functions that are also used on
    the microcontroller. Refer to the C-source files for documentation.
    """
    check_features_dll()
    c_lib = ctypes.CDLL(FEATURES_DLL)

    c_lib.variance.restype = ctypes.c_float
    n = len(data)
    x = (ctypes.c_float * n)(*data)
    return c_lib.variance(ctypes.byref(x), n)

def energy(data):
    """
    Python wrapper for the feature calculation functions that are also used on
    the microcontroller. Refer to the C-source files for documentation.
    """
    check_features_dll()
    c_lib = ctypes.CDLL(FEATURES_DLL)

    c_lib.energy.restype = ctypes.c_float
    n = len(data)
    x = (ctypes.c_float * n)(*data)
    return c_lib.energy(ctypes.byref(x), n)

def peak_to_peak(data):
    """
    Python wrapper for the feature calculation functions that are also used on
    the microcontroller. Refer to the C-source files for documentation.
    """
    check_features_dll()
    c_lib = ctypes.CDLL(FEATURES_DLL)

    c_lib.peak_to_peak.restype = ctypes.c_float
    n = len(data)
    x = (ctypes.c_float * n)(*data)
    return c_lib.peak_to_peak(ctypes.byref(x), n)

def raw(data, n=None):
    """
    Returns the first raw sample in the array

    Mainly used for testing purpose. With a block_size of 1, this feature should
    return the same raw input data.
    """
    return data[0] if (len(data) > 0) else None

def find_crossings(data):
    """
    Python wrapper for the find_crossings function from the features DLL. This function
    identifies threshold crossings in the input data array based on a predefined threshold.

    :param data: List or array of float data representing the signal.
    :return: The count of threshold crossings detected in the data.
    """
    check_features_dll()
    c_lib = ctypes.CDLL(FEATURES_DLL)

    c_lib.find_crossings.restype = ctypes.c_uint32
    c_lib.find_crossings.argtypes = [
        ctypes.POINTER(ctypes.c_float),  
        ctypes.c_uint32,                
    ]

    n = len(data)
    x = (ctypes.c_float * n)(*data)

    num_crossings = c_lib.find_crossings(x, ctypes.c_uint32(n))

    return num_crossings

def frequency(data, sampling_rate):
    """
    Calculates the frequency of threshold crossings in the data.

    This function counts the number of times the signal crosses a specified threshold within a given data chunk,
    then uses the sampling rate to determine the frequency of these crossings in Hz, assuming that crossings
    are reset for each chunk.

    :param data: List or array of float data representing the signal.
    :param sampling_rate: The number of samples per second.
    :return: The frequency of the threshold crossings in Hz.
    """
    check_features_dll()
    c_lib = ctypes.CDLL(FEATURES_DLL)

    c_lib.find_crossings.restype = ctypes.c_uint32
    c_lib.find_crossings.argtypes = [
        ctypes.POINTER(ctypes.c_float),  
        ctypes.c_uint32,                 
    ]

    n = len(data)
    x = (ctypes.c_float * n)(*data)

    # Get the number of crossings
    num_crossings = c_lib.find_crossings(x, ctypes.c_uint32(n))

    # Time duration for the data chunk in seconds
    time_duration = n / sampling_rate

    # Calculate the frequency of crossings
    if time_duration > 0:
        frequency = num_crossings / time_duration
    else:
        frequency = 0

    return frequency
