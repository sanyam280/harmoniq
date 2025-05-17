import cv2
from deepface import DeepFace
import pylast  # Last.fm library
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Last.fm API Configuration
LASTFM_API_KEY = "8f2e5122c0034cb7c1eaf3a0e21c7ee5"
LASTFM_API_SECRET = "fd5d0aae8dbc49c3d514b0dfc078091f"

# Initialize Last.fm network
def initialize_lastfm():
    """Initialize and authenticate Last.fm client"""
    try:
        return pylast.LastFMNetwork(
            api_key=LASTFM_API_KEY,
            api_secret=LASTFM_API_SECRET
        )
    except Exception as e:
        logger.error(f"Last.fm initialization failed: {str(e)}")
        raise

# emotion map - last.fm tags
emotion_map = {
    'happy': {'tags': ['happy', 'pop', 'dance']},
    'sad': {'tags': ['sad', 'acoustic', 'classical']},
    'angry': {'tags': ['angry', 'rock', 'metal']},
    'neutral': {'tags': ['chill', 'pop']},
    'surprise': {'tags': ['energetic', 'edm']},
    'fear': {'tags': ['dark', 'ambient']},
    'disgust': {'tags': ['grunge', 'alternative']}
}

def get_lastfm_recommendations(lastfm, emotion):
    """Get track recommendations from Last.fm based on emotion"""
    params = emotion_map.get(emotion.lower(), emotion_map['neutral'])
    
    try:
        # getting top tracks for the first matching tag
        for tag in params['tags']:
            try:
                tag = lastfm.get_tag(tag)
                tracks = tag.get_top_tracks(limit=5)
                recommendations = []
                
                for track in tracks:
                    try:
                        track_info = track.item
                        recommendations.append(
                            (track_info.get_name(), 
                             track_info.get_artist().get_name())
                        )
                    except Exception as e:
                        logger.warning(f"Couldn't process track: {str(e)}")
                        continue
                
                if recommendations:
                    return recommendations
                    
            except Exception as e:
                logger.warning(f"Tag {tag} failed: {str(e)}")
                continue
        
        return []  # If no tracks found for any tag
        
    except Exception as e:
        logger.error(f"Last.fm API Error: {str(e)}")
        return []

def main():
    
    cap = None
    try:
        # Initialize components
        lastfm = initialize_lastfm()    
        #capturing video
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            raise RuntimeError("Webcam initialization failed")  
        
        logger.info("System ready. Press Q to quit.")
        last_emotion = None
        
        while True:
            ret, frame = cap.read()
            if not ret:
                logger.warning("Frame capture failed")
                continue
            
            # Process every second (30 frames at ~30fps)
            if cv2.getTickCount() % 30 == 0:
                try:
                    # Emotion detection
                    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    analysis = DeepFace.analyze(rgb_frame, 
                                              actions=['emotion'], 
                                              enforce_detection=False)
                    current_emotion = analysis[0]['dominant_emotion'].lower()
                    
                    if current_emotion != last_emotion:
                        logger.info(f"New emotion detected: {current_emotion}")
                        recommendations = get_lastfm_recommendations(lastfm, current_emotion)
                        
                        if recommendations:
                            print("\nRecommended Songs:")
                            for idx, (name, artist) in enumerate(recommendations, 1):
                                print(f"{idx}. {name} by {artist}")
                        else:
                            print("No recommendations available")
                        
                        last_emotion = current_emotion
                
                except Exception as e:
                    logger.error(f"Processing error: {str(e)}")
            
            # Display output
            display_text = f"Current Mood: {last_emotion}" if last_emotion else "Analyzing..."
            cv2.putText(frame, display_text, (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            cv2.imshow('Emotion Music Recommender', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            time.sleep(0.033)  # ~30fps
            
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
    finally:
        if cap and cap.isOpened():
            cap.release()
        cv2.destroyAllWindows()
        logger.info("Application shutdown complete")

if __name__ == "__main__":
    main()