
import sys, random

class Card(object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  # constructor
  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card object
  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  # equality tests
  def __eq__ (self, other):
    return self.rank == other.rank

  def __ne__ (self, other):
    return self.rank != other.rank

  def __lt__ (self, other):
    return self.rank < other.rank

  def __le__ (self, other):
    return self.rank <= other.rank

  def __gt__ (self, other):
    return self.rank > other.rank

  def __ge__ (self, other):
    return self.rank >= other.rank

class Deck (object):
  # constructor
  def __init__ (self, num_decks = 1):
    self.deck = []
    for i in range (num_decks):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card (rank, suit)
          self.deck.append (card)

  # shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # deal a card
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  # constructor
  def __init__ (self, num_players = 2, num_cards = 5):
    self.deck = Deck()
    self.deck.shuffle()
    self.all_hands = []
    self.numCards_in_Hand = num_cards

    # deal the cards to the players
    for i in range (num_players):
      hand = []
      for j in range (self.numCards_in_Hand):
        hand.append (self.deck.deal())
      self.all_hands.append(hand)

  # simulate the play of poker
  def play (self):
    # sort the hands of each player and print
    print()
    for i in range (len(self.all_hands)):
      sorted_hand = sorted (self.all_hands[i], reverse = True)
      self.all_hands[i] = sorted_hand
      hand_str = ''
      for card in sorted_hand:
        hand_str = hand_str + str (card) + ' '
      print ('Player ' + str(i + 1) + ' : ' + hand_str)
      print()

    # determine the type of each hand and print
    player_points = []	# create a list to store points for each hand
    hand_points = []	# create a list to store points for individual player

    for i in range(len(self.all_hands)):
      print('Player ' + str(i+1) + ' : ', end = ' ')

      if self.is_royal(self.all_hands[i]):
        hand_points.append(10)
        print('Royal Flush')
      elif self.is_straight_flush(self.all_hands[i]):
        hand_points.append(9)
        print('Straight Flush')
      elif self.is_four_kind(self.all_hands[i]):
        hand_points.append(8)
        print('Four of a Kind')
      elif self.is_full_house(self.all_hands[i]):
        hand_points.append(7)
        print('Full House')
      elif self.is_flush(self.all_hands[i]):
        hand_points.append(6)
        print('Flush')
      elif self.is_straight(self.all_hands[i]):
        hand_points.append(5)
        print('Straight')
      elif self.is_three_kind(self.all_hands[i]):
        hand_points.append(4)
        print('Three of a Kind')
      elif self.is_two_pair(self.all_hands[i]):
        hand_points.append(3)
        print('Two Pair')
      elif self.is_one_pair(self.all_hands[i]):
        hand_points.append(2)
        print('One Pair')
      elif self.is_high_card(self.all_hands[i]):
        hand_points.append(1)
        print('High Card')

     #cards in each players hands
      c1 = self.all_hands[i][0].rank()
      c2 = self.all_hands[i][1].rank()
      c3 = self.all_hands[i][2].rank()
      c4 = self.all_hands[i][3].rank()
      c5 = self.all_hands[i][4].rank()

      #how many points the player got
      #adding them to the overall list of points in the game
      total_points = (hand_points[i] * 15 ** 5) + (c1 * 15 ** 4) + (c2 * 15 ** 3) + (c3 * 15 ** 2) + (c4 * 15) + c5
      player_points.append(total_points)

    tie = 0
    all_tied = []
    first = 0
    while (first < (len(player_points)-1)):
      second = first +1
      while (second < (len(player_points)-1)):
        if (hand_points[first] == hand_points[second]):
          if (tie == 0) or (tie >= 1 and (hand_points[all_tied[0][0]] == hand_points[first])):
            tie += 1
            player1 = [first, player_points[first]]
            player2 = [second, player_points[second]]
            all_tied.append(player1)
            all_tied.append(player2)
          elif (tie > 0) and (hand_points[all_tied[0][0]] < hand_points[first]):
            tie = 1
            player1 = [first, player_points[first]]
            player2 = [second, player_points[second]]
            all_tied = []
            all_tied.append(player1)
            all_tied.append(player2)
        second += 1
      first += 1

    order_tied = []
    max = 0
    if tie > 0:
      for i in range(len(all_tied)):
        if all_tied[i][1] > max:
          max = all_tied[i][1]
          order_tied.insert(0, all_tied[i])
          if (len(all_tied) < 3) and (all_tied[0][0] == 1):
            order_tied.append(all_tied[i+1])
      print()
      for i in range(len(order_tied)):
        print('Player ' + str(order_tied[i][0] + 1) + ' ties.')
    else:
      winner = 0
      for i in range(len(player_points)):
        if (player_points[i] > max):
          winner = i
          max = player_points[i]
      print()
      print('Player ' + str(winner+1) + ' wins.')
    # determine winner and print


  # determine if a hand is a royal flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)

    if (not rank_order):
      return 0, ''

    points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Royal Flush'

  def is_straight_flush (self, hand):
    same_suit = True
    for i in range(len(hand)-1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    #check for numerical order
    rank_order = True

    for i in range(len(hand)-1):
      rank_order = rank_order and (hand[i].rank == (hand[i+1].rank + 1))

    if (not rank_order):
      return 0, ''

    points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Straight Flush'

  def is_four_kind (self, hand):
    four = False
    first = 0
    while (first < (len(hand)-1)):
      second = first +1
      same_count = 0
      while(second < (len(hand))):
        if (hand[first].rank == hand[second].rank):
          same_count += 1
        second += 1
      if (same_count == 3):
        four = True
      first += 1

    if four == False:
      return 0, ''

    points = 8 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Four of a Kind'

  def is_full_house (self, hand):
    full = False
    if ((hand[0].rank == hand[1].rank) and (hand[1].rank == hand[2].rank) and (hand[3].rank == hand[4].rank)):
      if (hand[0].rank != hand[3].rank):
        full = True
    elif ((hand[2].rank == hand[3].rank) and (hand[3].rank == hand[4].rank) and (hand[0].rank == hand[1].rank)):
      if hand[2].rank != hand[0].rank:
        full = True

    if full == False:
      return 0, ''

    points = 7 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Full House'

  def is_flush (self, hand):
    same_suit = True
    for i in range(len(hand)-1):
      same_suit = same_suit and (hand[i].suit == hand[i+1].suit)

    if same_suit == False:
      return 0, ''

    points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Flush'

  def is_straight (self, hand):
    straight = False
    same_suit = True
    for i in range(len(hand)-1):
      same_suit = same_suit and (hand[i].suit == hand[i+1].suit)

    if (not same_suit):
      rank_order = True
      for i in range(len(hand)-1):
        rank_order = rank_order and (hand[i].rank == (hand[i+1].rank + 1))
      straight = rank_order

    if straight == False:
      return 0, ''

    points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Straight'

  def is_three_kind (self, hand):
    three = False
    first = 0
    while first < (len(hand)-1):
      second = first + 1
      same_count = 0
      while (second < (len(hand)-1)):
        if (hand[first].rank == hand[second].rank):
          same_count += 1
        second += 1
      if same_count == 2:
        three = True
      first += 1

    if three == False:
      return 0, ''

    points = 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Three of a Kind'

  def is_two_pair (self, hand):
    two = False
    if ((hand[0].rank == hand[1].rank) and (hand[2].rank == hand[3].rank)):
      if ((hand[0].rank != hand[4].rank) and (hand[2].rank != hand[4].rank)):
        two = True

    if two == False:
      return 0, ''

    points = 3 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Two Pair'

  # determine if a hand is one pair
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
  def is_one_pair (self, hand):
    one_pair = False
    pair = []
    c1 = 0
    c2 = 0
    for i in range(len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        one_pair = True
        c1 = hand[i].rank
        c2 = hand[i+1].rank
        break
    if (not one_pair):
      return 0, ''

    pair.append(c1)
    pair.append(c2)
    hand.remove(c1)
    hand.remove(c2)

    points = (2 * 15 ** 5) + (pair[0] * 15 ** 4) + (pair[1] * 15 ** 3)
    points = points + (hand[0].rank) * 15 ** 2 + (hand[1].rank) * 15 ** 1
    points = points + (hand[2].rank)

    return points, 'One Pair'

  def is_high_card (self,hand):
    high_card = True

    points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'High Card'

def main():
  # read number of players from stdin
  line = sys.stdin.readline()
  line = line.strip()
  num_players = int (line)
  if (num_players < 2) or (num_players > 6):
    return

  # create the Poker object
  game = Poker (num_players)

  # play the game
  game.play()

if __name__ == "__main__":
  main()
