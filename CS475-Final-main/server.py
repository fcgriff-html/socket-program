""" 
based on chatting example from https://stackoverflow.com/questions/21233340/sending-string-via-socket-python

"""
import socket as sock
from goFish import *

def socket_setup():
    s = sock.socket()
    port = 12345
    s.bind(('', port))
    s.listen(5)
    c, addr = s.accept()
    #just a sanity check
    print("socket connected!")

    return s, c
"""
def send_n_recieve(s, c):
    
    **Params**
    s: Host socket 
    c: client socket

    while True:
        recmsg = c.recv(1024).decode()
        turn = int(recmg[-1])
        turn+=1
        card_search = raw_input("Please enter the card you are looking for: ")
        sendmsg = card_search + turn
"""

class Game_run:
    def __init__(self):
        self.winner==""
        self.turn = 0
        self.opponet_hand = []
        self.player_hand = []
        self.fishing_pile = []
        self.game_state = "running"

    def shuffle_n_split(self):
        cards = np.zeros(52)
        split = []
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
                self.player_hand.append(split[i])
            else:
                self.opp_hand.append(split[i])
       #now that we have split the selected cards into two hands, we need to populate the fishing pile
        for i in range(len(cards)):
            if i not in idx_trace:
                self.fishing_pile.append(cards[i])
        return idx_trace
    def go_fish(self, turn_holder_hand, card_id):
        card_steal = []
        if turn_holder_hand != self.player_hand:
            for i in range(len(self.player_hand)):
                if self.player_hand[i] == card_id:
                    #remove card from player hand, go fish, add to opp hand
                    card_steal.append(self.player_hand[i])
                    self.player_hand.pop(i)
                    self.player_hand = fishing(self.player_hand)
                    self.opponet_hand += card_steal        
        else:
            for i in range(len(self.opponet_hand)):
                if self.opponet_hand[i] == card_id:
                    card.steal.append(self.opponet_hand[i])
                    self.opponet_hand.pop(i)
                    self.opponet_hand = fishing(self.opponet_hand)
                    self.player_hand += card_steal
        return 0
    def fishing(hand):
        if len(hand) < 7:
            #we draw cards until it is 7
            hand.append(self.fishing_pile[1])
            self.fishing_pile.pop(1)
            fishing(hand)
        return hand
def main():
    s = socket.socket()
    port = 12345
    s.bind(('', port))
    y = input("please press y to start: ")
    if y == "y":
      game = Game_run()
      turn = 0
      idx = game.shuffle_n_split()
      player = game.player_hand
      opp = game.opponet_hand
      pile = game.fishing_pile
      print("opponet goes first!")
      while len(pile) != 0:
            s.listen(5)
            c, address = s.accept()
            while True:
                data = c,recv(1024).decode()
                print("looking for ... : ", data[0:2])
                game.go_fish(opp, data[0:2])
                game.fishing_pile(player)
                print("your turn! Your cards are: ", player)
                print(" 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, Jack: J, Queen: Q, King: K, Ace: A")
                send = input("please enter the card you are looking for: ")
                c.send(send.encode())
            c.close()
    

if __name__ == "__main__":
    main()
    







