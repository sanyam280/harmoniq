from flask import Flask, request, jsonify, render_template
from deepface import DeepFace
import pylast
from flask_cors import CORS
import cv2
import numpy as np
import logging
import os

# Setup
app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Last.fm credentials
LASTFM_API_KEY = "8f2e5122c0034cb7c1eaf3a0e21c7ee5"
LASTFM_API_SECRET = "fd5d0aae8dbc49c3d514b0dfc078091f"

# Connect to Last.fm
def init_lastfm():
    return pylast.LastFMNetwork(api_key=LASTFM_API_KEY, api_secret=LASTFM_API_SECRET)

# Emotion-to-tags mapping
emotion_map = {
    'happy': {'tags': ['happy', 'pop', 'dance']},
    'sad': {'tags': ['sad', 'acoustic', 'classical']},
    'angry': {'tags': ['angry', 'rock', 'metal']},
    'neutral': {'tags': ['chill', 'pop']},
    'surprise': {'tags': ['energetic', 'edm']},
    'fear': {'tags': ['dark', 'ambient']},
    'disgust': {'tags': ['grunge', 'alternative']}
}

def get_recommendations(lastfm, emotion):
    tags = emotion_map.get(emotion.lower(), emotion_map['neutral'])['tags']
    for tag_str in tags:
        try:
            tag = lastfm.get_tag(tag_str)
            tracks = tag.get_top_tracks(limit=5)
            return [{"title": t.item.get_name(), "artist": t.item.get_artist().get_name()} for t in tracks]
        except Exception as e:
            logger.warning(f"Tag {tag_str} failed: {e}", exc_info=True)
    return []

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['image']
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

    try:
        analysis = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
        emotion = analysis[0]['dominant_emotion'].lower()

        lastfm = init_lastfm()
        recommendations = get_recommendations(lastfm, emotion)

        return jsonify({
            'emotion': emotion,
            'recommendations': recommendations
        })
    except Exception as e:
        logger.error(f"Error during analysis: {e}", exc_info=True)
        return jsonify({'error': 'Failed to process image or get recommendations.'}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port = port)
