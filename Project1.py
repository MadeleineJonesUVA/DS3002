## This processor is designed to ingest a TSV file using its file path, output summary statistics about its rows and columns, and convert the file to CSV format

## Import the Pandas Module to use the Read Table function
import pandas as pd


## Retrieve TSV File and Produce Errors if Not Possible
# try-except statements will attempt to run the code in try block.  If the try block code does not work due to one of the except statement errors, the except block code will then be run
try: # try to read the file with the file path given
    tsv_file = "winequality.tsv" # save the file path the the variable tsv_file
    tsv = pd.read_table(tsv_file, sep = '\t')  # read the file into the tsv variable using the pd.read_table() function
                                               # sep = '\t' means separate the file based on tabs because we are reading in a tsv    
    
except FileNotFoundError: # if the file is not found, print out informative error and exit code
    print("File Path Is Not Found")
    exit()
except UnicodeDecodeError: # if file cannot be read (ex: not a tsv file), print out informative error and exit code
    print("File Cannot Be Read")
    exit()
except IndexError: # if file is not given, print out informative error and exit code
    print("File Is Not Given")
    exit()


## Generate Brief Summary of Data File Ingested 
tsv.info()   # info() summarizes information about the columns and rows of the data table it is called on, including number of rows and columns, and column names


## Convert General Format to CSV and Export
tsv.to_csv('winequality.csv', index=False)  # to_csv() exports the data table to a csv file with the specified name.
                                            # Index=False indicates to not use row indices when formatting the new csv
