import os
from tkinter import filedialog


def ask_path_filedialog():
    #Otwarcie okienka
    sel_path = filedialog.askopenfilename(
        title="Choose a txt or csv file", #tekst na górze
        filetypes=[       #dozwolone rodzaje plików
            ("MP3 or FLAC files", "*.mp3 *.flac")])

    return sel_path
