# Data Cleaning Assignment

## Preparation steps
Import packages needed for this assignment 
> Import pandas as pd

> Import numpy 

## Step 1
Loads the data into python
> upload = pd.read_csv('/Users/marialozano/Downloads/GRADUATE FALL 2022 /HHA 507 Data Science/HW Documents/School_Learning_Modalities.csv')

## Step 2
Prints the count of columns and rows 
> upload.shape allows us to get a number of rows and columns present in our dataset
This line assigns names to each value
> countRows, countColumns = upload.shape
Ran it to be able to see the number of rows in our dataset 
> countRows 
Ran it to be able to see the number of columns in our dataset 
> countColumns
## Step 3
Provides a print out of the column names 

## Step 4
Cleans the column names 


## Step 5
Cleans the strings that might exist within each column


### Step 6
Assesses white space or special characters 


## Step 7
Converts the column types to the correct types (e.g., DOB field is datetime and not object) 


## Step 8
Look for duplicate rows and remove duplicate rows 


### Step 9
Assess missingness (count of missing values per column) 


### Step 10
New data field: attempt to create a new column called modality_inperson. This column should contain a binary value of true or false. Try to write a function that takes in the old column name (learning modality), and recodes the value for a specific row to true, if the learning modality value is ‘in-person’, and recodes it to false if the value is either ‘remote’ or ‘hybrid’ 

