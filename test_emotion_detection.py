import unittest
import json

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def sort_dominent(self, data):
        # Filter out non-numeric values
        numeric_items = {k: v for k, v in data.items() if isinstance(v, (int, float))}
        # Sort by value
        sorted_data = dict(sorted(numeric_items.items(), key=lambda item: item[1], reverse=True))
        return sorted_data

    def test_emotion_detector(self):
        # Sort value by desceding and check the first key 

        # Test case for positive joy
        result_1 = json_response = json.loads(emotion_detector('I am glad this happened'))
        numeric_items = {k: v for k, v in result_1.items() if isinstance(v, (int, float))}
        sorted_data = dict(sorted(numeric_items.items(), key=lambda item: item[1], reverse=True))
        self.assertEqual(list(sorted_data.keys())[0], 'joy')

        # Test case for positive anger
        result_1 = json_response = json.loads(emotion_detector('I am really mad about this'))
        numeric_items = {k: v for k, v in result_1.items() if isinstance(v, (int, float))}
        sorted_data = dict(sorted(numeric_items.items(), key=lambda item: item[1], reverse=True))
        self.assertEqual(list(sorted_data.keys())[0], 'anger')

        # Test case for positive disgust
        result_1 = json_response = json.loads(emotion_detector('I feel disgusted just hearing about this'))
        numeric_items = {k: v for k, v in result_1.items() if isinstance(v, (int, float))}
        sorted_data = dict(sorted(numeric_items.items(), key=lambda item: item[1], reverse=True))
        self.assertEqual(list(sorted_data.keys())[0], 'disgust')

        # Test case for positive sadness
        result_1 = json_response = json.loads(emotion_detector('I am so sad about this'))
        numeric_items = {k: v for k, v in result_1.items() if isinstance(v, (int, float))}
        sorted_data = dict(sorted(numeric_items.items(), key=lambda item: item[1], reverse=True))
        self.assertEqual(list(sorted_data.keys())[0], 'sadness')

        # Test case for positive fear
        result_1 = json_response = json.loads(emotion_detector('I am really afraid that this will happen'))
        numeric_items = {k: v for k, v in result_1.items() if isinstance(v, (int, float))}
        sorted_data = dict(sorted(numeric_items.items(), key=lambda item: item[1], reverse=True))
        self.assertEqual(list(sorted_data.keys())[0], 'fear')        

unittest.main()
