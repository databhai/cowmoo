
from pathlib import Path
from collections import OrderedDict
from itertools import islice
from typing import Union
from pyAudioAnalysis import audioTrainTest as aT

# from feature_extrcation import load_audio_extract_feat
# from config import path_config, feature_config
# from pycaret.classification import load_model, predict_model

# def _predict_audio_class(input_file_path:Union[str,Path])->dict:
#     '''
#     predict the input audio class by passing the extracted features through the trained model
#     '''
#     features = load_audio_extract_feat(input_file_path)
#     features = pd.DataFrame(features, columns = feature_config['feature_columns'])
#     model = load_model(join(path_config['model'], 'model'))
#     prediction = predict_model(model, data = features)
#     return {'class' : prediction.Label[0], 'probability' : prediction.Score[0]}



def predict_audio_class(input_file_path:Union[str,Path])->dict:
    _, probability_, class_ = aT.file_classification(input_file_path, "randForestV2","randomforest")
    result = {c:v for c, v in zip(class_, probability_.tolist())}
    result = OrderedDict(sorted(result.items(), key = lambda x: x[1], reverse = True))
    result = dict(islice(result.items(), 5))
    return result




def generate_message(prediction:dict):
    if max(list(prediction.values()))<0.55:
    # case when there is no strong prediction for any single class. This may mean that
    # - either the class was not in training samples
    # - or the audio input is of poor quality ot full of noise
        if 'Cow' not in prediction or 'Hamba' not in prediction:
        # no prediction for cow or hamba in top 5 means that
        # the input is either a bad attempt or some comeplete weird sound
            msg = f"That didn't sound like a cow! Do you want to try again? Make sure you speak clearly to the microphone."
        else:
        # No single strong class but either 'cow' or 'hamba' or both are in top 5
        # - perhaps a poor input and the model is struggling to predict
            msg = f"That wasn't great! Lets see your score!."
    elif max(list(prediction.values()))>0.55:
    # A single dominant class is predicted
    # - perhaps a really good attempt or an accidental match in aplitude, frqeuency, etc with a specific class
    # - or a pre-reocrded sound is played at imput
        if 'Cow' not in prediction or 'Hamba' not in prediction:
        # no prediction for cow or hamba in top 5 means that
        # the input is either accidentally turned out to be too good/similar to a class model was trained on
        # or someone is just playing with the model, not for winning, but perhaps for fun!
            msg = f" Ahemm, that sounded like a {[k for k, v in prediction.items() if v == max(list(prediction.values()))]}! Do you want to try again? Make sure you speak clearly to the microphone."
        elif prediction['Cow']>0.7 and 'Hamba' not in prediction:
        # strong fraud attempt   
            msg = f'Hmmm, is there a cow in the room?'
        elif prediction['Hamba']>0.7 and 'Cow' not in prediction:
        # As per moedel performance, this should be good but rather rare result
            msg = f'Sounds good! your score is being processed...'
        elif 'Cow' in prediction and 'Hamba' in prediction:
        # both cow and hamba are in top 5
        # - legit case, should be a good attempt. Further scoring for % match needed
            msg = f'Nice job! Your score is being processed...'  
    else:
        msg = f"Ooops that wasn't great! You should try again." 
    return msg
