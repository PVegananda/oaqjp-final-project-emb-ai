# Emotion Detector - Tasks 7 & 8 Copy-Paste Ready Submission

---

## TASK 7 - Activity 1: emotion_detection.py Error Handling Code (7a_error_handling_function)

**Requirement**: Submit the code from the emotion_detection.py file showing the updated emotion_detector function for status code 400. (1 Point)

**COPY THIS CODE TO COURSERA**:

```python
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
```

**Key Requirements Met:**
✅ Function definition: `emotion_detector(text_to_analyse)`
✅ Imports: `import requests`
✅ URL specified: Watson NLP API endpoint
✅ HTTP Headers: Authorization and Content-Type for JSON
✅ POST request: `requests.post(url, headers=headers, json=payload, timeout=10)`
✅ Status code 400 handling: Returns None values with status_code: 400
✅ Error response structure includes status_code field

---

## TASK 7 - Activity 2: server.py Error Handling Code

**Requirement**: Submit the code from the server.py file showing the handling of blank input errors. (1 Point)

**COPY THIS CODE TO COURSERA**:

```python
"""
Flask web server for Emotion Detector application
"""
from flask import Flask, render_template, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the main page"""
    return render_template("index.html")


@app.route("/emotions", methods=["POST"])
def analyze_emotion():
    """
    API endpoint to analyze emotions from text

    Expected JSON payload:
    {
        "textToAnalyze": "text content here"
    }
    """
    # Get the text from request
    data = request.get_json()
    text_to_analyze = data.get("textToAnalyze", "").strip() if data else ""

    # Handle blank input
    if not text_to_analyze:
        return jsonify({
            "error": "Please provide non-empty text",
            "status_code": 400
        }), 400

    # Analyze emotions
    result = emotion_detector(text_to_analyze)

    # Check for errors
    if result.get("status_code") == 400:
        return jsonify({
            "error": "Invalid input",
            "status_code": 400
        }), 400

    if result.get("status_code") and result.get("status_code") != 200:
        return jsonify({
            "error": "Error analyzing emotions",
            "status_code": result.get("status_code")
        }), result.get("status_code", 500)

    # Return the emotion analysis
    return jsonify(result), 200


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
```

---

## TASK 7 - Activity 3: Error Handling Interface Screenshot

**Requirement**: Upload the screenshot named 7c_error_handling_interface.png validating error handling functionality. (1 Point)

**ACTION**: Upload the file: `7c_error_handling_interface.png`

**FILE LOCATION**:
- Local path: `/Users/pvegananda/Dev/01-Study/Kuliah/Coursera/emotion-detector/7c_error_handling_interface.png`
- GitHub: https://github.com/PVegananda/emotion-detector/blob/main/7c_error_handling_interface.png

**SCREENSHOT SHOWS**:
- Emotion Detector web interface (http://localhost:5002/)
- Text input field
- Analyze/Clear buttons
- Purple gradient background
- Ready to test error handling with blank input

---

## TASK 8 - Activity 1: server.py Code For Static Code Analysis

**Requirement**: Submit the code from the server.py file demonstrating the execution of static code analysis. (1 Point)

**COPY THIS CODE TO COURSERA**:

```python
"""
Flask web server for Emotion Detector application
"""
from flask import Flask, render_template, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the main page"""
    return render_template("index.html")


@app.route("/emotions", methods=["POST"])
def analyze_emotion():
    """
    API endpoint to analyze emotions from text

    Expected JSON payload:
    {
        "textToAnalyze": "text content here"
    }
    """
    # Get the text from request
    data = request.get_json()
    text_to_analyze = data.get("textToAnalyze", "").strip() if data else ""

    # Handle blank input
    if not text_to_analyze:
        return jsonify({
            "error": "Please provide non-empty text",
            "status_code": 400
        }), 400

    # Analyze emotions
    result = emotion_detector(text_to_analyze)

    # Check for errors
    if result.get("status_code") == 400:
        return jsonify({
            "error": "Invalid input",
            "status_code": 400
        }), 400

    if result.get("status_code") and result.get("status_code") != 200:
        return jsonify({
            "error": "Error analyzing emotions",
            "status_code": result.get("status_code")
        }), result.get("status_code", 500)

    # Return the emotion analysis
    return jsonify(result), 200


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
```

---

## TASK 8 - Activity 2: Static Code Analysis Perfect Score Terminal Output

**Requirement**: Submit the terminal output showing a perfect score for static code analysis. (1 Point)

**COPY THIS OUTPUT TO COURSERA**:

```
$ source venv/bin/activate && PYTHONPATH=. python -m pylint emotion_detection.py server.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

---

## SUBMISSION CHECKLIST - Tasks 7 & 8

✅ Task 7 - Activity 1: emotion_detection.py code with status code 400 error handling (1 Point)
✅ Task 7 - Activity 2: server.py code showing blank input error handling (1 Point)
✅ Task 7 - Activity 3: 7c_error_handling_interface.png screenshot (1 Point)
✅ Task 8 - Activity 1: server.py code for static code analysis (1 Point)
✅ Task 8 - Activity 2: Pylint terminal output with 10.00/10 perfect score (1 Point)

**TOTAL POINTS**: 5 Points ✅

---

## HOW TO SUBMIT TO COURSERA

### For Each Field:

**1️⃣  TASK 7 - Activity 1**:
→ Copy the emotion_detection.py code above
→ Paste into Coursera submission field

**2️⃣  TASK 7 - Activity 2**:
→ Copy the server.py code above
→ Paste into Coursera submission field

**3️⃣  TASK 7 - Activity 3**:
→ Download or upload: `7c_error_handling_interface.png`
→ Upload to Coursera

**4️⃣  TASK 8 - Activity 1**:
→ Copy the server.py code above
→ Paste into Coursera submission field

**5️⃣  TASK 8 - Activity 2**:
→ Copy the pylint terminal output above
→ Paste into Coursera submission field

---

## GitHub REPOSITORY

All files available at:
https://github.com/PVegananda/emotion-detector

**Files included**:
- 7c_error_handling_interface.png (error handling screenshot)
- emotion_detection.py (error handling implementation)
- server.py (error handling and analysis)
- SUBMISSION_TASKS_7_8.md (full documentation)
- COPY_PASTE_TASKS_7_8.md (this file)
- All previous task submission materials
