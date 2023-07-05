""" 
 Main body of the FullBody program, it must be always iniciated from here 
 
 For the correct functioning of this programme, we need the following files in the same folder:
     
 Program.py    
 firstTimeApp.py
 newProfile.py
 udpateProfile.py
 plotUser.py    
     
"""

## This library provides us the funcion sys.exit(), which finishes the program
import sys

# Import the pandas package under the name pd
import pandas as pd

## This function will create a new profile for a new user
import newProfile

# This function will open the excel file of a certain user and update it
import updateProfile

## This function will generate a plot with the user's records
import plotUsers

## This function will check that everything is ready to start
import firstTimeApp


firstTimeApp.firstTimeApp()




print('\n Welcome to the Full Body program app')

x = input("Is this your first time in the app? (y/n) ")

if (x == 'y'):
    
    print('First time')
    
    # Let´s call the newProfile´s program to create a new profile
    Profile, LastTrainingSession = newProfile.newProfile()
    
    print('So this is your data: \n')
    print(Profile)
    print()
    
    print('And this is your record after your first day: \n')
    print(LastTrainingSession)
    
    
    
    
elif (x == 'n'):
    
    # In the case of dealing with a user with previous experience, let´s start printing his/her personal data from the users database
    print('Already a member \n')

    # We load the database with the users´information
    df = pd.read_csv('DataUsers.csv')

    # Now we are going to ask the user for his/her ID and show his/her info. In case of a wrong ID, we handle the error
    switch = False
    while (switch == False):
         
        try:
            
            # We ask for the member ID
            id_user = int(input("What is your member number/id? "))
            print()
            
            
            # We check that the number inserted is not higher than the number of users
            Number_Users = int(str(df.iloc[-1][0]))
            
            # If that the case, we have an error and we ask again for the ID                        
            if (id_user > Number_Users):
                
                raise ValueError('We dont have that many users.')
               
      
        # This exception also catches if the user inserts something that is not a number
        except ValueError as e:
            print(e)
            print("There was a problem. Are you sure that was your ID? Please, try again")
            
                
        else:
            # We create a mask that will help us print just the information related to this specific member
            mask = df['Member #'] == id_user
            print(df[mask]) 
            switch = True
            
            
    # Now we ask the user if he wishes to update his profile or see a plot with his records
    z = input("What do you wish to do? (u for update profile / p for watching records / anything else for finishing using this app) ") 
    print()
    
    if (z == 'u'):
        updateProfile.updateProfile(id_user)
        print("Thanks for using this app")
        
    elif (z == 'p'):   
    
        plotUsers.plotUsers(id_user)
        print("Thanks for using this app")
        
    else:
        print("Thanks for using this app")
        sys.exit()


else:
    print("Wrong answer, closing the app143")
    sys.exit()
 
    
 
    
 
    