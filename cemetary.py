print('''
*******************************************************************************
                  _  /)
                 mo / )
                 |/)\)
                  /\_
                  \__|=
                 (    )
                 __)(__
_________+______/      \______+__________
  __--   |       R.I.P.       |-_-- __
_-- -    | ___ __________ ___ |
-_-- __  || | | | {|    /| | || __---  -_
 --__-   || | | | {|   /|| | ||--        -
         || | | | {|  /||| | ||__--
 __-- -__|| | | | {| |}||| | ||--   __--
         ||_|_|_|_{| |}|||_|_||  -__
 --__-  -|| | | | {& |}||/ | ||---   __--
         || | | | {| |}|/| | ||-__
--   __--|| | | | {| |}/|| | ||__-- -__
  --     || | | | {| &}||| | ||   __
---   __-|| | | | {| |}||| | ||_---__-  --
 -  -_   || | | | {| |}||| | || --
 __ejm 97|| | | | {| |}||| | ||_--__-   _---
_________||_|_|_|_{| |}|||_|_||______________
                     |}|/
                     |}/
                     |/
                               _                   
                              | |                  
  ___ ___ _ __ ___   ___ _ __ | |_ __ _ _ __ _   _ 
 / __/ _ \ '_ ` _ \ / _ \ '_ \| __/ _` | '__| | | |
| (_|  __/ | | | | |  __/ | | | || (_| | |  | |_| |
 \___\___|_| |_| |_|\___|_| |_|\__\__,_|_|   \__, |
                                              __/ |
                                             |___/ 
                     
*******************************************************************************
''')
#Introduction to game
print("Welcome to the Cementary.")
print("Your mission is to escape alive!")

#Game Over Prompt
restart = "no"
def gameover():
  print("You have died.")
  restart()
  
def restart():  
  restart = input("Type 'yes' to play again.\n")
  restart = restart.lower()
  if restart == "yes":
    main()
  else:
    main()

def main():
  #First Prompt 
  print("You wake up in a dark room. You also hear spewing and screaming.")
  answer = input("Type 'scream' to call for help or type 'look' to look for a door.. \n")
  answer = answer.lower()


  if answer == "look":
    print("You look for a door and find one.")
    print("You walk through the door and find a table with a sword, a bow, and a knife.")
  
  else:
    print("You scream at the top of your lungs and ... nobody hears you.")
    print("You scream again and ... nobody hears you.")
    print("You scream again and ... nobody hears you..")
    gameover()


  answer1 = input("Which weapon do you choose? Type 'sword', 'bow', or 'knife' \n")
  answer1 = answer1.lower()
  
  if answer1 == "bow":
    print("You walk up to the bow and take it but you hear a noise behind you!")
    print("You turn around and see a giant bear running from the wall. You shoot it!\n")
  elif answer == "sword":
    print("You walk up to the sword and take it.")
    print("You hear a noise behind you!")
    print("You turn around and see a giant bear running from the wall. It slaps the sword out of your hand!")
    gameover()
  else:
    print("You walk up to the knife and take it but you hear a noise behind you!.")
    print("You turn around and see a giant bear running from the wall. It slaps the knife out of your hand!")
    gameover()
  print("You buy some time and try to look for a way out...")
  print("You see a window to the outside, stairs going to the cellar, and a door to the north.")
  answer2 = input("How would you like to escape? Type 'window', 'stairs', or 'door'.\n")
  
  answer2 = answer2.lower()
  
  if answer2 == "window":
    print("You climb through the window and find your way out. \n You run out of the cementary and escape!")
    print("You win!")
    restart()
    
  elif answer2 == "stairs":
    print("You slowly walk down the stairs and it starts to get darker the more you walk.")
    print("The light dims even more..")
    print("Into the darkness, you are consumed...")
    gameover()
  else: 
    print("You walk through the door and run into a family of bears!!")
    print("You shoot your last arrow and try to run back through the door.")
    print("The bear catches you and tackles you.")
    gameover()
main()

#git config --global user.email yournew@email.com
#git config --global user.name yournewgoodname