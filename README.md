# Final Project: Emotion Detector

**Project Name: Final Project**

A Flask-based emotion detection application using IBM Watson NLP to analyze sentiment and emotions from text input.

## Features

- Detects emotions from text using Watson NLP
- Captures anger, disgust, fear, joy, and sadness emotions
- Web interface for easy access
- Comprehensive error handling
- Unit test coverage
- Production-ready code (pylint verified)

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

**As a module:**
```python
from emotion_detection import emotion_detector

result = emotion_detector("I love this!")
print(result)
```

**As a web service:**
```bash
python server.py
```
Then visit `http://localhost:5000/` in your browser.

## Project Structure

- `emotion_detection.py` - Core emotion detection logic
- `__init__.py` - Package initialization
- `server.py` - Flask web server
- `test_emotion_detection.py` - Unit tests
- `requirements.txt` - Python dependencies

## Testing

Run the test suite:
```bash
python -m pytest test_emotion_detection.py -v
```

## Code Quality

Run pylint analysis:
```bash
pylint emotion_detection.py server.py
```

## API Reference

### emotion_detector(text_to_analyze)

Analyzes emotions in the provided text.

**Parameters:**
- `text_to_analyze` (str): The text to analyze

**Returns:**
- Dictionary with emotion scores and dominant emotion if text is valid
- Error status code if input is invalid

**Example response:**
```json
{
  "anger": 0.0,
  "disgust": 0.0,
  "fear": 0.0,
  "joy": 1.0,
  "sadness": 0.0,
  "dominant_emotion": "joy"
}
```
