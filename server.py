"""
server.py

This module defines a Flask application that provides an endpoint for detecting emotions in text.
The application uses the EmotionDetection package to analyze the input text
and return emotion scores
along with the dominant emotion.

Author: Thanh Trung
Date: 16 Mar 2025
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Flask endpoint to detect emotions from a given statement.
    Returns:
        str: A formatted response including emotion scores and the dominant emotion,
        or an error message.
    """
    try:
        data = request.get_json()
        statement = data.get("statement", "")

        # Call the emotion detector function
        result = emotion_detector(statement)

        # Handle cases where the dominant emotion is None
        if result["dominant_emotion"] is None:
            return "Invalid text! Please try again!"


        response = (
            f"For the given statement, the system response is 'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
            f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )

        return response

    except ValueError as e:
        return jsonify({"error": f"Value error: {str(e)}"}), 400

    except KeyError as e:
        return jsonify({"error": f"Missing key: {str(e)}"}), 400

    except RuntimeError as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
