'''Implements the game data and logic and features the dice roll/sum functions as well as the point system functions for all levels'''
import random # The random module is a module present in the original Python Library that chooses a random number within a required range
import Role1  # The Role 1 module is the module featuring the attributes for Jay with the inital values for his special powers
import Role2  #The Role 2 module is the module featuring the attributes for Rosé with the initial values for her special powers


# The following function will be used in all of the dice rolls. It assigns two variables dice 1 and dice 2.
#Then the random module and randint is used to roll a random integer between 1-6 for both dice.
#Then a variable called Total_d1_d2 is assigned which sums up the integer values recieved from dice 1 and dice 2. Then that value is returned.
def rollDice():
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    Total_d1_d2=dice1+dice2
    return Total_d1_d2

# Level 1 success checker: This function will be used to check if the sum of the two dice was between 4-12.
#This has to be done in 3 tries or else the function quits and the game ends

def RollSuccessChecker1():   
    #The following for loop rolls the dice three times to see if the user has been able to get the sum between 4-12.
    for index in range(3):                             
        current_roll=rollDice()       #Uses the dice roll function to roll dice and add sum

        print(current_roll)            #Prints the acquired values above for user interactivity
        if current_roll in range(4,13):       #This if statement checks to see if the sum is within 4-12.
            s=1                                  #The value of s which will be returned at the end determines if the check was succesful.
            print('Congratulations you have completed this level!')
            return s
        else:
            continue                   #If the required range was not met, it loops again
    #for loop is done
    print('You have run out of tries, Neil is now possessed. Game Over')  # Once the user has used up all 3 tries, the game is over and that is printed
    exit()   #Since the game is over if 3 tries are used, the function quits the program and ends it.
    

# The rest of the success checkers work the exact same way as the first success checker. The only difference is the range
#changes based on the level as mentioned in the instructions and game play rules.

#Level 2 Success Checker
def RollSuccessChecker2():
    #The following for loop rolls the dice three times to see if the user has been able to get the sum between 2-10.
    for index in range(3):                             
        current_roll=rollDice()

        print(current_roll)  
        if current_roll in range(2,11):
            s=1                                  #The value of s which will be returned at the end determines if the check was succesful.
            print('Congratulations you have completed this level!')
            return s
            #break
        else:
            continue
    #for loop is done
    print('You have run out of tries, Neil is now possessed. Game Over')
    exit()

#Levell 3 Sucess Checker
def RollSuccessChecker3():
    #The following for loop rolls the dice three times to see if the user has been able to get the sum between 2-8.
    for index in range(3):                             
        current_roll=rollDice()

        print(current_roll)  
        if current_roll in range(2,9):
            s=1                        #The value of s which will be returned at the end determines if the check was succesful.
            print('Congratulations you have completed this level!')
            return s
            #break
        else:
            continue
    #for loop is done
    print('You have run out of tries, Neil is now possessed. Game Over')
    exit()


#Level 4 Success Checker
def RollSuccessChecker4():
    #The following for loop rolls the dice three times to see if the user has been able to get the sum between 2-6.
    for index in range(2):                             
        current_roll=rollDice()

        print(current_roll)  
        if current_roll in range(2,7):
            s=1                      #The value of s which will be returned at the end determines if the check was succesful.
            print('Congratulations you have completed this level!')
            return s
            #break
        else:
            continue
    #for loop is done
    print('You have run out of tries, Neil is now possessed. Game Over')
    exit()


#The following functions are used for the points system which will add points to each player once they have completed a level
# These points they acquire at each level unlocks a special powerup for each level which helps the player complete that level.
#Plus, these points are stored and added after each level so they can be used to get the Magic Carpet on the last level needed to finish the game.


#Level 1 points system
#The following function will require the program to pass a parameter called character which is defined at the start.
#Then it checks to see what the parameter and assigns points accordingly.
def Level1points(character):
    if character=='Jay':
        print('You have also gained 10 points for Night Vision ')  # Print statement to let user know how many points they have achieved for which powerup
        JaypointsL1=int(Role1.Nightvision +10) # Assigns a variable for Jay in Level 1, access the role 1 modules variable called NightVision and finds it's value and add's 10 to it
        return JaypointsL1  #Returns the new value for this variable
      #This function works the same way for Rosé but she just has different initial values for each superpower.  
    else:
        character=='Rosé'
        print('You have also gained 10 points for Night Vision ')
        RosépointsL1=int(Role2.Nightvision+10)
        return RosépointsL1


#The rest of the point systems work the exact same way as the first. The only difference is the differet initial values for each character which are accedded from the Role 1 and Role 2 modules
# and the points which are added based on the level, it is 20 points in level 2, 30 in level 3 and then level 4 adds 50 points but level 4 is not mentioned in this module.     

#Level 2 points system
def Level2points(character):
    if character=='Jay':
        print('You have also gained 20 points for Strength')
        JaypointsL2=int(Role1.Strength+20)
        return JaypointsL2
        
    else:
        character=='Rosé'
        print('You have also gained 20 points for Strength ')
        RosépointsL2=int(Role2.Strength+20)
        return RosépointsL2
        

#Level 3 points system
def Level3points(character):
    if character=='Jay':
        print('You have also gained 30 points for Health ')
        JaypointsL3=int(Role1.Health +30)
        return  JaypointsL3
    else:
        character=='Rosé'
        print('You have also gained 30 points for Health')
        RosépointsL3=int(Role2.Health+30)
        return RosépointsL3


# The reason why Level 4 is not included in this module as a function is because it requires the program to add up all the point values
# for the past three levels then add 50 for finishing level 4 to that total value. Adding a function for level 4 would be difficult because
#those variables which are the totals for each level are not used in this module. Since you cannot access those variables, you cannot use them properly.
#which is why a seperate addition statement is used for this purpose in the app.py.

       

















