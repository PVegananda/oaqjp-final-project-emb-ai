"""
Emotion Detection module using IBM Watson NLP
"""
import requests


def emotion_detector(text_to_analyze):
    """
    Detect emotions in the provided text using Watson NLP API.

    Args:
        text_to_analyze (str): The text to analyze for emotions

    Returns:
        dict: Contains emotion scores and dominant emotion, or error status
    """

    # Check for blank or None input
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "status_code": 400
        }

    # Watson NLP API endpoint
    url = ("https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/"
           "instances/9ccb4dc7-69a2-4302-821e-d17f2b185c36")

    # Headers for authentication
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json"
    }

    # Request payload
    payload = {
        "raw_document": {
            "text": text_to_analyze
        },
        "features": {
            "emotion": {}
        }
    }

    try:
        # Make the API request
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=10
        )

        # Handle HTTP error responses
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

        # Parse the response
        response_json = response.json()

        # Extract emotion scores
        emotion_data = response_json.get("emotion", {}).get("document", {}).get("emotion", {})

        # Extract individual emotion scores
        anger = emotion_data.get("anger", 0)
        disgust = emotion_data.get("disgust", 0)
        fear = emotion_data.get("fear", 0)
        joy = emotion_data.get("joy", 0)
        sadness = emotion_data.get("sadness", 0)

        # Find dominant emotion
        emotions = {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness
        }

        dominant_emotion = max(emotions, key=emotions.get)

        # Format and return the result
        return {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness,
            "dominant_emotion": dominant_emotion
        }

    except requests.exceptions.RequestException:
        # Handle network errors
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "status_code": 500
        }
