import requests
import json
def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json= { "raw_document": { "text": text_to_analyze } }
    try:
        response = requests.post(url, headers=headers, json = input_json)
        response_dict = json.loads(response.text)

        if response.status_code == 200:
            anger_score = response_dict["emotionPredictions"][0]["emotion"]["anger"]
            disgust_score = response_dict["emotionPredictions"][0]["emotion"]["disgust"]
            fear_score = response_dict["emotionPredictions"][0]["emotion"]["fear"]
            joy_score = response_dict["emotionPredictions"][0]["emotion"]["joy"]
            sadness_score = response_dict["emotionPredictions"][0]["emotion"]["sadness"]

            emotions = {
                'anger' : anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
            }

            dominant_emotion = max(emotions, key= emotions.get)
            emotions['dominant_emotion'] = dominant_emotion
            return emotions 
        elif response.status.code == 400:
            emotions = {
                'anger' : None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
            return response.emotions
    except Exception as e:
            return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }