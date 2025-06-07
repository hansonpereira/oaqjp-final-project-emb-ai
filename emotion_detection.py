import json
import requests

def emotion_detector(text_to_analyze):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Set the headers with the required model ID for the API
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Create the payload with the text to be analyzed
    myobj = {"raw_document": { "text": text_to_analyze} }


    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Return response
    return response.text  # This returns the response content as a string
