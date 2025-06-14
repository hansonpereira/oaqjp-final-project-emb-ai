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

    if (response.status_code == 400):
        output = {
            'anger': None, 'disgust': None,'fear': None,
            'joy': None,'sadness': None,
            'dominant_emotion': None
            }
        return json.dumps(output, indent=4, sort_keys=False)

    formatted_response = json.loads(response.text)
    # Parse the response from the API
    formatted_response = json.loads(response.text)
    output = formatted_response["emotionPredictions"][0]["emotion"]

    #sort to find dominent name
    numeric_items = {k: v for k, v in output.items() if isinstance(v, (int, float))}
    sorted_data = dict(sorted(numeric_items.items(), key=lambda item: item[1], reverse=True))
    dominent_name = list(sorted_data.keys())[0]
    output.update({"dominant_emotion": dominent_name})
    pretty_output = json.dumps(output, indent=4, sort_keys=False)
    return pretty_output