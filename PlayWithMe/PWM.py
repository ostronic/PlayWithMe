#!/bin/ !python
#:  Title:  PlayWithMe(PWM) -Converts Video file(mainly from screen rec.) of playht to audio .wav file 
#:  Synopsis:   python PWM.py
#:  Date:   2025-02-28
#:  Version:    1.0
#:  Author: ostronics {fg_daemon}
#:  Options:    Enter file path or Folder/Directory path

from audio_extract import extract_audio

import os

ROOT = input("ENTER DIRECTORY/FOLDER PATH CONTAINING VIDEO FILE : ")
fmt = input("\nEnter output file format E.G: WAV, OGG, MP3, AAC, FLAC, M4A, OGA, OPUS:    ")
fmt.lower()

OUTROOT = "VOICE" + f"{fmt}"

def get_file(srcdir=ROOT, tgtdir=OUTROOT):
    for fnames in os.listdir():
        if not fnames.upper().endswith(('.wav','.mp3','.mp4', '.mkv', '.webm', '.mov')):
            continue
        doc_in = os.join(srcdir, fnames)
        global doc_out
        doc_out = tgtdir

        with open(doc_in) as f:
            if doc_in is None:
                print("There is no file is inputed Directory/Folder")
                continue
    vid_to_aud()

def vid_to_aud():
    extract_audio(input_path="{}".format(doc_in), output_path="{}".format(doc_out), duration=600.0) # 10mins max audio

if __name__ == '__main__':
    get_file()
# CLI command -  audio-extract --input="vokoscreenNG-2025-02-26_21-35-54.mp4" --output="extracted_audio.wav" --format="wav"

