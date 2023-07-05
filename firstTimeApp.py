
"""
In this program we will make sure that the file containing Data from users exists
If not, it will be created
"""

## If you want to save the CSV file in the same directory as the current Python script or Jupyter Notebook, you can use the __file__ attribute to get the path of the current script, and then manipulate it to create the file path for the CSV file
## In this example, the os module is used to work with file paths. The os.path.abspath(__file__) function gives the absolute path of the current script, and os.path.dirname() extracts the directory path. Then, os.path.join() is used to combine the directory and file name to create the final file path for the CSV file.
import os


# Import the pandas package under the name pd
import pandas as pd


def firstTimeApp():
    print()
    
    
    try:
        # We want to check that the csv file 'DataUsers' exists
        df = pd.read_csv('DataUsers.csv')
        
    
    except:
        # If there is a problem loading the database, we will come here
        # We will create a database that will save the data of the users
        # This database will have by default a first user called John Smith
        
        data = [{'Member #': 1, 'First Name': 'John', 'Last Name': 'Smith', 'Age': 35, 'Gender': 'Male'}]
        
        df = pd.DataFrame(data)
        
        # Get the path of the current script
        current_path = os.path.abspath(__file__)

        # Extract the directory path
        directory = os.path.dirname(current_path)
        
        # Create the file path by joining the directory and file name
        file_path = os.path.join(directory, 'DataUsers.csv')
        
        # Create the csv file "DataUsers"
        df.to_csv(file_path, index=False)
        
        
        # Let's also create a csv file which saves all the records of John Smith
                
        training = pd.DataFrame([["2023.01.01", '100', '50', '78']], 
                                columns= ['Date', 'Dead Lift', 'Bench', 'Squads'])
        
        #The name of the csv file that keeps track of everything will be his name + Training
        nameFile = 'JohnSmithTraining.csv'
        
        training.to_csv(nameFile, mode = 'w', index = False)
        
        
        print('Database created. Congratulations, you are our second member after John Smith')
        
    else:
        #Run this code if NO exceptions were thrown
        print('Database already existed') 
        print()
        
    finally:
        #Always runs this code even if an exception was thrown
        #To show that everything goes well, we show some info
        
        print("We have " + str(df.iloc[-1][0]) + " members in this gym. Let´s see the last member: \n")
                       
        print(df.iloc[-1])
        print()
        
        return
    
