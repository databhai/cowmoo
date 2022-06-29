
import os
from pathlib import Path
from os import listdir
from os.path import isfile, join
from typing import List, Union

from config import path_config

def load_sound_file(file_type:str)->List[Union[str, Path]]:
    filelist = [join(path_config[file_type], f) for f in listdir(path_config[file_type]) if f.endswith('.wav')]
    return filelist


from pydub import AudioSegment

def ogg2wav(ofn):
    wfn = ofn.replace('.ogg','.wav')
    x = AudioSegment.from_file(ofn)
    x.export(wfn, format='wav')



def mp3_to_wav(mp3_file):
    wav_file_name = mp3_file.replace('.mp3','.wav')
    conversion = AudioSegment.from_mp3(mp3_file)
    conversion.export(wav_file_name, format='wav')

def flac_to_wav(flac_file):
    wav_file_name = flac_file.replace('.flac','.wav')
    conversion = AudioSegment.from_file(flac_file)
    conversion.export(wav_file_name, format='wav')

def convert_audio_to_wav(DATA_DIR, format):
    for file in listdir(DATA_DIR):
        file = join(DATA_DIR, file)
        if file.endswith(format):
            if format == '.mp3':
                mp3_to_wav(file)
                os.remove(file)
            elif format == '.flac':
                flac_to_wav(file)
                os.remove(file)
            elif format == '.ogg':
                flac_to_wav(file)
                os.remove(file)
            else:
                print('unknown format')
