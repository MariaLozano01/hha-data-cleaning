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
> list(upload)

## Step 4
Cleans the column names 
> upload.columns = upload.columns.str.replace('[^A-Za-z0-9]+', '_')

## Step 5
Cleans the strings that might exist within each column
> strings = upload.select_dtypes(include=['object']).columns

Ran the code again to make sure it worked
> strings

### Step 6
Assesses white space or special characters 
> list(upload) White spaces were replaced by an underscore when line 13 was ran

# Step 7 
Converts the column types to the correct types
> upload.dtypes In order to display the data type of each column

To convert column types to the correct types 
> upload ['billing_code'] = upload['billing_code'].astype(str)

> upload['billing_code'] = str(upload['billing_code'])

## Step 8
Look for duplicate rows and remove duplicate rows 
This line is to see which columns have suplicates
> print(upload.duplicated()) 

This line is to define how many duplicates there are
> print(upload.duplicated().sum())

There are no duplicates to remove on this dataset

### Step 9
Assess missingness (count of missing values per column) 
> upload.isnull().sum() 


### Step 10
New data field: attempt to create a new column called modality_inperson. This column should contain a binary value of true or false. Try to write a function that takes in the old column name (learning modality), and recodes the value for a specific row to true, if the learning modality value is ‘in-person’, and recodes it to false if the value is either ‘remote’ or ‘hybrid’ 

This line was added to make a new column named "Modality in Person" and determines whether to assign a 'True' statement if the row was "In PEerson" or 'False' statement if otherwise
> upload['modality_inperson'] = pd.np.where(upload.Learning_Modality.str.contains('In Person'), 'true', 'false')

This lines was done to view the entire table and make sure the modality column was added 
> print(upload.head())

