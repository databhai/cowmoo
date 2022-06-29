import warnings
from itertools import islice
from argparse import ArgumentParser
from utils.config import path_config
from utils.files import load_sound_file
from utils.compute import score, normalise_score
from utils.predict import predict_audio_class
from utils.msg_generator import generate_msg

warnings.filterwarnings('ignore')


def main()->dict:
    input_file_path = load_sound_file('input')
    input_file_path = input_file_path[0]
    predcition = predict_audio_class(input_file_path)
    raw_score = score(input_file_path, path_config['benchmark_file_list'])
    final_score = normalise_score(raw_score)
    pred_ict = dict(islice(predcition.items(), 1))
    result = {'class' : list(pred_ict.keys())[0], 'probability' : list(pred_ict.values())[0], 'score' : final_score}
    print(generate_msg(predcition))
    return result

if __name__ == '__main__':
    main()
