import librosa
import numpy as np

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


    def shpow_spectogram(self):
        return


    def show_chart(self):
        return
