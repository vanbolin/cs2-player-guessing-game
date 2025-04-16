"""
Game logic for CS2 Player Guessing Game.
"""
import os
import json
import datetime
from csplayerguessgame.data.players import get_random_player, get_player_by_name

class Game:
    """Main game class to manage game state and logic."""
    
    def __init__(self):
        """Initialize a new game."""
        self.target_player = get_random_player()
        self.guesses = []
        self.max_guesses = 8
        self.game_over = False
        self.won = False
        self.start_time = datetime.datetime.now()
    
    def make_guess(self, player_name):
        """Process a player's guess."""
        guessed_player = get_player_by_name(player_name)
        
        if not guessed_player:
            return {"error": f"Player '{player_name}' not found."}
        
        result = self._compare_players(guessed_player)
        self.guesses.append(result)
        
        # Check if the guess is correct
        if guessed_player["name"] == self.target_player["name"]:
            self.game_over = True
            self.won = True
            
        # Check if max guesses reached
        if len(self.guesses) >= self.max_guesses:
            self.game_over = True
            
        return result
    
    def _compare_players(self, guessed_player):
        """Compare the guessed player with the target player and provide feedback."""
        target = self.target_player
        
        # Create a result dictionary with all needed information
        result = {
            "name": guessed_player["name"],
            "team": {
                "value": guessed_player["team"],
                "correct": guessed_player["team"] == target["team"],
                "partial": False,
            },
            "nationality": {
                "value": guessed_player["nationality"],
                "flag": guessed_player["nationality"],
                "correct": guessed_player["nationality"] == target["nationality"],
                "partial": guessed_player["continent"] == target["continent"] and 
                           guessed_player["nationality"] != target["nationality"],
            },
            "age": {
                "value": guessed_player["age"],
                "correct": guessed_player["age"] == target["age"],
                "direction": "equal" if guessed_player["age"] == target["age"] else 
                            ("down" if guessed_player["age"] > target["age"] else "up"),
            },
            "role": {
                "value": guessed_player["role"],
                "correct": guessed_player["role"] == target["role"],
            },
            "hltv_top20_appearances": {
                "value": guessed_player["hltv_top20_appearances"],
                "correct": guessed_player["hltv_top20_appearances"] == target["hltv_top20_appearances"],
                "direction": "equal" if guessed_player["hltv_top20_appearances"] == target["hltv_top20_appearances"] else 
                            ("down" if guessed_player["hltv_top20_appearances"] > target["hltv_top20_appearances"] else "up"),
            }
        }
        
        return result
    
    def get_state(self):
        """Return the current game state."""
        return {
            "guesses": self.guesses,
            "target_player": self.target_player if self.game_over else None,
            "game_over": self.game_over,
            "won": self.won,
            "guesses_left": self.max_guesses - len(self.guesses),
            "elapsed_time": (datetime.datetime.now() - self.start_time).total_seconds()
        }
    
    def get_target_player(self):
        """Return the target player (only if game is over)."""
        if self.game_over:
            return self.target_player
        return None 