
"""
This function will open the excel file of a certain user and update it
"""

import pandas as pd


def updateProfile(id):
    

     # We load the database with all the users´ information
     df = pd.read_csv('DataUsers.csv')
     
     
     
     # We get the name and surname of the user, this will allow us to search and open his personal training file
     # We save the name to make the app more user-friendly
     
     name = (df.iloc[(id-1),1])
     
     fileName = (name + df.iloc[id-1,2] + 'Training.csv')
     
          
     
     # We open his excel personal file and show his last training
     df = pd.read_csv(fileName)
     
     print('This is the data about your last training, ' + name + ': \n')
     print(df.iloc[-1])
     
    
          
     # Let's ask about the new training
     print()
     print('Let´s write down the records of today´s training: \n')
     
     date = input('What date is today? (Format: yyyy-mm-dd)')
     deadLift = input("Dead Lift? ")
     bench = input('Bench? ' )
     squads = input('Squads? ')
     print()
     
     training = pd.DataFrame([[date, deadLift, bench, squads]], 
                             columns= ['Date', 'Dead Lift', 'Bench', 'Squads'])
     
     
     #¶ We add the new data to the excel file of the user
     df = pd.concat([df, training])
         
     
     # After adding the new user's information, we save the CSV file
     df.to_csv(fileName, mode = 'w', index=False)
     
     

     return 

