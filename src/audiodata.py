import librosa
import numpy

class AudioData:
    #inicjlizacja
    def __init__(self, audio_file_path):
        self.audio_file_path = audio_file_path
        self.data_array, self.samplerate = librosa.load(audio_file_path, sr=None, mono=True)
        