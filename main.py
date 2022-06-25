from os.path import join
import pandas as pd
from argparse import ArgumentParser
from utils.config import path_config, feature_config
from pycaret.classification import load_model, predict_model
from utils.feature_extrcation import load_audio_extract_feat
from utils.files import load_sound_file
from utils.compute import score, normalise_score
from utils.msg_generator import generate_msg


model = load_model(join(path_config['model'],'model'))

def main()->float:
    input_file_path = load_sound_file('input')
    input_file_path = input_file_path[0]
    features = load_audio_extract_feat(input_file_path)
    features = pd.DataFrame(features, columns = feature_config['feature_columns'])
    raw_score = score(input_file_path, path_config['benchmark_file_list'])
    prediction = predict_model(model, data = features)
    final_score = normalise_score(raw_score)
    result = {'class' : prediction.Label[0], 'probability' : prediction.Score[0], 'score' : final_score}
    print(generate_msg(result))
    return result

if __name__ == '__main__':
    main()
