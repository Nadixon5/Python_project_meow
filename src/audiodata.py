import librosa
import numpy as np
import matplotlib.pyplot as plt
import scipy

plt.rcParams.update({
    "font.size": 14,
    "axes.titlesize": 18,
    "axes.labelsize": 16,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    "legend.fontsize": 14
})



class AudioData:
    audio_file_path: str
    data_array: np.ndarray
    samplerate: int

    #inicjlizacja
    def __init__(self, audio_file_path):
        self.audio_file_path = audio_file_path
        self.data_array, self.samplerate = librosa.load(audio_file_path, sr=None, mono=True)


    def fast_fourier(self):
        return


    def apply_lowpass(self):
        return


    def apply_hipass(self):
        return


    def show_spectrogram(self):
        # Dane zostały spreparowane do spektrogramu za pomocą scipy, a 
        # zobrazowane na wykresie używając matplotliba. Dzieje się tak, 
        # ponieważ plt.specgram nie radzi sobie z 0, z których próbuje 
        # obliczyć logarytm o podstawie 10.
        nperseg = 1024

        f, t, Sxx = scipy.signal.spectrogram(
            self.data_array,
            fs = self.samplerate,
            nperseg = nperseg,        # Każda pionowa kreska/wartość/nie wiem
                                      # spektrogramu wynosi nperseg próbek.
                                      # Im większe - mniejsza dokładność spek.
                                      # Im mniejsze - większa dokładność spek.
            noverlap = nperseg // 2,  # Określa zachodzenie na siebie pionowych
                                      # wartości. Im więcej tym gładsze
            scaling = 'density')
        Sxx_db = 10 * np.log10(Sxx + 1e-12)

        plt.figure(figsize=(8, 4))
        plt.pcolormesh(t, f, Sxx_db, shading='auto')
        plt.ylabel("Frequency [Hz]")
        plt.xlabel("Time [s]")
        plt.colorbar(label="Power (dB)")
        plt.tight_layout()
        plt.show()
        return


    def show_chart(self):
        plt.figure()
        plt.plot(self.data_array)
        plt.xlabel("Sample")
        plt.ylabel("Amplitude")
        plt.title("Soundwave")
        plt.show()
