import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotions(self):
        test_cases = [
            {"statement": "I am glad this happened", "expected_dominant_emotion": "joy"},
            {"statement": "I am really mad about this", "expected_dominant_emotion": "anger"},
            {"statement": "I feel disgusted just hearing about this", "expected_dominant_emotion": "disgust"},
            {"statement": "I am so sad about this", "expected_dominant_emotion": "sadness"},
            {"statement": "I am really afraid that this will happen", "expected_dominant_emotion": "fear"},
        ]

        for case in test_cases:
            with self.subTest(statement=case["statement"]):
                result = emotion_detector(case["statement"])
                self.assertEqual(result["dominant_emotion"], case["expected_dominant_emotion"],
                                 f"Failed for statement: {case['statement']}")

if __name__ == "__main__":
    unittest.main()

# python -m unittest test_emotion_detection.py