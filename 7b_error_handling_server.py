"""
Flask web server for Emotion Detector application
Error handling for blank input
"""
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the main page of the application"""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detection():
    """
    Flask route for emotion detection using GET method.
    Handles blank input errors and returns formatted response.
    
    Query Parameters:
        textToAnalyze (str): The text to analyze for emotions
        
    Returns:
        JSON response with emotion scores or error message
    """
    # Get the text to analyze from query parameters
    text_to_analyze = request.args.get("textToAnalyze")
    
    # Check for blank or empty input
    if not text_to_analyze or text_to_analyze.strip() == "":
        # Handle blank input error - generate formatted error response
        return jsonify({
            "error": "Please provide non-empty text for emotion analysis",
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "status_code": 400
        }), 400
    
    # Call the emotion_detector function with the text input
    result = emotion_detector(text_to_analyze)
    
    # Check if emotion_detector returned a status code 400 error
    if result.get("status_code") == 400:
        # Handle blank input error from emotion_detector
        return jsonify({
            "error": "Invalid input: Text could not be analyzed",
            "anger": result.get("anger"),
            "disgust": result.get("disgust"),
            "fear": result.get("fear"),
            "joy": result.get("joy"),
            "sadness": result.get("sadness"),
            "dominant_emotion": result.get("dominant_emotion"),
            "status_code": 400
        }), 400
    
    # Check for other non-200 status codes
    if result.get("status_code") and result.get("status_code") != 200:
        return jsonify({
            "error": "Error processing emotions",
            "anger": result.get("anger"),
            "disgust": result.get("disgust"),
            "fear": result.get("fear"),
            "joy": result.get("joy"),
            "sadness": result.get("sadness"),
            "dominant_emotion": result.get("dominant_emotion"),
            "status_code": result.get("status_code")
        }), result.get("status_code", 500)
    
    # Format and return the successful response with all emotion scores
    formatted_response = {
        "anger": result.get("anger"),
        "disgust": result.get("disgust"),
        "fear": result.get("fear"),
        "joy": result.get("joy"),
        "sadness": result.get("sadness"),
        "dominant_emotion": result.get("dominant_emotion")
    }
    
    return jsonify(formatted_response), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
