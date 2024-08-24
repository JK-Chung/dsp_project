import numpy as np

"""
Calculates the required power in your noise in order to meet the provided SNR (in dBW)
"""
def calculate_noise_power_ratio(desired_snr_dbw):
  return 10 ** (-1 * desired_snr_dbw / 10)

"""
Takes in a 1D signal and returns its power
"""
def calculate_signal_power(one_dimenstional_signal):
  absolute_signal = np.abs(one_dimenstional_signal)
  absolute_power_samples = np.square(absolute_signal)
  return np.sum(absolute_power_samples)