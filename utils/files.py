
import os
from pathlib import Path
from os import listdir
from os.path import isfile, join
from typing import List, Union

from config import path_config

def load_sound_file(file_type:str)->List[Union[str, Path]]:
    filelist = [join(path_config[file_type], f) for f in listdir(path_config[file_type]) if isfile(join(path_config[file_type], f))]
    return filelist


from pydub import AudioSegment

def ogg2wav(ofn):
    wfn = ofn.replace('.ogg','.wav')
    x = AudioSegment.from_file(ofn)
    x.export(wfn, format='wav')


DATA_DIR = 'data/train'
data_dir_list = ['dog', 'other', 'hamba', 'glass', 'snoring', 'horn', 'baby', 'cow', 'cat', 'birds', 'church', 'siren', 'storm']

#convert ogg to wav and delete ogg file
def convert_ogg_wav():
    for dir in data_dir_list:
        for file in listdir(join(DATA_DIR, dir)):
            file = join(DATA_DIR, dir, file)
            if file.endswith('.ogg'):
                ogg2wav(file)
            if file.endswith('.ogg'):
                os.remove(file)
