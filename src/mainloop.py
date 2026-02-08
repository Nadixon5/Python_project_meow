from src.askers import ask_path_filedialog, ask_main_menu
from src.audiodata import AudioData

def mainloop_fun():
    audio_file_path = ask_path_filedialog()
    if not audio_file_path:
        print("No file has been chosen :(\n")
        return

    loaded_data = AudioData(audio_file_path)
    print("ŚCIEŻKA    :", loaded_data.audio_file_path)
    print("Sample rate:", loaded_data.samplerate)
    print("Próbki:     ", loaded_data.data_array)
    print("Długość:    ", len(loaded_data.data_array))
    print()
    # loaded_data.show_chart()
    while True:
        asker = ask_main_menu()

        if asker == "chart":
            loaded_data.show_chart()
            print("\n")

        elif asker == "spectrogram":
            loaded_data.show_spectrogram()
            print("\n")

        elif asker == "low-pass_filter":
            loaded_data.apply_lowpass()
            print("\n")

        elif asker == "high-pass_filter":
            loaded_data.apply_hipass()
            print("\n")

        elif asker == "fast_fourier_transform":
            loaded_data.fast_fourier()
            print("\n")

        elif asker == "save_as_file":
            loaded_data.save_audio()
            print("\n")

        elif asker == "quit":
            return
