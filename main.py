
from argparse import ArgumentParser
from sklearn.tree import DecisionTreeClassifier
from utils.config import path_config
from utils.files import load_sound_file
from utils.compute import score, normalise_score


#input file 
# collect input file detail 
# load input file
# extract feature
# score -> predict
# apply filtering 
# compute DTW score
# Make Decision


def main()->float:
    input_file_path = load_sound_file('input')
    input_file_path = input_file_path[0]
    raw_score = score(input_file_path, path_config['benchmark'])
    final_score = normalise_score(raw_score)
    print(f'Your hamba match is {final_score:.2%}')
    return final_score

if __name__ == '__main__':
    main()
