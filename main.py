import whisper

from tkinter import *
from tkinter import filedialog
import json


def info_audio():
    try:
        model = whisper.load_model("small")  # small.en (only en)
        song_path = filedialog.askopenfilename(title = "Select a File", 
                                                filetypes = (("Text files", 
                                                                "*.mp3*"), 
                                                            ("all files", 
                                                                "*.*")))

        result = model.transcribe(song_path)
        lyric = result["text"]

        with open("lyric.json", "w", encoding="utf-8") as f:
            json.dump(result,f, ensure_ascii=False, indent=4)

    except Exception as err:
        print(err)


def extract_speech():
    with open('lyric.json') as file:
        data = json.load(file)

    with open("extract_speech.txt","w", encoding="utf-8") as f:
        for row in data['segments']:
            text = row['text']

            f.writelines(text)
            f.writelines("\n\n")


def main():
    print("loading...")
    info_audio()
    extract_speech()

if __name__ == "__main__":
    main()