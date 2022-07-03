import warnings
from itertools import islice
from argparse import ArgumentParser
from utils.config import path_config
from utils.files import load_sound_file
from utils.predict import predict_audio_class, process_score

warnings.filterwarnings('ignore')


def main()->dict:
    input_file_path = load_sound_file('input')
    input_file_path = input_file_path[0]
    prediction = predict_audio_class(input_file_path)
    result = process_score(prediction=prediction)
    print(result['message'])
    return result

if __name__ == '__main__':
    main()
