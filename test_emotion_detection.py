import unittest
import json

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for positive joy
        json_response = json.loads(emotion_detector('I am glad this happened'))
        self.assertEqual(json_response["dominant_emotion"], 'joy')

        # Test case for positive anger
        json_response = json.loads(emotion_detector('I am really mad about this'))
        self.assertEqual(json_response["dominant_emotion"], 'anger')
        # Test case for positive disgust
        json_response = json.loads(emotion_detector('I feel disgusted just hearing about this'))
        self.assertEqual(json_response["dominant_emotion"], 'disgust')
        # Test case for positive sadness
        json_response = json.loads(emotion_detector('I am so sad about this'))
        self.assertEqual(json_response["dominant_emotion"],'sadness')
        # Test case for positive fear
        json_response = json.loads(emotion_detector('I am really afraid that this will happen'))
        self.assertEqual(json_response["dominant_emotion"], 'fear')        

unittest.main()
