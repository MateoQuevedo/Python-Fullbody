
"""
This function will create a plot representing the trainings of a certain user
"""

import pandas as pd

# This library will provide us the tools we need to plot the trainings
import matplotlib.pyplot as plt



def plotUsers(id):
    
        
        # We load the database with the users´information
        generalTable = pd.read_csv('DataUsers.csv')
                
        
        # We get the name and surname of the user, this will allow us to search and open his personal training file
        
        fileName = (generalTable.iloc[id-1,1]  
                    + generalTable.iloc[id-1,2] 
                    + 'Training.csv')
        
        
        # We open his excel personal file and show his last training
        df = pd.read_csv(fileName)
        

        plt.figure(figsize=(8,5))


        # plot the first line in blue, the second line in red and the third one in yellow
        plt.plot(df['Date'], df['Dead Lift'], 'b.-', label='Dead Lift')
        plt.plot(df.Date, df['Squads'], 'r.-', label='Squads')
        plt.plot(df['Date'], df['Bench'], 'y.-', label='Bench ')

        # Modify the xlabel to make it cleaner
        plt.xticks(df.Date)

        # Set the x-axis label
        plt.xlabel('Date')

        # Set the y-axis label
        plt.ylabel('Record [kg]')


        # Set the plot title
        plt.title('Gym records (' + generalTable.iloc[id-1,1] + ")")

        # add a legend to the plot
        plt.legend()

        # Show the plot
        plt.show()

         


