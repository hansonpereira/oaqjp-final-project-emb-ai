from flask import Flask, render_template, request
import json
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app O
app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET"])
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detection function and store the response
    response = json.loads(emotion_detector(text_to_analyze))
    # Extract the label and score from the response
    dominant_emotion =  response["dominant_emotion"]
    response.pop("dominant_emotion")

    formatted = str(response).replace('{','').replace('}','')
    return f"For the given statement, the system response is {formatted}. The dominant emotion is <strong>{dominant_emotion}</strong>."



@app.route("/")
def render_index_page():
    """
     This is a default route to run index page
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
