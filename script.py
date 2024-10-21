import random

def initialize_deck():
  # Initialize cards
  suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
  values = [ i for i in range(1, 14) ] # 1 = A, 2~10, 11~13 = J, Q, K
  deck = [(suit, value) for suit in suits for value in values]
  # Add 1 joker
  deck.extend([("Joker", "Black")])
  # random cards
  random.shuffle(deck)

  return deck

def deal_cards(cards, num_players):
  # deal out cards to players
  players_cards = [ [] for _ in range(num_players) ]

  for i in range(len(cards)):
    players_cards[i % num_players].append(cards[i])
  
  return players_cards

def main():
  # Initialize players
  num_players = int(input("Please enter the number of players: "))

  while num_players < 2 or num_players > 4:
    num_players = int(input("Number of players is limited to 2 to 4 people!\nPlease enter again: "))
  
  print("OK. Now please enter player name in sequence.")
  name_players = [str(input(f"{i}: ")) for i in range(1, num_players + 1)]
  print(name_players)

  deck = initialize_deck()
  players_card = deal_cards(deck, num_players)


if __name__ == "__main__":
  main()