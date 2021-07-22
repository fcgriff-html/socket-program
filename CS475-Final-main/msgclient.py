import socket as sock
with sock.socket(sock.AF_INET, sock.SOCK_STREAM) as socky:#setting up socket connection
    localhost = '127.0.0.1'
    port = 9897
    socky.connect((localhost, port))
    breakoff = True
    count = 0
    while breakoff:
        if count == 0:
            print("say hi!")
            sendy = input("I said: ")
            conf = input("ready to send? (y/n): ")
            print("if you would like to play a game of Rock, Paper, Shoot, enter 'game'")
            count+=1
        else: 
            sendy = input("I said: ")
            conf = input("ready to send? (y/n): ")
            if sendy == "game":
              sendy = "game started"
              socky.send(sendy.encode())
              gamers = True
              while gamers: 
                print("enter '1': Rock, '2': paper, or '3': scissors") #remember to compare answers before sending messages
                shoot = input("choose wisely... :")
                socky.send(shoot.encode())
                recvy = socky.recv(1024).decode()
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
            socky.send(sendy.encode())
            msg = socky.recv(1024).decode()
            print("recieved: ", msg)
        if msg == "game started":
          gamers = True
          while gamers:
            print("enter '1': Rock, '2': paper, or '3': scissors")
            shoot = input("choose wisely... : ")
            socky.send(shoot.encode())
            recvy = socky.recv(1024).decode()
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
        if sendy == "bye" or sendy == "Bye" or sendy == "goodbye" or sendy == "Goodbye":
            breakoff = False
       

    
