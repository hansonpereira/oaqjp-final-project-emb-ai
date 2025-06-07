from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app O
app = Flask("Emotion Detector")


@app.route("/emotionDetector", methods=["GET"])
def sent_analyzer():
    """
    Endpoint to perform emotionDetector on the provided input text.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detection function and store the response
    response = emotion_detection(text_to_analyze)

    # Extract the label and score from the response
    label = response['label']
    score = response['score']

    # Check if the label is None, indicating an error or invalid input
    if label is None:
        return "Invalid input! Try again."
    # Return a formatted string with the sentiment label and score
    return f"The given text has been identified as {label.split('_')[1]} with a score of {score}."


@app.route("/")
def render_index_page():
    """
     This is a default route to run index page
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
