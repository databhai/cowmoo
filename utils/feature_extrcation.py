import os
import pandas as pd
import numpy as np
from os import listdir
from os.path import join
from pathlib import Path
from typing import Union, List
from librosa.feature import zero_crossing_rate, rms, mfcc, spectral_centroid, spectral_rolloff, spectral_bandwidth
from config import path_config, audio_config, feature_config
from compute import load_audio



def extract_feature(audio_data:np.ndarray, \
                    sample_rate:int=audio_config['sample_rate'], \
                    hop_length:int=audio_config['hop_length'], \
                    n_mfcc = audio_config['n_mfcc'])->np.ndarray:
    '''
    exctracts features from audio files
    '''
    zcr_feat = zero_crossing_rate(y=audio_data, hop_length=hop_length)
    rms_feat = rms(y=audio_data, hop_length=hop_length)
    mfcc_feat = mfcc(y=audio_data, sr=sample_rate, n_mfcc=n_mfcc, hop_length=hop_length)
    spectral_centroid_feat = spectral_centroid(y=audio_data, sr=sample_rate, hop_length=hop_length)
    spectral_rolloff_feat = spectral_rolloff(y=audio_data, sr=sample_rate, hop_length=hop_length)
    spectral_bandwidth_feat = spectral_bandwidth(y=audio_data, sr=sample_rate, hop_length=hop_length)
    concat_feat = np.concatenate((zcr_feat,
                                    rms_feat,
                                    mfcc_feat,
                                    spectral_centroid_feat,
                                    spectral_rolloff_feat,
                                    spectral_bandwidth_feat
                                    ), axis=0)                            
    mean_feat = np.mean(concat_feat, axis=1, keepdims=True).transpose()
    return mean_feat  


def load_audio_extract_feat(file:Union[str,Path])->np.ndarray:
    y, sr = load_audio(file)
    mean_feat = extract_feature(audio_data=y, sample_rate=sr)
    return mean_feat


def create_feat_label(dir_path:Union[str,Path],\
                        columns_list:List[str],\
                        label:str)->pd.DataFrame:
    '''
    crates a dataset of extracted features from all files along with the labels from a dir of files
    '''
    
    feat_df = pd.DataFrame(np.concatenate([load_audio_extract_feat(join(dir_path,file)) for file in listdir(dir_path) \
            if file.endswith('.wav')]), columns = columns_list)
    feat_df['label'] = label
    return feat_df


def create_feature_set(data_dir:Union[str,Path] = path_config['data'],\
                        data_dir_list:List[str]= path_config['train_data_dir_list'],\
                        colmuns:List[str] = feature_config['feature_columns'])->pd.DataFrame:
    '''
    creates feature set dataframe combining feature and labels from all files from all folders
    '''
    feature_set = pd.concat([create_feat_label(dir_path=os.path.join(data_dir,dir), columns_list=colmuns, label=dir) for dir in data_dir_list])
    return feature_set
