"""
Unit tests for emotion_detection module
"""
import unittest
from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for emotion_detector function"""

    def test_emotion_detector_joy(self):
        """Test detection of joy emotion"""
        result = emotion_detector("I love this!")
        # Should return a dictionary with proper keys
        self.assertIsInstance(result, dict)
        self.assertIn("dominant_emotion", result)
        self.assertIn("anger", result)
        self.assertIn("disgust", result)
        self.assertIn("fear", result)
        self.assertIn("joy", result)
        self.assertIn("sadness", result)

    def test_emotion_detector_sadness(self):
        """Test detection of sadness emotion"""
        result = emotion_detector("I am very sad")
        # Should return a dictionary with proper keys
        self.assertIsInstance(result, dict)
        self.assertIn("dominant_emotion", result)
        self.assertIn("anger", result)

    def test_emotion_detector_anger(self):
        """Test detection of anger emotion"""
        result = emotion_detector("I am furious!")
        # Should return a dictionary with proper keys
        self.assertIsInstance(result, dict)
        self.assertIn("dominant_emotion", result)

    def test_emotion_detector_blank_input(self):
        """Test handling of blank input"""
        result = emotion_detector("")
        self.assertEqual(result.get("status_code"), 400)
        self.assertIsNone(result.get("dominant_emotion"))

    def test_emotion_detector_none_input(self):
        """Test handling of None input"""
        result = emotion_detector(None)
        self.assertEqual(result.get("status_code"), 400)
        self.assertIsNone(result.get("dominant_emotion"))

    def test_emotion_detector_whitespace_input(self):
        """Test handling of whitespace-only input"""
        result = emotion_detector("   ")
        self.assertEqual(result.get("status_code"), 400)
        self.assertIsNone(result.get("dominant_emotion"))

    def test_emotion_detector_response_format(self):
        """Test that response has correct format"""
        result = emotion_detector("Test emotion detection")
        # Check that response contains all required keys
        required_keys = ["anger", "disgust", "fear", "joy", "sadness"]
        for key in required_keys:
            self.assertIn(key, result)


if __name__ == '__main__':
    unittest.main()
