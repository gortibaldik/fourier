import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def plot_recording_spectrum(freqs, absFreqSpectrum, name):

  plt.plot(freqs, absFreqSpectrum)

  # annotate the maximum
  ax = plt.gca()
  plot_most_significant_points(ax, freqs, absFreqSpectrum)

  # create plot
  plt.ylabel('|X(n)|')
  plt.xlabel('frequency[Hz]')
  plt.title(name)
  plt.show()

def plot_most_significant_points(ax, freqs, absFreqSpectrum):
  average = np.average(absFreqSpectrum)
  peaks, _ = find_peaks(absFreqSpectrum, height=2*average, distance=1000)

  for p in peaks:
    text = f"{int(freqs[p])}"
    kw = dict(xycoords='data', ha="left", va="top",
      xytext=(-10, 10), textcoords="offset points"
    )
    ax.annotate(text, xy=(freqs[p], absFreqSpectrum[p]), **kw)