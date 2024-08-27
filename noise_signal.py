import math
import random
import numpy as np

def generate_awgn_signal(desired_power, no_desired_samples):
  no_spectra = no_desired_samples

  if no_spectra % 2 != 0:
    raise ValueError("no_spectra must be odd because it must reflect a spectrum of even symmetry")

  noise_frequency_spectra_magnitude = math.sqrt(desired_power / no_spectra)

  noise_frequency_spectrum = [0] * no_spectra
  noise_frequency_spectrum[0] = 0 # Set DC Offset to 0

  # for AWGN, magnitude has to be kept constant. However, phases must be uniformly distrubed. If phases are constant, then the iFFT would give you Dirac's function instead (https://www.reddit.com/r/askscience/comments/6tedvr/comment/dlki29e/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) 
  # Additional, matching positive/negative frequency pairs must be conjugates of one another to ensure the combined frequency of these complex exponentials is real-valued
  for i in range(1, no_spectra // 2):
    random_complex_number = _generate_random_complex_number(noise_frequency_spectra_magnitude)
    noise_frequency_spectrum[i] = random_complex_number
    noise_frequency_spectrum[no_spectra - i] = random_complex_number.conjugate()
    
  time_domain_signal = np.fft.ifft(noise_frequency_spectrum)
  return np.real(time_domain_signal) # ifft result should be real-valued but taking the absolute here to take into account any 


def _generate_random_complex_number(desired_magnitude):
  real_component = 2 * desired_magnitude * random.random() - desired_magnitude # real_component range doubled to allow for negative real_component
  
  absolute_imaginary_component = math.sqrt(desired_magnitude ** 2 - real_component ** 2)
  should_imaginary_component_be_negative = bool(random.getrandbits(1))
  imaginary_component = absolute_imaginary_component * (-1 if should_imaginary_component_be_negative else 1)

  return complex(real=real_component, imag=imaginary_component)