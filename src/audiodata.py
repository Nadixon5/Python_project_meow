import librosa
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from datetime import datetime
from pathlib import Path
import scipy
from scipy.signal import butter, firwin, filtfilt
import os

plt.rcParams.update({
    "font.size": 14,
    "axes.titlesize": 18,
    "axes.labelsize": 16,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    "legend.fontsize": 14
})



class AudioData:
    audio_file_path: str #ścieżka do pliku
    data_array: np.ndarray #numpy.klasa(lepszy array)
    samplerate: int 

    #inicjlizacja (kiedy tworzysz instancję klasy) trzeba.
    def __init__(self, audio_file_path):
        self.audio_file_path = audio_file_path#argument
        #ładowanie ze ścieżki zmiennych ładowanych z pliku
        self.data_array, self.samplerate = librosa.load(audio_file_path, sr=None, mono=False)


    def fast_fourier(self):
        return


    # ========================= FILTERS =========================
    # cutoff - frequencies below cutoff pass for low-pass filters
    # cutoff - frequencies above cutoff pass for high-pass filters
    #
    # nyq (Nyquist frequency) - Half the sampling rate. A digital 
    # signal cannot represent frequencies ≥ samplerate/2.
    #
    # order (Butterworth)- The steepness of the transition band for filter.
    # Higher order means sharper cutoff and better frequency separation
    #
    # numtaps (FIR) - The number of filter coefficients (length of 
    # the impulse response). Higher numtaps is sharper cutoff, 
    # narrower transition band but higher CPU cost.


    def apply_lowpass_butterworth(self):
        cutoff = 3000
        order = 5
        nyq = 0.5 * self.samplerate

        norm_cutoff = cutoff / nyq
        b, a = butter(order, norm_cutoff, btype='low')

        self.data_array[0] = filtfilt(b, a, self.data_array[0])
        self.data_array[1] = filtfilt(b, a, self.data_array[1])


    def apply_lowpass_fir(self):
        cutoff = 3000
        numtaps = 401
        nyq = 0.5 * self.samplerate

        taps = firwin(
            numtaps=numtaps,
            cutoff=cutoff / nyq,
            window="hamming",
            pass_zero="lowpass")

        self.data_array[0] = filtfilt(taps, [1.0], self.data_array[0])
        self.data_array[1] = filtfilt(taps, [1.0], self.data_array[1])


    def apply_hipass_butterworth(self):
        cutoff = 200
        order = 5
        nyq = 0.5 * self.samplerate

        norm_cutoff = cutoff / nyq
        b, a = butter(order, norm_cutoff, btype='high')

        self.data_array[0] = filtfilt(b, a, self.data_array[0])
        self.data_array[1] = filtfilt(b, a, self.data_array[1])


    def apply_hipass_fir(self):
        cutoff = 200
        numtaps = 401
        nyq = 0.5 * self.samplerate

        taps = firwin(
            numtaps=numtaps,
            cutoff=cutoff / nyq,
            window="hamming",
            pass_zero="highpass")

        self.data_array[0] = filtfilt(taps, [1.0], self.data_array[0])
        self.data_array[1] = filtfilt(taps, [1.0], self.data_array[1])


    def show_spectrogram(self):
        # Dane zostały spreparowane do spektrogramu za pomocą scipy, a 
        # zobrazowane na wykresie używając matplotliba. Dzieje się tak, 
        # ponieważ plt.specgram nie radzi sobie z 0, z których próbuje 
        # obliczyć logarytm o podstawie 10.
        nperseg = 1024

        freq_bins_l, time_bins_l, left_spectr = scipy.signal.spectrogram(
            self.data_array[0],
            fs = self.samplerate,
            nperseg = nperseg,        # Każda pionowa kreska/wartość/nie wiem
                                      # spektrogramu wynosi nperseg próbek.
                                      # Im większe - mniejsza dokładność spek.
                                      # Im mniejsze - większa dokładność spek.
                                      # Uśrednia 1024 próbek
            noverlap = nperseg // 2,  # Określa nakładanie się na siebie
                                      # pionowych wartości. Im więcej tym gładsze
            scaling = 'density')
        freq_bins_r, time_bins_r, right_spectr = scipy.signal.spectrogram(
            self.data_array[1],
            fs = self.samplerate,
            nperseg = nperseg,
            noverlap = nperseg // 2,
            scaling = 'density')

        left_spectr_compressed  = 10 * np.log10(left_spectr + 1e-12)
        right_spectr_compressed = 10 * np.log10(right_spectr + 1e-12)


        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
        axes[0].pcolormesh(time_bins_l, freq_bins_l, left_spectr_compressed,  shading='auto')
        axes[0].set_title("Left speaker")
        axes[0].set_xlabel("Time [s]")
        axes[0].set_ylabel("Frequency [Hz]")

        axes[1].pcolormesh(time_bins_r, freq_bins_r, right_spectr_compressed, shading='auto')
        axes[1].set_title("Right speaker")
        axes[1].set_xlabel("Time [s]")
        axes[1].set_ylabel("Frequency [Hz]")

        plt.tight_layout()
        plt.show()
        return


    def show_chart(self):
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

        axes[0].plot(self.data_array[0])
        axes[0].set_title("Left speaker")
        axes[0].set_xlabel("Sample")
        axes[0].set_ylabel("Amplitude")

        axes[1].plot(self.data_array[1])
        axes[1].set_title("Right speaker")
        axes[1].set_xlabel("Sample")
        axes[1].set_ylabel("Amplitude")

        plt.tight_layout()
        plt.show()


    def save_audio(self):
        # do plików mieć konkretny czas w nazwie (żeby inne były)
        currtime = datetime.now()
        currtime_string = currtime.strftime("%Y-%m-%d_%H-%M-%S")

        filename = Path(self.audio_file_path).stem
        project_path = Path(__file__).resolve().parent.parent
        os.chdir(project_path) #przejście do katalogu projektu

        # zapis jako plik FLAC
        sf.write(
            f"output/{filename}_{currtime_string}.flac",
            self.data_array.T,
            self.samplerate,
            format="FLAC",
            subtype="PCM_16") # or PCM_24 or PCM_32
