import socket as sock

with sock.socket(sock.AF_INET, sock.SOCK_STREAM) as socky: #sets up socket connection to client
    port = 9897
    socky.bind(('0.0.0.0', port))
    socky.listen(5)
    client, clidress = socky.accept()
    print("the socket connected to: ", clidress) #sanity check
    breakoff = True
    while breakoff:
        msg = client.recv(1024).decode()
        print("response: ", msg)
        if msg == "game started":
          gamers = True
          while gamers:
            print("enter '1': Rock, '2': paper, or '3': scissors")
            shoot = input("choose wisely... : ")
            client.send(shoot.encode())
            recvy = client.recv(1024).decode()
          #process this info and return the results to the players
            if shoot == recvy:
              print("you and your opponet have tied, try again")
              gamers = True
            if (shoot == "1" and recvy == "2") or (shoot == "2" and recvy == "3") or (shoot == "3" and recvy == "1"):
              print("You have lost! ... *sad wario noises* ")
              gamers = False
            if (shoot == "2" and recvy == "1") or (shoot == "3" and recy == "2") or (shoot == "1" and recvy == "3"):
              print("You have won! ... *Nyan cat is pleased* ") 
              gamers = False 
        print("to start a game of rock, paper, scissors, enter 'game' ")
        sendy = input("I said: ") #to help format the file
        conf = input("ready to send? (y/n): ") #another sanity check
        if sendy == "game":
          sendy = "game started"
          client.send(sendy.encode())
          gamers = True
          while gamers: 
            print("enter '1': Rock, '2': paper, or '3': scissors") #remember to compare answers before sending messages
            shoot = input("choose wisely... :")
            client.send(shoot.encode())
            recvy = client.recv(1024).decode()
            #process this info and return the results to the players
            if shoot == recvy:
              print("you and your opponet have tied, try again")
              gamers = True
            if (shoot == "1" and recvy == "2") or (shoot == "2" and recvy == "3") or (shoot == "3" and recvy == "1"):
              print("You have lost! ... *sad wario noises* ")
              gamers = False
            if (shoot == "2" and recvy == "1") or (shoot == "3" and recy == "2") or (shoot == "1" and recvy == "3"):
              print("You have won! ... *Nyan cat is pleased* ") 
              gamers = False 
        if conf == "y":
              client.send(sendy.encode())
        if sendy == "bye" or sendy == "Bye" or sendy == "goodbye" or sendy == "Goodbye": #break case
              breakoff = False
    client.close()
#C:\Users\charl\Documents\GitHub\CS475-Final