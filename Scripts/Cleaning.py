import pandas as pd #Import packages needed
import numpy as np
#Step 1
upload = pd.read_csv('/Users/marialozano/Downloads/GRADUATE FALL 2022 /HHA 507 Data Science/HW Documents/School_Learning_Modalities.csv')
upload.shape #df.shape gives us the number of rows and columns in our specific dataset
#Step 2
countRows, countColumns = upload.shape
countRows
countColumns
#Step 3 provides column names
list(upload)
#Step 4 cleans column names
upload.columns = upload.columns.str.replace('[^A-Za-z0-9]+', '_')
#Step 5 cleans the strings that might exist within each column
strings = upload.select_dtypes(include=['object']).columns
strings
#Step 6 Assesses white space or special characters 
list(upload) #White spaces were replaced by an underscore when line 13 was ran
#Step 7 Converts the column types to the correct types 
numbers = upload.select_dtypes(include=['int64', 'float64']).columns
numbers
dates = upload.select_dtypes(include=['datetime64[ns]']).columns
dates
booleans = upload.select_dtypes(include=['bool']).columns
booleans
objects = upload.select_dtypes(include=['object']).columns
objects

upload.dtypes 

#all column typpes seem to be correct

#Step 8 Look for duplicate rows and remove any duplicate rows

print(upload.duplicated()) #this line is to see which columns have suplicates
print(upload.duplicated().sum()) #This line is to define how many duplicates there are

#The record has no duplicates to remove 

#Step 9 count of missing values per column
upload.isnull().sum() 

#Step 10 #This line was added to make a new column named "Modality in Person" and determines whether to assign a 'True' statement if the row was "In PEerson" or 'False' statement if otherwise
upload['modality_inperson'] = pd.np.where(upload.Learning_Modality.str.contains('In Person'), 'true', 'false')
print(upload.head()) #this lines was done to view the entire table and make sure the modality column was added 

