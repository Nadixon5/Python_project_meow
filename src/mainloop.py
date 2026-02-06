from src.askers import ask_path_filedialog
from src.audiodata import AudioData

def mainloop_fun():
    audio_file_path = ask_path_filedialog()
    loaded_data = AudioData(audio_file_path)
    print("ŚCIEŻKA MIMIMIMI:", loaded_data.audio_file_path)
    print("Sample rate:", loaded_data.samplerate)
    print("Próbki:", loaded_data.data_array)
    print("Długość:", len(loaded_data.data_array))
    loaded_data.draw_tone()
    while True:
        print("MEOW")
        print("KOKO")
        break
