# CS2 Player Guessing Game

A game where you try to guess the mystery CS2 professional player in 8 tries, similar to [Blast.tv's Counter-Strikle](https://blast.tv/counter-strikle/multiplayer).

## Features

- Guess the mystery CS2 player in 8 tries
- Feedback on each guess:
  - Green cells for correct attributes
  - Yellow cells for continent matches
  - Up/down arrows to indicate age and HLTV Top20 appearances comparisons
- Database of professional CS2 players that can be easily extended
- Search and autocomplete for player names

## Installation

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Game

Run the following command to start the web server:

```
python main.py
```

Then open your browser and navigate to:

```
http://localhost:5000
```

## Adding Players to Database

To add more players to the database, edit `csplayerguessgame/data/players.py`. The player data structure is as follows:

```python
{
    "name": "Player IGN",
    "team": "Team Name",
    "nationality": "Country",
    "continent": "Continent",
    "age": 25,
    "role": "Rifler",  # or "AWPer"
    "hltv_top20_appearances": 3
}
```

If you add players from a new country, also add the country flag code in `csplayerguessgame/data/country_flags.py`.

## Game Rules

1. You have 8 guesses to identify the mystery player
2. After each guess, you'll get feedback:
   - Green background = correct match
   - Yellow background = same continent but different country 
   - Arrows = indicates if the actual player is older/younger or has more/fewer HLTV Top20 appearances
3. When you run out of guesses or correctly identify the player, the answer will be revealed

## Technologies Used

- Python with Flask (backend)
- HTML, CSS, JavaScript (frontend)
- Bootstrap 5 (UI framework) 