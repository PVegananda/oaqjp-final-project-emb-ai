"""
Flask web server for Emotion Detector application
Server implementation with proper code structure for static code analysis
"""
from flask import Flask, render_template, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """
    Render the main index page of the application.
    
    Returns:
        Rendered HTML template for the main page
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def run_emotion_detection():
    """
    Route to detect emotions from input text_to_analyze.
    
    Receives text input as query parameter and returns emotion analysis
    with all five emotion scores and the dominant emotion.
    
    Query Parameters:
        textToAnalyze (str): The text to analyze for emotions
        
    Returns:
        JSON response containing:
        - anger (float): Anger emotion score
        - disgust (float): Disgust emotion score
        - fear (float): Fear emotion score
        - joy (float): Joy emotion score
        - sadness (float): Sadness emotion score
        - dominant_emotion (str): The emotion with highest score
    """
    # Get the text to analyze from query parameters
    text_to_analyze = request.args.get("textToAnalyze")
    
    # Check for blank or missing input
    if not text_to_analyze or text_to_analyze.strip() == "":
        # Return formatted response for blank input (400 error)
        response_text = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "status_code": 400
        }
        return jsonify(response_text), 400
    
    # Call emotion_detector function with the input text
    response_text = emotion_detector(text_to_analyze)
    
    # Check for status code 400 (invalid input from emotion_detector)
    if response_text.get("status_code") == 400:
        # Return formatted response for invalid input
        return jsonify(response_text), 400
    
    # Check for other error status codes
    if response_text.get("status_code") and response_text.get("status_code") != 200:
        # Return formatted response for other errors
        return jsonify(response_text), response_text.get("status_code", 500)
    
    # Format the successful response with all emotion scores
    formatted_response = {
        "anger": response_text.get("anger"),
        "disgust": response_text.get("disgust"),
        "fear": response_text.get("fear"),
        "joy": response_text.get("joy"),
        "sadness": response_text.get("sadness"),
        "dominant_emotion": response_text.get("dominant_emotion")
    }
    
    # Return successful response with 200 status code
    return jsonify(formatted_response), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
