from tkinter import filedialog

def ask_path_filedialog():
    #Otwarcie okienka
    sel_path = filedialog.askopenfilename(
        title="Choose a txt or csv file", #tekst na górze
        filetypes=[       #dozwolone rodzaje plików
            ("MP3 or FLAC files", "*.mp3 *.flac")])

    return sel_path

#sło(w)(n)ik
def ask_settings_type():
    returns_dict = {#dict-dictionary!
        "c": "chart",
        "s": "spectrogram",
        "l": "low-pass_filter",
        "h": "high-pass_filter",
        "f": "fast_fourier_transform",
        "q": "quit"}

    while True:
        print("Choose settings type (type 'q' to quit):\n"
                "c - Show data on chart\n"
                "s - Show data by means of spectrogram\n"
                "l - Low-pass filter\n"
                "h - High-pass filter\n"
                "f - Show data by means of fast fourier transform\\n>> ", end="")
        asker = input().strip().lower() #strip - zbędne spacje usuwa, lower - zamienia duże litery na małe

        if asker not in returns_dict:
            print("Invalid input :(\n")
        else:
            return returns_dict[asker]
