
"""
Let´s create a function newProfile() that will be called by the main body of the program whenever we have a new gym´s member 
This function will save his/her personal data in the general members csv and his/her training data in a private csv and

"""
import pandas as pd



def newProfile():
    
    #Let's create a profile for the newcomer:
    name = input("What is your name? ")
    last_name = input("What is your last name? ")
    age = input('How old are you?' )
    gender = input('Which gender do you identify with? \n')
    
 
    
    
    # We want to open the csv file 'DataUsers' and registe the newcomer
    df = pd.read_csv('DataUsers.csv')
    
    
    # We save in variable x the # of the last member who joined previously
    x = df.iloc[-1][0]
    
    # We create a Panda Series that will be added to our DataUsers File
    # Watch that we use x to give to the new member the next # number
    
    memberNumber = (x+1)
    
    df2 = pd.DataFrame([[memberNumber, name, last_name, age, gender]], 
                       columns=['Member #','First Name','Last Name', 'Age', 'Gender'])
    
    df = pd.concat([df, df2])
        
    # After adding the new user's information, we save the CSV file
    df.to_csv('DataUsers.csv',mode = 'w', index=False)
    
    
    # We save a dictionary with all this data from the new user. 
    # This program will return it, just in case we need it later
    Profile = {"Member Number": memberNumber,'Name': name, 'Last Name': last_name, 'Age': age, 'Gender': gender}
    
    
    
    
    # Let's create a csv file which saves all the records of his/her training
    print()
    print('Let´s write down the records of your first training: \n')
    
    date = input('What date is today? (Format: yyyy-mm-dd)')
    deadLift = input("Dead Lift? ")
    bench = input('Bench? ' )
    squads = input('Squads? ')
    print()
    
    training = pd.DataFrame([[date, deadLift, bench, squads]], 
                            columns= ['Date', 'Dead Lift', 'Bench', 'Squads'])
    
    #The name of the csv file that keeps track of everything will be his/her name + Training
    nameFile = name + last_name + 'Training.csv'
    
    training.to_csv(nameFile, mode = 'w', index = False)
    
    
    
    
    # We save a dictionary with all the data from training session from the new user. 
    # This program will return it, just in case we need it later
    LastTrainingSession = {'Date': date, 'Dead Lift': deadLift, 'Bench': bench, 'Squads': squads}

    return Profile, LastTrainingSession



