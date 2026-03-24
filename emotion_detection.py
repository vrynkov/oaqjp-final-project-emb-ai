import json
import requests


def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input =  {"raw_document": { "text": text_to_analyze}}
    response = requests.post(URL, json = input, headers=header)
    formatted_response = json.loads(response.text)

    emotions = formatted_response['emotionPredictions'][0]['emotion']
    emotions_dict = {}
    dominant_emotion, dominant_emotion_val = 'anger', emotions['anger']

    for emotion in emotions:
        if emotions[emotion] > dominant_emotion_val:
             dominant_emotion, dominant_emotion_val = emotion, emotions[emotion]

        emotions_dict[emotion] = emotions[emotion] 
        
    emotions_dict['dominant_emotion'] = dominant_emotion

    return emotions_dict