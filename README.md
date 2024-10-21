# Joker Card Game (Terminal Version)

## Introduction

This is a terminal-based interactive version of the classic **Old Maid** card game. Players can enjoy the game directly from their terminal by interacting through the command line. The game involves strategic decision-making and luck as players draw cards from each other to avoid being the one left holding the Joker at the end.

The goal of the game is to form pairs with the cards in your hand and discard them. The player who successfully discards all their cards first is the winner, while the one holding the Joker card at the end is the loser.

## Features

- **Interactive Gameplay**: The game takes player input for every move, allowing for an immersive and interactive experience directly from the terminal.
- **Customizable Players**: You can play with 2 to 4 players, with the ability to name each player.
- **Randomized Deck**: Cards are shuffled randomly at the start of the game, and each player is dealt a random set of cards.
- **Pair Matching**: The game automatically detects pairs of cards in a player's hand and removes them.
- **Joker Card**: One Joker card is added to the deck, and the goal is to avoid holding it by the end of the game.

## How to Play

1. **Setup**:
   - After starting the game, you will be asked to input the number of players (between 2 and 4).
   - You will then enter the names for each player.

2. **Gameplay**:
   - Players will take turns drawing a card from the next player's hand.
   - After drawing a card, if the player has a pair (two cards with the same value), they will discard the pair.
   - The game continues until one player discards all of their cards and becomes the winner.
   - The player holding the Joker at the end loses the game.

3. **Winning the Game**:
   - The first player to discard all of their cards is declared the winner.
   - If any player holds the Joker after all other cards have been paired and discarded, that player is the loser.

## Game Flow

1. **Initialize Deck**: A standard deck of 52 cards is created with one additional Joker.
2. **Deal Cards**: Cards are dealt evenly to all players, with one player receiving an extra card (the Joker).
3. **Draw and Discard**: Players take turns drawing a card from the next player's hand and discarding any pairs.
4. **End Game**: The game ends when one player runs out of cards or when only the Joker remains.

## Example Gameplay

```
$ python old_maid.py
Please enter the number of players (2-4): 3
OK. Now please enter player names in sequence.
Enter name for player 1: Alice
Enter name for player 2: Bob
Enter name for player 3: Charlie

--- ROUND 1 ---
Hi, Alice! Your next player has 5 card(s).
Please enter which card do you want (1-5): 3
Alice throws out the pairs: [(Hearts, 3), (Diamonds, 3)]

--- ROUND 2 ---
Hi, Bob! Your next player has 4 card(s).
Please enter which card do you want (1-4): 2
...
```

## Installation and Requirements

1. **Python**: Ensure you have Python installed (version 3.x recommended).
2. **Clone the Repository**: Clone this repository to your local machine.
   ```
   git clone https://github.com/verna0214/joker_game.git
   ```
3. **Run the Game**: Run the Python script from the terminal.
   ```
   python script.py
   ```

## License

This project is licensed under the MIT License.

## Author

verna0214

