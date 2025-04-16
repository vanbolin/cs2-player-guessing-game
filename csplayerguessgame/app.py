"""
CS2 Player Guessing Game - Web Application
"""
from flask import Flask, render_template, request, jsonify, session
import secrets
from csplayerguessgame.game import Game
from csplayerguessgame.data.players import get_all_players, get_player_by_name
from csplayerguessgame.data.country_flags import COUNTRY_TO_FLAG_CODE

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Store active games by session id
active_games = {}

@app.route('/')
def index():
    """Render the main game page."""
    # Start a new game for this session if one doesn't exist
    if 'game_id' not in session:
        session['game_id'] = secrets.token_hex(8)
        
    game_id = session['game_id']
    if game_id not in active_games:
        active_games[game_id] = Game()
        
    all_players = get_all_players()
    player_names = [player["name"] for player in all_players]
    
    return render_template('index.html', player_names=player_names)

@app.route('/api/make_guess', methods=['POST'])
def make_guess():
    """Process a player guess."""
    if 'game_id' not in session:
        return jsonify({"error": "No active game"}), 400
    
    game_id = session['game_id']
    if game_id not in active_games:
        active_games[game_id] = Game()
    
    game = active_games[game_id]
    
    # If game is already over, return current state
    if game.game_over:
        return jsonify(game.get_state())
    
    # Get player name from request
    data = request.get_json()
    player_name = data.get('player_name')
    
    if not player_name:
        return jsonify({"error": "Player name is required"}), 400
    
    # Make the guess and get result
    result = game.make_guess(player_name)
    
    # If there was an error finding the player, return that
    if "error" in result:
        return jsonify({"error": result["error"]}), 404
    
    # Return the current game state
    return jsonify(game.get_state())

@app.route('/api/new_game', methods=['POST'])
def new_game():
    """Start a new game."""
    game_id = session.get('game_id', secrets.token_hex(8))
    session['game_id'] = game_id
    
    active_games[game_id] = Game()
    
    return jsonify({"message": "New game started"})

@app.route('/api/game_state', methods=['GET'])
def game_state():
    """Get current game state."""
    if 'game_id' not in session:
        return jsonify({"error": "No active game"}), 400
    
    game_id = session['game_id']
    if game_id not in active_games:
        active_games[game_id] = Game()
    
    game = active_games[game_id]
    return jsonify(game.get_state())

@app.route('/api/players', methods=['GET'])
def get_players():
    """Return list of player names for autocomplete."""
    players = get_all_players()
    player_names = [player["name"] for player in players]
    return jsonify(player_names)

@app.route('/api/flag/<country>', methods=['GET'])
def get_flag_code(country):
    """Get flag code for a country."""
    flag_code = COUNTRY_TO_FLAG_CODE.get(country, "")
    return jsonify({"flag_code": flag_code})

# Clean up finished games occasionally (not implemented for simplicity)

if __name__ == '__main__':
    app.run(debug=True) 