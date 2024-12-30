#This exercise made me wonder: How do we account for situations where caps sensitivity doesn't matter? Right now it does and it's cool for learning, but it's not practical for real world use.

#Declarations
import time
#
#
#Intro


print("  Fake Gamer Finder 👀")
print("=======================")
time.sleep(2)
print("Between Dead By Daylight, Overwatch, and Fortnite,")
favGame = input("which game is your favorite? ")


#
#DBD Module
if favGame == "Dead By Daylight" or favGame == "dead by daylight" or favGame == "Dead by daylight":
  favRole = input("What is your favorite role? Killer or Survivor? ")
  if favRole == "Killer" or favRole == "killer":
    print("Oh a killer main for once!")
    time.sleep (2)
    print("Who is your favorite base killer? Trapper, Hillbilly,")
    time.sleep (1)
    faveKiller = input(" Wraith, Nurse, or Huntress? ")
    if faveKiller == "Trapper" or faveKiller == "trapper":
      print("I don't gotta ask more. You're gaming!")
      time.sleep(2)
      print("So your favorite game is", favGame, ",your favorite role is", favRole, ",and your favorite base killer is", faveKiller)
      print("So cool!")
    if faveKiller == "Hillbilly" or faveKiller == "hillbilly":
      print("Insta down go burrrr")
      time.sleep(2)
      print("So your favorite game is", favGame, ",your favorite role is", favRole, ",and your favorite base killer is", faveKiller)
      print("So cool!")
    if faveKiller == "Wraith":
      print("You're a true gamer...")
      time.sleep(2)
      print("So your favorite game is", favGame, ",your favorite role is", favRole, ",and your favorite base killer is", faveKiller)
      print("So cool!")
    if faveKiller == "Nurse":
      print("You're a true gamer...")
      time.sleep(2)
      print("So your favorite game is", favGame, ",your favorite role is", favRole, ",and your favorite base killer is", faveKiller)
      print("So cool!")
    if faveKiller == "Huntress":
      print("Hmm.. What perk would you use in a build?")
      time.sleep (2)
      perkUsed = input("Darkness Revealed, Lithe, or Devour Hope? ")
      if perkUsed == "Darkness Revealed":
        print("Oooh, you're a true gamer!")
        time.sleep(2)
        print("So your favorite game is", favGame, ",your favorite role is", favRole, ",and your favorite base killer is", faveKiller)
        print("So cool!")
      else:
        print("You're a fake gamer... How could you...")
  if favRole == "Survivor":
    print("Tbh I dropped the ball here. Too much coding work for one exercise.")


#
#OW Module
if favGame == "Overwatch":
  time.sleep (2)
  favOwRole = input("What is your favorite role? Tank, Damage, or Support? ")
  if favOwRole == "Tank":
    time.sleep(2)
    knownTanks = input("Name 3 tanks you know.")
    time.sleep(2)
    print("Wait LOL I don't know how to check for 3 answers in one input. Fuck it, you pass!")
    time.sleep(2)
    print("But I do have to practice this concept called concatenation.")
    time.sleep(3)
    print("So here's a little descriptor of you.")
    time.sleep(2)
    print("You're a faggot")
    time.sleep(2)
    print("JK!")
    time.sleep(1)
    print("Your favorite game is", favGame, "and your favorite role is", favOwRole)
    time.sleep(2)
    print("You know the following tanks:", knownTanks)

  if favOwRole == "Damage":
    print("You have skill... I respect that")
  if favOwRole == "Support":
    print("You have skill... I respect that")


#
#FN Module
if favGame == "Fortnite":
  print("You're in luck bc idk jack shit about Fortnite")
  time.sleep(2)
  print("I guess you're a gamer by default idk")