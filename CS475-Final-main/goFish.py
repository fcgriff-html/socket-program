#each player needs 7 out of 52 unique cards
  #each 52-14  = 38 fishing cards
  #turn counter
  #major if statement: if [request] is in [players][deck] then send [request] card to [opponet][deck]
                    #else: 
            #go fish
#functions: generate deck and fish pile
  #generate deck and separate
  #creates array w 38 spots, two "hands" with 7 cards each
    #randomly populate the hands
   #deck = 2Darray [4][12]
  #pick 14 random cards and sort them into temp array[14]
  #if index of temp is even, send it to player, if odd send to opponet
  #copy deck into fishing pile unless the card has been drawn,
  #go_fish function to draw random card and update the fishing pile
#game stops when the pile counter hits zero or the quit command is entered

# the game is one by the player with the most "books"
# "book" = four cards of the same rank, i.e. for Queens or four 8s

#skeleton code


import numpy as np
import socket as sock
import random
#each player needs 7 out of 52 unique cards
  #each 52-14  = 38 fishing cards
  #turn counter
  #major if statement: if [request] is in [players][deck] then send [request] card to [opponet][deck]
                    #else: 
            #go fish
#functions: generate deck and fish pile
  #generate deck and separate
  #creates array w 38 spots, two "hands" with 7 cards each
    #randomly populate the hands
   #deck = 2Darray [4][52]
  #pick 14 random cards and sort them into temp array[14]
  #if index of temp is even, send it to player, if odd send to opponet
  #copy deck into fishing pile unless the card has been drawn,
  #go_fish function to draw random card and update the fishing pile
#game stops when the pile counter hits zero or the quit command is entered

#skeleton code

    
        
  
  #constructor to generate 2dArray
  #deck counter


class deck():
  
  #constructor to generate 2dArray
     def __init__(self):
        self.cards = []
        for suit in range (4):
            for rank in range (12):
                card = card(suit, rank)
                self.cards.append(card)
  #deck counter
"""
  def deck_popsplit():
    
    cards = [] 
    card_id = 0
    split = []
    split_key = []
    hand_player = []
    player_key = []
    hand_opp = []
    opp_key = []
    trackx = []
    tracky = []
    fishing_pile = []
    for i in range(0,3):
        cards[i]= []
        for j in range(0,11):
            card_id+=1
            cards[i][j] = card_id
    suite_key = ["clubs", "diamonds", "hearts", "spades"]
    cn_key = [1, 2, 3, 4, 5, 6, 7, 8, 9, "jack", "queen", "king", "ace"]
    turn = 0
    choice1 = None
    choice2 = None
    for i in range(0, 13): #this should generate the split and tie it to a choice number
        x = np.rand(0, 51)
        y = np.rand(0, 3)
        if x != choice1 and y != choice2:
            split.append([x, y])
            trackx.append(x)
            tracky.append(y)
            card_num = cn_key[x]
            cardname = suite_key[y]
            split_key[turn] = [card_num, cardname]
            turn+=1
            choice1 = x
            choice2 = y
    #next we want to split the 14 selected cards into two hands
    for i in range(0, 13):
        if i %2 ==0:
            hand_player[i] = split[i]
            player_key[i] = split_key[i]
        else:
            hand_opp[i] = split[i]
            opp_key[i] = split_key[i]
    count = 0
    for i in range(0, 3):
        for j in range(0, 11):
            sn = i #suite_number
            cn = j #card_number
            if sn != trackx[count] and cn != tracky[count]:
                   fish_pile 

    """
"""
    cards = np.zeros(52)
    split = []
    player_hand = []
    opp_hand = []
    fishing_pile = []
    card_id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "jack", "queen", "king", "ace"]
    count = 0
    for i in range(len(cards)):
      if count == 11:
        cards[i] = card_id[count]
        count = 0
      else:
        cards[i] = card_id[count]
      count+=1
    #so now we want to split the deck and make the fish pile
    #splitting
    prev = np.inf
    counter = 0
    idx_trace = []
    while counter != 13:
      randnum = random.randint(0, 51)
        if randnum != prev:
          split.append(cards[randnum])
          counter+=1
          idx_trace.append(randnum) #should allow us to trace indicies when making the fishing pile
          prev = randnum
         else:
          randnum = random.randint(0, 51)
     for i in range(len(split)):
      if i%2 == 0:
        player_hand.append(split[i])
       else:
        opp_hand.append(split[i])
       #now that we have split the selected cards into two hands, we need to populate the fishing pile
     for i in range(len(cards)):
      if i not in idx_trace:
        fishing_pile.append(cards[i])
     return fishing_pile, player_hand, opp_hand
      #the above code should cycle through all 52 cards assigning each index a card id from the possible card_ids
            
    #now we want to copy the deck into the fish pile and remove the 14 cards the players have in their hands
    """
  #method for determining if the deck contains a specific card
  #returns true if the deck contains the given card, false if not
def contains(card):
    ret = False
    # loop through each card in the deck
    for i in range(len(cards)):
       # pick out the current card
      currentCard = cards[i]
      # check if current card matches the given card
      if (currentCard.isSameCard(card)):
        # if it does match, return true
        ret = True
    # if we make it through the deck with no matches, return false   
    return ret   

  
class Card(object):
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
    
    # checks if two cards are of the same rank
  def isSameRank(self, otherCard):
      return self.rank == otherCard.rank
            
    # checks if two cards are the same card
  def isSameCard(self, otherCard):
      return self.rank == otherCard.rank, self.suit
          
  
class Player(object):
  def __init__(self):
      self.hand = [] # start with an empty array
      self.score = 0 # score gets +1 every time a book is achieved
        
       
  def dealHand(self, deck):
         # deal 7 random cards to this player
         while(len(self.hand) < 7):
            self.hand.append(getRandomCard(deck))
       
    
    
 #Method to generate random card
  def getRandomCard(deck):
     #generate any random card
    suit = random.randint(0, 3)
    rank = random.randint(0, 11)
    newCard = __init__(card, suit, rank)
    #check if card is in the deck, if not, keep making a new card
    while not(deck.contains(newCard)):
      suit = random.randint(0, 3)
      rank = random.randint(0, 11)
      newCard = __init__(card, suit, rank)
   
    #once we know card is in the deck, remove card from the deck and return the random card
      deck.removeCard(newCard)
    return newCard
