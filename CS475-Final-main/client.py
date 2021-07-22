import socket as sock
from goFish import *

host = socket.gethostname()
port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host,port))

message = socket.recv(4096)

if message.startswith("1"):
  card_id = message[1]
  # do stuff to check if card is in player's hand,
  # then send appropriate message back
  
elif message.startswith("2"):
  card_id = message[1]
  cardAmount = message[2]
  # do stuff to add cards to player's hand
  
elif message.startswith("3"):
  # add a random card from the deck to the player's hand
    pass