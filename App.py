'''Implements the interactivity with the user'''
import tkinter.messagebox as ms   #imports the tkinter module available in the standard Python Library and specifically imports the message box as ms.
import random   #Random module found in the Standard Python Library which generates a random number within a required range
import time     # This time module found in the Python Standard Library helps delay execution for a set time
import Game    # This is the module I created which has all the game logic and game data
import Role1   #This is the module I created for Jay and it features his attributes ( Superpowers)
import Role2   #This is the module I created for Rosé and it features her attributes(Superpowers)

#Introduction, setting the plot and explaining the characters and gameplay rules
ms.askyesno(title='Welcome',message='Let us start play Covert Heart of Har-khebu?')  # Asks the user if they are ready to play using the askyesno function found within the messagebox module in Tkinter.
#The line below uses the showinfo function in message box found within the Tkinter module to explain the background story to the user
ms.showinfo('Background', message='Jay, Rosé, and Neil had always been fascinated by the ancient Egyptian pyramids. So when they finally had the chance to visit the pyramids in person, they jumped at the opportunity.As they explored the pyramids, they could not help but feel a sense of awe and wonder. But as they delved deeper into the pyramids, they began to notice strange occurrences. The hieroglyphics on the walls seemed to shift and change shape before their eyes, as if they were trying to convey a message, maybe a warning? Neil, the most sceptical of the three, was suddenly pulled away from the group and disappeared into a dark side passage. Jay and Rosé called out to him, but got no response. As they continued to search, they began to notice strange symbols etched into the walls. They looked like hieroglyphics, but they seemed to pulse with a malevolent energy. And then, in the centre of one of the symbols, they saw a figure standing. It was Neil, but he was different. His eyes were dark and empty, and his skin was deathly pale.Rosé felt a chill run down her spine. "We have to get him out of here," she whispered to Jay. "This place is cursed."The hieroglyphics on the walls formed a message “ To free your friend, you must pass through the four layers of the cursed pharaoh Har-khebu and get to the fourth layer, the heart, which is where your friend will be found. Each layer has a different form of the pharaoh that must be defeated using your in-built supoerpowers. Good luck!”') 
ms.askyesno(title='Game Play Rules', message='There are four levels in this game in increasing order of difficulty. You must complete all four to save Neil! Each level will require you to roll two dice. To pass the level, the sum of the two rolled dice must add up to the range mentioned in the instructions. If you fail to obtain the sum in the given rolls, the game ends and Niel is possessed by the  Har-khebu.  If you succeed in passing the level, you move onto the next and points are added to your in built superpowers which are Night Vision, Strength and Health. These added points will help you gain access to the Magic Carpet needed to escape this haunted place.The rest of the game will take place in the terminal. You will first be granted a character either Jay or Rosè. Shall we begin?')

#The user is given a choice between the two characters.
character=input('Who would you like to play as, Jay or Rosé?') # User asked which character they would like to be
#The if statement below prints the welcome message after the character has been chosen. If they user types an answer that isnt one of the two characters name, the game quits and they are told to start again.
if character=='Jay':
    print(f'Welcome,{Role1.name},Let us begin')    #Uses the variable name present in the Role1 module created by me to access the word Jay
elif character=='Rosé':
    print(f'Welcome  {Role2.name}, Let us proceed to level 1')    #Uses the variable name present in the Role 2 Module created by me to access the word Rosé
else:
    print('Sorry, I did not understand that please try restarting the game')  #This is the forementioned quit()statement if the user did not select a proper name
    quit()

#After the character has been chosen, a message is printed that states that level 1 is starting.
ms.showinfo(title='Initiating', message='LEVEL 1')
time.sleep(3)  # gives a pause in between the messages using the time module and the sleep function 


#Level1
print('-------------------------------------------------------------------------------------------------------------------------------')
print('Welcome to level 1! To beat this level, you must obtain lazer night vision to burn the flesh form of Har-khebu. To do this, you must roll the dice and obtain a sum between 4-12. You will have three tries after which it is game over for Neil')
print('-------------------------------------------------------------------------------------------------------------------------------')
print('The dice is now being rolled and the sum is being calculated')
#use the RollSuccessChecker1 in the game module to roll the dice and see if player moves onto the next level

