import pandas as pd
from os.path import join
from pathlib import Path
from typing import Union
from feature_extrcation import load_audio_extract_feat
from config import path_config, feature_config
from pycaret.classification import load_model, predict_model

def predict_audio_class(input_file_path:Union[str,Path])->dict:
    '''
    predict the input audio class by passing the extracted features through the trained model
    '''
    features = load_audio_extract_feat(input_file_path)
    features = pd.DataFrame(features, columns = feature_config['feature_columns'])
    model = load_model(join(path_config['model'], 'model'))
    prediction = predict_model(model, data = features)
    return {'class' : prediction.Label[0], 'probability' : prediction.Score[0]}


