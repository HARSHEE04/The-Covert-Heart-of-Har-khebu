#Used as a duplicate of the app.py to work out game flow design

import tkinter.messagebox as ms
import random
import time
import Game
import Role1
import Role2

#Introduction, setting the plot and explaining the characters and gameplay rules
ms.askyesno(title='Welcome',message='Are you ready to play The Covert Heart of Har-khebu?')
ms.showinfo('Background', message='Jay, Rosé, and Neil had always been fascinated by the ancient Egyptian pyramids. So when they finally had the chance to visit the pyramids in person, they jumped at the opportunity.As they explored the pyramids, they could not help but feel a sense of awe and wonder. But as they delved deeper into the pyramids, they began to notice strange occurrences. The hieroglyphics on the walls seemed to shift and change shape before their eyes, as if they were trying to convey a message, maybe a warning? Neil, the most sceptical of the three, was suddenly pulled away from the group and disappeared into a dark side passage. Jay and Rosé called out to him, but got no response. As they continued to search, they began to notice strange symbols etched into the walls. They looked like hieroglyphics, but they seemed to pulse with a malevolent energy. And then, in the centre of one of the symbols, they saw a figure standing. It was Neil, but he was different. His eyes were dark and empty, and his skin was deathly pale.Rosé felt a chill run down her spine. "We have to get him out of here," she whispered to Jay. "This place is cursed."The hieroglyphics on the walls formed a message “ To free your friend, you must pass through the four layers of the cursed pharaoh Har-khebu and get to the fourth layer, the heart, which is where your friend will be found. Each layer has a different form of the pharaoh that must be defeated using your intelligence and luck. Good luck!”')
ms.askyesno(title='Game Play Rules', message='There are four levels in this game in increasing order of difficulty. You must complete all four to save Neil! Each level will require you to roll two dice. To pass the level, the sum of the two rolled dice must add up to the range mentioned in the instructions. If you fail to obtain the sum in the given rolls, the game ends and Niel is possessed by the  Har-khebu. The rest of the game will take place in the terminal. You will first be granted a character either Jay or Rosè. Shall we begin?')

#Character choice

character=input('Who would you like to play as, Jay or Rosé?')

if character=='Jay':
    print(f'Welcome,{Role1.name},Let us begin')
elif character=='Rosé':
    print(f'Welcome  {Role2.name}, Let us proceed to level 1')
else:
    print('Sorry, I did not understand that please try restarting the game')
    quit()



ms.showinfo(title='Initiating', message='LEVEL 1')
time.sleep(3)  # gives a pause in between the messages using the time module


#Level1


print('-------------------------------------------------------------------------------------------------------------------------------')
print('Welcome to level 1! To beat this level, you must obtain lazer night vision to burn the flesh form of Har-khebu. To do this, you must roll the dice and obtain a sum between 4-12. You will have three tries after which it is game over for Neil')
print('-------------------------------------------------------------------------------------------------------------------------------')
print('The dice is now being rolled and the sum is being calculated')
#use the RollSuccessChecker to roll the dice and see if player moves onto the next level

time.sleep(5)
level1=Game.RollSuccessChecker1()
L1points=Game.Level1points(character)
# if character=='Jay':
#     print('You have also gained 10 points for Night Vision ')
#     JaypointsL1=Role1.Nightvision +10
#     print('You now have',JaypointsL1,'total points')
# else:
#     character=='Rosé'
#     print('You have also gained 10 points for Night Vision ')
#     RosépointsL2=Role2.Nightvision+10
#     print('You now have', RosépointsL2,'total points')


ms.showinfo(title='Initiating', message='LEVEL 2')
time.sleep(5)  # gives a pause in between the messages using the time module

#Level 2

print('-------------------------------------------------------------------------------------------------------------------------------')
print('Welcome to level 2! To beat this level, you must obtain Inhumane Strength which will allow you to win in the boxing fight against the Wolf form of the pharaoh. To do this, you must roll the dice and obtain a sum between 2-10. Again, you have three tries to achieve this or else it is game over.')
print('-------------------------------------------------------------------------------------------------------------------------------')
print('The dice is now being rolled and the sum is being calculated')
#use the RollSuccessChecker to roll the dice and see if player moves onto the next level

time.sleep(5)
Level2=Game.RollSuccessChecker2()



ms.showinfo(title='Initiating', message='LEVEL 3')
time.sleep(5)  # gives a pause in between the messages using the time module


#Level 3
print('-------------------------------------------------------------------------------------------------------------------------------')
print('Welcome to level 3! To beat this level, you must obtain Imortal Health to beat the Dracula form of pharaoh. To do this, you must roll the dice and obtain a sum between 2-8. Again, you have three tries to achieve this or else it is game over.')
print('-------------------------------------------------------------------------------------------------------------------------------')
print('The dice is now being rolled and the sum is being calculated')
#use the RollSuccessChecker to roll the dice and see if player moves onto the next level

time.sleep(5)
Level3=Game.RollSuccessChecker3()


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
Level4=Game.RollSuccessChecker4()


#Print congratulations message for completion of the game
time.sleep(7)
ms.showinfo(title='CONGRAULATIONS!')
