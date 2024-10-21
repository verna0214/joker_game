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
        print(f"Game is finished! Winner is {name_players[i]}.")
        return


if __name__ == "__main__":
  main()