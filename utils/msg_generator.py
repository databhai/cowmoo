

def generate_message(result:dict)->str:
    if result['class'] not in ['hamba', 'cow']:
        msg = (f"That wasn't great! Your hamba score is {result['score']:.2%}. You can do better. try again!")
    elif result['class'] == 'cow' and result['probability'] > 0.7: 
        msg = f"Hmmm! Is there a real cow in the room? Your hamba score is {result['score']*.5:.2%}" 
    elif result['class'] == 'cow' and result['probability'] < 0.7:
        msg = f"Wow! good job! your hamba score is : {result['score'] * 1.2 if result['score']<=.65 else 1:.2%}"
    elif result['class'] == 'hamba' and result['probability'] > 0.7 and result['score'] <= 0.6:
        msg = f"Wow! good job! your hamba score is : {result['score'] * 1.5 if result['score']<=.65 else 1:.2%}"
    else:
        msg = f"Nice work! your hamba score is : {result['score']:.2%}"
    return msg