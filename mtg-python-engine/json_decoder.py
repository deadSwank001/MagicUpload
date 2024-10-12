import os
import json
import random
import logging

# Configure logging
logger = logging.getLogger('game_logger')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('game.log')
fh.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

# Define the path to the card data file
data_path = r'C:\Users\swank\Downloads\MtG Database.json'

# Load the card data from the JSON file
try:
    with open(data_path, 'r') as file:
        cards = json.load(file)
except FileNotFoundError:
    logger.error(f"Card data file not found at {data_path}")
    cards = []
except json.JSONDecodeError as e:
    logger.error(f"Error decoding JSON from {data_path}: {e}")
    cards = []
except Exception as e:
    logger.error(f"Unexpected error reading {data_path}: {e}")
    cards = []

# Ensure there are enough cards to create decks
if len(cards) >= 120:
    deck1_cards = random.sample(cards, 60)
    deck2_cards = random.sample(cards, 60)

    # Create decks
    deck1 = Deck(cards=deck1_cards)
    deck2 = Deck(cards=deck2_cards)

    # Create players
    player1 = Player(name="Alice", deck=deck1)
    player2 = AIPlayer(name="Bot", deck=deck2)

    # Start game
    game = GameEngine(players=[player1, player2])
    game.start_game()
else:
    logger.error("Insufficient cards available to start the game.")
    
    import os

json_path = os.path.join("C:", "Users", "swank", "Downloads", "Mtg Database.json")
image_dir = os.path.join("C:", "Users", "swank", "mtg-python-engine", "parser", "data", "images")