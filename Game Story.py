print('''                 $$$$$$$$$$$$$$$$$$$$$$$
                       uuu$$$$$E""""~~~~~""""$$$$$$uuu
                    u9$$$$"""                   """$$$$ku
  ud$$$$$$$$&uuuuu9$$F"                               "9$$ku
'$$$$"""""""#$$$$$$$                                     $$$$>
  "#$$$$-._   $$$$>                                       9$$$$
     """$$$$$$$$$.                                          $$$$
           $$$$$$$$$uuu..__                                  9$$$E
           $$$$E """***$$$uuu...__                           9$$$E.
           $$$$E       """***$$ILoveyou...__                    9$$$$$ec.
           $$$$E             ""?****$$$eeeec..._             9$$$E"**$ec.
           "?$$Ne                   """*****$$Neeee...._    e@$$""  '"$$$ec
            '"$$$e>                        '""?****$$$$beeee$$$?......??$$Ne
              "?$$be                               """"#*$$$$$$$$$$$$$$$$*#"
               '"*$$e:.                               .se$**"""""""""""""
                  ^"*$$eee...                   ...eee$**"
                     ^"***$$$eec...._____....eee$$$***"
                          """***$$$$$$$$$$$$$***"""
                               '"""""""""""""''')
print("You became an astronaut\n")

choice1 = input('You find yourself on a spaceship near the planet Saturn. Do you want to "land" on Saturn or "explore" its moons?\n ').lower()
if choice1 == "explore":
   choice2 =input('You descend through Saturns atmosphere. Do you "land" on the surface or "probe" the planets rings?\n').lower()

else:
    print("You cannot landing on Satrun. You lose!\n")
if choice2 == "land":
   choice3 =input('When You are discovering on Saturn. Do you want  "discovering " or "Talk" to aliens? \n'.lower())
   
else:
    choice2 = "probe"
    print("You lose control and crash into the planet's!\n")
    
if choice3 =="discovering":
    print("You uncover a powerful artifact that grants you incredible abilities. Congratulations, you win!\n")
    
else:
    print("Aliens killed you\n")



