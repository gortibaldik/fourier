import numpy as np

from scipy.fft import fft

def get_spectrum(recording, sampleFreq): 
  absFreqSpectrum = np.abs(fft(recording))

  # from DFT index to frequency: index / total_samples * sample_freq
  freqs = np.array([i / len(absFreqSpectrum) * sampleFreq for i in range(sampleFreq // 2)])
  absFreqSpectrum = absFreqSpectrum[:sampleFreq // 2]
  return freqs, absFreqSpectrum

def hps(spectrum, R):
  hpsSpectrum = spectrum[:]
  for r in range(1, R):
    otherSpectrum = np.zeros(len(hpsSpectrum))
    ln = len(spectrum) // (r + 1)
    otherSpectrum[:ln] = spectrum[:ln]
    hpsSpectrum = np.multiply(hpsSpectrum, otherSpectrum)

  return hpsSpectrum