"""
Emotion Detection module using IBM Watson NLP
Error handling for status code 400
"""
import requests


def emotion_detector(text_to_analyse):
    """
    Detect emotions in the provided text using Watson NLP API.
    
    Sends a POST request to the Watson NLP API endpoint.
    Handles response status code 400 for invalid input.

    Args:
        text_to_analyse (str): The text to analyze for emotions

    Returns:
        dict: Contains emotion scores and dominant emotion,
              or error details with status_code for errors
    """
    
    # Watson NLP API endpoint URL
    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/9ccb4dc7-69a2-4302-821e-d17f2b185c36/analyze"
    
    # HTTP request headers for authentication and content type
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json"
    }
    
    # Request payload with input text
    payload = {
        "raw_document": {
            "text": text_to_analyse
        },
        "features": {
            "emotion": {}
        }
    }

    try:
        # Make POST request to Watson API
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=10
        )

        # Handle HTTP error status code 400 (Bad Request)
        if response.status_code == 400:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
                "status_code": 400
            }

        # Handle other non-200 status codes
        if response.status_code != 200:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
                "status_code": response.status_code
            }

        # Parse JSON response from Watson API
        response_json = response.json()

        # Extract emotion scores from nested response structure
        emotion_data = response_json.get("emotion", {}).get("document", {}).get("emotion", {})

        # Extract individual emotion scores
        anger = emotion_data.get("anger", 0)
        disgust = emotion_data.get("disgust", 0)
        fear = emotion_data.get("fear", 0)
        joy = emotion_data.get("joy", 0)
        sadness = emotion_data.get("sadness", 0)

        # Calculate dominant emotion (highest score)
        emotions = {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness
        }

        dominant_emotion = max(emotions, key=emotions.get)

        # Return formatted response with all emotion scores
        return {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness,
            "dominant_emotion": dominant_emotion
        }

    except requests.exceptions.RequestException:
        # Handle network/connection errors with status code 500
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "status_code": 500
        }
