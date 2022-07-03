__all__ = ['predict_audio_class', 'process_score']

import random
from pathlib import Path
from collections import OrderedDict
from itertools import islice
from typing import Union
from pyAudioAnalysis import audioTrainTest as aT


def predict_audio_class(input_file_path:Union[str,Path])->OrderedDict:
    _, probability_, class_ = aT.file_classification(input_file_path, "randForestV2","randomforest")
    result = {c:v for c, v in zip(class_, probability_.tolist())}
    result = OrderedDict(sorted(result.items(), key = lambda x: x[1], reverse = True))
    result = dict(islice(result.items(), 5))
    return result


def process_score(prediction:dict)->str: 
    pred = dict(islice(prediction.items(), 1))
    try:
        if pred['Cow']<=0.1:
            score = 0.05
        elif pred['Cow']>0.1 and pred['Cow']<=0.2:
            score = pred['Cow'] + 0.1
        elif pred['Cow']>0.2 and pred['Cow']<=0.3:
            score = pred['Cow'] + 0.2
        elif pred['Cow']>0.3 and pred['Cow']<=0.4:
            score = pred['Cow'] + 0.25
        elif pred['Cow']>0.4 and pred['Cow']<=0.5:
            score = pred['Cow'] + 0.15
        elif pred['Cow']>0.5 and pred['Cow']<=0.65:
            score = pred['Cow'] + 0.1
        elif pred['Cow']>0.65:
            score = pred['Cow'] - 0.6
    except KeyError:
        score = round(random.uniform(0.08, 0.21),2)
    score = round(score, 2)
    msg = f'Your score is {score*100:.2f}%'
    result = {**pred, 'message':msg, 'score':score}
    return result  



def generate_message(prediction:dict, score:float)->str:
    if max(list(prediction.values()))<0.55:
    # case when there is no strong prediction for any single class. This may mean that
    # - either the class was not in training samples
    # - or the audio input is of poor quality ot full of noise
        if 'Cow' not in prediction and 'hamba' not in prediction:
        # no prediction for cow or hamba in top 5 means that
        # the input is either a bad attempt or some comeplete weird sound
            msg = f"That didn't sound like a cow! your score is {min(15, score*100*.6):.0f}%"
        elif 'Cow' in prediction and 'hamba' in prediction:
        # No single strong class but both 'cow' and 'hamba' in top 5
        # - perhaps a poor but cow-like input and the model is struggling to predict
            msg = f"That was okay..ish! your score is {max(55,score*100*1.3):.0f}%"
        elif 'Cow' in prediction and 'hamba' not in prediction:
        # No signle dominant class but 'cow' is in top 5 and 'hamba' is not
        # - perhaps a poor cow-like input but model did not detect human-like input
        # - or a poor pre-recorded sound is played at input
            msg = f'Sounds good like cow! your score is {max(20, score*100*1.2):.0f}%'
        elif 'Cow' not in prediction and 'hamba' in prediction:
        # No signle dominant class but 'hamba' is in top 5 and 'cow' is not
        # - perhaps a poor hamba-like input but no resemblence to cow
            msg = f'Sounds good like hamba! your score is {max(50, score*100*1.2):.0f}%'
        else:
            msg = f"something is not right - admins will look at it - Level-BL1-Score {score*100:.0f}%"
    elif max(list(prediction.values()))>=0.55:
    # A single dominant class is predicted
    # - perhaps a really good attempt or an accidental match in aplitude, frqeuency, etc with a specific class
    # - or a pre-reocrded sound is played at input
        if 'Cow' not in prediction and 'hamba' not in prediction:
        # no prediction for cow and hamba in top 5 means that
        # the input is either accidentally turned out to be too good/similar to a class model was trained on
        # or someone is just playing with the model, not for winning, but perhaps for fun!
            msg = f" Ahemm, that sounded like a {[k for k, v in prediction.items() if v == max(list(prediction.values()))][0]}! Make sure you speak clearly to the microphone. By the way your score is {min(15, score*100*.9):.0f}%"
        elif 'Cow' in prediction and 'hamba' in prediction:
        # both cow and hamba are in top 5
        # - legit case, should be a good attempt. Further scoring for % match needed
            msg = f'Nice job! your score is {max(60, score*100*1.3):.0f}%'
        elif 'Cow' in prediction and 'hamba' not in prediction: 
        # either 'cow' or 'hamba' is in top 5 but not both
            if prediction['Cow']>0.7:
            # strong fraud attempt  - reduce score by 50%
                msg = f'Hmmm, is there a cow in the room? By the way your score is {min(10,score*100*.5):.0f}%'
        elif 'Cow' not in prediction and 'hamba' in prediction:
            if prediction['hamba']>0.7:
            # As per moedel performance, this should be good but rather rare result
                msg = f'Sounds good! your score is {max(60, score*100*1.2):.0f}%'
            else:
                msg = f'Nice job! your score is {max(50, score*100*1.2):.0f}%'
        else: #
            msg = f'something is not right - admins will look at it - Level-BL2-Score {max(50, score*100*1.2):.0f}%'
    else:
        msg = f"somethinig is not right - admins will look at it - Level-Def-Score {score*100:.0f}%"
    return msg