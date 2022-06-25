import os
from os import listdir
from os.path import isfile
from pathlib import Path
from os import listdir


def get_project_root() -> Path:
    return Path(__file__).parent.parent

ROOT_DIR = get_project_root()

DATA_DIR = os.path.join(ROOT_DIR, 'data')
TRAIN_DATA_DIR = os.path.join(DATA_DIR, 'train')
TRAIN_DATA_DIR_LIST = [dir for dir in listdir(TRAIN_DATA_DIR) if not isfile(dir)]
BENCHMARK_DIR = os.path.join(DATA_DIR, 'benchmark')
TEST_DIR = os.path.join(DATA_DIR, 'test')
INPUT_DIR = os.path.join(DATA_DIR, 'input')
LOG_DIR = os.path.join(ROOT_DIR, 'logs')
MODEL_DIR = os.path.join(ROOT_DIR, 'model')
OUT_DIR = os.path.join(ROOT_DIR, 'output')
IMAGE_DIR = os.path.join(OUT_DIR, 'images')


path_config = {'data':DATA_DIR,
                'train_data_dir':TRAIN_DATA_DIR,
                'train_data_dir_list':TRAIN_DATA_DIR_LIST,
                'benchmark':BENCHMARK_DIR,
                'test':TEST_DIR,
                'input':INPUT_DIR,
                'log':LOG_DIR,
                'model':MODEL_DIR,
                'out':OUT_DIR,
                'image':IMAGE_DIR
                }

data_path_config = {f'{dir}': os.path.join(DATA_DIR, dir) for dir in TRAIN_DATA_DIR_LIST}


# Audio configurations

SAMPLE_RATE = 44100 #22050
OFFSET = .1    #.1 second  
DURATION = 4   # 3 seconds
HOP_LENGTH = 512
N_FMCC = 13
CHUNK_SIZE = 1024
INPUT_DEVICE = 0
MAX_INPUT_CHANNELS = 1  

audio_config = {
    'sample_rate': SAMPLE_RATE,
    'offset': OFFSET,
    'duration': DURATION,
    'hop_length': HOP_LENGTH,
    'n_mfcc': N_FMCC,
    'chunk_size': CHUNK_SIZE,
    'input_device': INPUT_DEVICE,
    'input_channel':MAX_INPUT_CHANNELS
    }

# features
FEATURE_COLUMNS = ['zcr', 'rms_energy',\
           'mfcc0', 'mfcc1', 'mfcc2', 'mfcc3', 'mfcc4', 'mfcc5', 'mfcc6', 'mfcc7', 'mfcc8', 'mfcc9', 'mfcc10', 'mfcc11',\
           'mfcc12', 'sp_centroid', 'sp_rolloff', 'sp_bw']

feature_config = {'feature_columns' : FEATURE_COLUMNS}
=======
# LOG_CONFIG = os.path.join(ROOT_DIR, 'logging.yml')
# print(LOG_CONFIG)

# DATA_DIR = os.path.join(ROOT_DIR, 'data')
# DATA_DIR_AUDIO = os.path.join(DATA_DIR, 'audio')
# DATA_DIR_GUITAR = os.path.join(DATA_DIR_AUDIO, 'Guitar_Only/')
# DATA_DIR_AUGMENTED = os.path.join(DATA_DIR_AUDIO, 'augmented')

# METADATA_DIR = os.path.join(DATA_DIR, 'metadata')
# METADATA_DIR_RAW = os.path.join(METADATA_DIR, 'raw')
# METADATA_DIR_PROCESSED = os.path.join(METADATA_DIR, 'processed')

# METADATA_DIR_AUGMENTED = os.path.join(METADATA_DIR, 'augmented')
# METADATA_DIR_AUGMENTED_RAW = os.path.join(METADATA_DIR_AUGMENTED, 'raw')
# METADATA_DIR_AUGMENTED_PROCESSED = os.path.join(METADATA_DIR_AUGMENTED, 'processed')

# LOG_DIR = os.path.join(ROOT_DIR, 'logs')
# LOG_DIR_TRAINING = os.path.join(LOG_DIR, 'training')



# WAVE_OUTPUT_FILE = os.path.join(RECORDING_DIR, "recorded.wav")
# SPECTROGRAM_FILE = os.path.join(RECORDING_DIR, "spectrogram.png")

# # Features


# # Audio configurations
# INPUT_DEVICE = 0
# MAX_INPUT_CHANNELS = 1  # Max input channels
# DEFAULT_SAMPLE_RATE = 44100   # Default sample rate of microphone or recording device
# DURATION = 3   # 3 seconds
# CHUNK_SIZE = 1024
