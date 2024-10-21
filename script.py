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

def check_pairs(players_hand):
  pairs = []
  values = [ card[1] for card in players_hand if card[0] != "Joker" ]
  
  for value in set(values):
    count = values.count(value)
    if count >= 2:
      pair_cards = [card for card in players_hand if card[1] == value][:count - (count % 2)]
      pairs.extend(pair_cards)

  for pair in pairs:
    players_hand.remove(pair)
  
  return pairs


def main():
  # Initialize players
  num_players = int(input("Please enter the number of players: "))

  while num_players < 2 or num_players > 4:
    num_players = int(input("Number of players is limited to 2 to 4 people!\nPlease enter again: "))
  
  print("OK. Now please enter player name in sequence.")
  name_players = [str(input(f"{i}: ")) for i in range(1, num_players + 1)]

  # Deal with cards
  deck = initialize_deck()
  players_card = deal_cards(deck, num_players)

  # check pairs first
  for i in range(num_players):
    pairs = check_pairs(players_card[i])
    if pairs:
      print(f"{name_players[i]} throws out the pairs: {pairs}")
      if len(players_card[i]) == 0:
        print(f"Game is finished! Winner is {name_players[i]} !!")
        return
      
  # Game start
  current_round = 1

  while True:
    print(f"--- ROUND {current_round} ---")

    for i in range(num_players):
      opponent_cards = players_card[(i + 1) % num_players]
      print(f"Opponent_cards is: {opponent_cards}")
      opponent_idx = int(input(f"Hi, {name_players[i]}! Your next player has {len(opponent_cards)} card(s).\nPlease enter which card do you want? ")) - 1
      while opponent_idx < 0 or opponent_idx >= len(opponent_cards):
        opponent_idx = int(input(f"Out of range. Please choose again: ")) - 1
      
      print(f"oppnent_idx: {opponent_idx}")
      remove_card = opponent_cards.pop(opponent_idx)
      if len(opponent_cards) == 0:
        print(f"Game is finished! Winner is {name_players[(i + 1) % num_players]} !!")
        return
      players_card[i].append(remove_card)
      pairs = check_pairs(players_card[i])
      if pairs:
        print(f"{name_players[i]} throws out the pairs: {pairs}")
        if len(players_card[i]) == 0:
          print(f"Game is finished! Winner is {name_players[i]} !!")
          return
    
    current_round += 1

if __name__ == "__main__":
  main()