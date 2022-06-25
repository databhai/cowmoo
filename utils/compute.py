from logging import warning
import warnings
import numpy as np
import librosa as lr
from pathlib import Path
from dtw import dtw
from typing import Any, Union, List
from config import audio_config

warnings.filterwarnings('ignore')

def load_audio(path:Union[str,Path], \
                sample_rate:int=audio_config['sample_rate'],\
                offset:float=audio_config['offset'],\
                duration:float=audio_config['duration']):
    '''loading the audio clip as floating point time series
    args:
        path: path to the sound clip, can be either str or a path object
        sr: sample rate
        offset: loading after offset seconds
        duration: only load up to certain duration in secords
    returns:
        y : np.ndarray [shape=(n,) or (…, n)]
        s : '''
    y, s = lr.load(path)
    return y, s

def compute(path:Union[str,Path])->np.ndarray:
    y, sr = load_audio(path)
    mfcc_coef = lr.feature.mfcc(y=y, sr=sr)
    return mfcc_coef

def compare(mfcc1:np.ndarray, mfcc2:np.ndarray)->Any:
    output =  dtw(mfcc1.T, mfcc2.T)
    output =  round(output.normalizedDistance,2)
    return output


def score(input_file:Union[str, Path], benchmark_file_paths:List[Union[str,Path]])->float:
    input_mfcc = compute(input_file)
    score = 0
    for benchmark_file in benchmark_file_paths:
        benchmark_mfcc = compute(benchmark_file)
        output = compare(benchmark_mfcc, input_mfcc)
        score = output if output > score else score
    return score


def normalise_score(score:float, top_range:float=200)->float:
    final_score = round((top_range - score) /top_range,2)
    return final_score