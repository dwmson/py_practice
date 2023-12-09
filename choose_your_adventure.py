def play_game():
  print("Welcome to the Choose Your Own Adventure game!")
  print("Your mission is to find the lost treasure of the dread pirate, Blind Beard!... He's blind, okay? he can't see where he hid the treasure")
  print("\n")
  crossroads = input("While walking, you arrive at a crossroads, do you go left or right?\n").lower()
  if crossroads == "left":
    lake = input("You came to a lake, you spot an island in the middle of the lake, do you wait for a boat? or try to swim to the island? Type \"wait\" or \"swim\". \n")
    if lake == "wait":
      door = input("You come across three cave entrances. Which entrance do you take? Type \"left\", \"middle\", or \"right\". \n")
      if door == "left":
        print("You found the treasure! You WIN! :D")
      elif door == "middle":
        print("Blind Beard accused you to be a thief and shot you. Game over :(")
      else:
        print("You found a robot in the cave who ate your soul out of your head. Game over :(")
    else:
      print("You were eaten by a Kraken in the lake. Game over :(")
  else:
    print("You fell into a pit and died. Game over :(")

play_again = "Y"
while play_again == "Y":
    play_game()
    play_again = input("Would you like to play again? (Y/N) ").upper()
