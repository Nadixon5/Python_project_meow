from src.askers import ask_path_filedialog, ask_main_menu, ask_filters
from src.audiodata import AudioData

def mainloop_fun():
    audio_file_path = ask_path_filedialog()
    if not audio_file_path:
        print("No file has been chosen :(\n")
        return

    loaded_data = AudioData(audio_file_path)

    while True:
        print("ŚCIEŻKA    :", loaded_data.audio_file_path)
        print("Sample rate:", loaded_data.samplerate)
        print("Długość:    ", len(loaded_data.data_array[0]))
        print()
        asker = ask_main_menu()

        if asker == "chart":
            loaded_data.show_chart()
            print("\n")

        elif asker == "spectrogram":
            loaded_data.show_spectrogram()
            print("\n")

        elif asker == "filters":
            while True:
                print("\n")
                asker = ask_filters()
                print()

                if asker == "low_pass_butterworth":
                    loaded_data.apply_lowpass_butterworth()
                    print("Filter successfully applied\n\n")

                elif asker == "low_pass_fir":
                    pass

                elif asker == "high_pass_butterworth":
                    loaded_data.apply_hipass_butterworth()
                    print("Filter successfully applied\n\n")

                elif asker == "high_pass_fir":
                    pass

                elif asker == "return":
                    break

        elif asker == "fast_fourier_transform":
            loaded_data.fast_fourier()
            print("\n")

        elif asker == "save_as_file":
            loaded_data.save_audio()
            print("File successfully saved\n\n")

        elif asker == "quit":
            print("Bye bye user...")
            return
