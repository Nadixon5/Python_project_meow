from tkinter import filedialog

def ask_path_filedialog():
    #Otwarcie okienka
    sel_path = filedialog.askopenfilename(
        title="Choose a txt or csv file", #tekst na górze
        filetypes=[       #dozwolone rodzaje plików
            ("Audio files", "*.mp3 *.flac *.ogg *.wav")])

    return sel_path


#sło(w)(n)ik
def ask_main_menu():
    returns_dict = {#dict-dictionary!
        "c": "chart",
        "s": "spectrogram",
        "f": "filters",
        "t": "fast_fourier_transform",
        "v": "save_as_file",
        "q": "quit"}

    while True:
        print("Choose settings type (type 'q' to quit):\n"
              "c - Show data on chart\n"
              "s - Show data by means of spectrogram\n"
              "f - Filters...\n"
              "t - Show data by means of Fast Fourier Transform\n"
              "v - Save as audio file\n>> ", end="")
        asker = input().strip().lower() #strip - zbędne spacje usuwa, lower - zamienia duże litery na małe

        if asker not in returns_dict:
            print("Invalid input :(\n")
        else:
            return returns_dict[asker]


def ask_filters():
    # FIR - Finite Impulse Response
    returns_dict = {
        "lb": "low_pass_butterworth",
        "lf": "low_pass_fir",
        "rb": "high_pass_butterworth",
        "rf": "high_pass_fir",
        "r":  "return"}

    while True:
        print("Choose filter to apply (type 'r' to return):\n"
              "lb - Apply low-pass Butterworth filter\n"
              "lf - Apply low-pass linear FIR filter\n"
              "rb - Apply high-pass Butterworth filter\n"
              "rf - Apply high-pass linear FIR filter\n>> ", end="")
        asker = input().strip().lower() #strip - zbędne spacje usuwa, lower - zamienia duże litery na małe

        if asker not in returns_dict:
            print("Invalid input :(\n")
        else:
            return returns_dict[asker]


def ask_cutoff(filter_type):
    default_cutoff = None
    if filter_type == "low":
        default_cutoff = 3000
    elif filter_type == "high":
        default_cutoff = 200

    while True:
        print("Pick a new cutoff value:\n"
             f"Leave empty for default val {default_cutoff}\n"
              "(type 'r' to return)\n>> ", end="")
        asker = input().strip().lower()

        if asker == "r":
            return
        elif asker == "":
            return default_cutoff
        elif not asker.isdigit():
            print("Invalid value.\n\n")
            continue

        asker_num = int(asker)
        if asker_num < 3:
            print("Input value is too low.\n\n")
        elif asker_num > 17000:
            print("Input value is too high.\n\n")
        else:
            return asker_num
