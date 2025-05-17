# music_recommender.py
import pylast
import logging
from typing import List, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MusicRecommender:
    def __init__(self, api_key: str, api_secret: str):
        """Initialize Last.fm recommender system"""
        self.lastfm = self._initialize_lastfm(api_key, api_secret)
        self.emotion_map = {
            'happy': {'tags': ['happy', 'pop', 'dance']},
            'sad': {'tags': ['sad', 'acoustic', 'classical']},
            'angry': {'tags': ['angry', 'rock', 'metal']},
            'neutral': {'tags': ['chill', 'pop']},
            'surprise': {'tags': ['energetic', 'edm']},
            'fear': {'tags': ['dark', 'ambient']},
            'disgust': {'tags': ['grunge', 'alternative']}
        }
    
    def _initialize_lastfm(self, api_key: str, api_secret: str) -> pylast.LastFMNetwork:
        """Initialize and authenticate Last.fm client"""
        try:
            return pylast.LastFMNetwork(
                api_key=api_key,
                api_secret= api_secret
            )
        except Exception as e:
            logger.error(f"Last.fm initialization failed: {str(e)}")
            raise
    
    def get_recommendations(self, emotion: str, limit: int = 5) -> List[Tuple[str, str]]:
        """
        Get track recommendations based on detected emotion
        
        Args:
            emotion: Detected emotion (must match emotion_map keys)
            limit: Number of recommendations to return
            
        Returns:
            List of (song_name, artist_name) tuples
        """
        params = self.emotion_map.get(emotion.lower(), self.emotion_map['neutral'])
        recommendations = []
    

        try:
            # Try each tag until we get recommendations
            for tag in params['tags']:
                try:
                    tag_obj = self.lastfm.get_tag(tag)
                    tracks = tag_obj.get_top_tracks(limit=limit)
                    
                    for track in tracks:
                        try:
                            track_info = track.item
                            recommendations.append(
                                (track_info.get_name(), 
                                 track_info.get_artist().get_name())
                            )
                            if len(recommendations) >= limit:
                                return recommendations
                        except Exception as e:
                            logger.warning(f"Couldn't process track: {str(e)}")
                            continue
                    
                except Exception as e:
                    logger.warning(f"Tag {tag} failed: {str(e)}")
                    continue
        
        except Exception as e:
            logger.error(f"Last.fm API Error: {str(e)}")
        
        return recommendations if recommendations else []

    @staticmethod
    def print_recommendations(recommendations: List[Tuple[str, str]]):
        """Display recommendations in a formatted way"""
        if not recommendations:
            print("No recommendations available")
            return
        
        print("\nRecommended Songs:")
        for idx, (name, artist) in enumerate(recommendations, 1):
            print(f"{idx}. {name} by {artist}")
            