time.sleep(5) #Delay the dice roll for effect
Level1rollsum=Game.RollSuccessChecker1()  #Assign a variable called level1rollsum, use module game to access the function RollSuccessChecker1 and get an output
L1points=Game.Level1points(character)   #Assign points to the character for winning the level using the Level1points function that assigns points to the chosen character.

#Show message that Level 2 is starting
ms.showinfo(title='Initiating', message='LEVEL 2')
time.sleep(5)  # gives a pause in between the messages using the time module


#Level 2
print('-------------------------------------------------------------------------------------------------------------------------------')
print('Welcome to level 2! To beat this level, you must obtain Inhumane Strength which will allow you to win in the boxing fight against the Wolf form of the pharaoh. To do this, you must roll the dice and obtain a sum between 2-10. Again, you have three tries to achieve this or else it is game over.')
print('-------------------------------------------------------------------------------------------------------------------------------')
print('The dice is now being rolled and the sum is being calculated')
#use the RollSuccessChecker2 to roll the dice and see if player moves onto the next level

time.sleep(5)
Level2rollsum=Game.RollSuccessChecker2() #Does the exact same thing as line 38 except with the RollSuccessChecker2 which checkes if the sum is between 2-10 and assigns it to the variable called Level2rollsum.
L2points=Game.Level2points(character)  #Does the exact same thing as line 39 except it assigns 20 points for Strength 


#Show message that Level 3 is starting
ms.showinfo(title='Initiating', message='LEVEL 3')
time.sleep(5)  # gives a pause in between the messages using the time module


#Level 3
print('-------------------------------------------------------------------------------------------------------------------------------')
print('Welcome to level 3! To beat this level, you must obtain Imortal Health to beat the Dracula form of pharaoh. To do this, you must roll the dice and obtain a sum between 2-8. Again, you have three tries to achieve this or else it is game over.')
print('-------------------------------------------------------------------------------------------------------------------------------')
print('The dice is now being rolled and the sum is being calculated')
#use the RollSuccessChecker to roll the dice and see if player moves onto the next level

time.sleep(5)
Level3rollsum=Game.RollSuccessChecker3() #This does the exact same thing as before except is uses the RollSuccessChecker3 which checks to see if the range of the sum is between 2-8.
L3points=Game.Level3points(character) #Assigns Health points to the chosen character and gets the total health points present for them.


#Show message that Level 4 is starting
ms.showinfo(title='Initiating', message='LEVEL 4')
time.sleep(5)  # gives a pause in between the messages using the time module


#Level 4
print('-------------------------------------------------------------------------------------------------------------------------------')
print('Welcome done warrior! You have made it far, your bravery is something to applaud! Now, focus up. To beat this last level, you must obtain  gain access to the magic carpet and the Ethereal Sword with which you will defeat the Phantom form of the pharaoh and use the magic carpet to escape the pyramid.')
print('To do this, you must roll the dice to get the sum between 2-6 with only two tries!')
print('-------------------------------------------------------------------------------------------------------------------------------')
print('The dice is now being rolled and the sum is being calculated')
#use the RollSuccessChecker to roll the dice and see if player moves onto the next level

time.sleep(5)
Level4=Game.RollSuccessChecker4() #Uses the RollSuccessChecker4 fuction present in the Game module to see if the sum of the two rolled dice is between 2-6.
totalpoints=((int(L1points))+(int(L2points))+(int(L3points))+50)  #Since the user has now passed all 4 levels, we add the total points they have and add 50 points to their total count for completing level 4.
#Keep in mind, to win the game, the player needed to pass all levels and at least 103 total points from all the levels. If they have greater than or equal to 103 points, then they get access to the magic carpet which they need to escape the haunted pyramid.
print('You gained',totalpoints,'so you have gained access to the magic carpet too!') #Prints out the total points for the user

#Print congratulations message for completion of the game
time.sleep(7) #Delay message for effect.
ms.showinfo(title='CONGRAULATIONS!', message='Well done!! You have succesfully rescued Neil and have opened the portal to the outside world. Thank you for playing:)')




