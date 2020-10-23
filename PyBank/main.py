#---------------------------------------------------------------------------------------
# A financial analysis of banking data to provide an overall summary of profit and loss
#
# Author: Niguel K. Williams
# Create Date: 2020-10-19
#---------------------------------------------------------------------------------------

import os as _dir
import pandas
import sys
import io

# Declared global variables for use outside of functions
#-----------------------------------------------------------
working_dir = _dir.getcwd() # Used to get working directory of the main.py script for pulling data and saving output
csv_file = "budget_data.csv" # File to be used for analysis of financial data

#---------------------------------------------
# Takes in variable (p) from the (show_results) function and builds a path using
# the current working directory and creates a text file in the Analysis folder of that
# root directory.
#---------------------------------------------
def output_file(p):
    Analysis = "Analysis\\results.txt"
    result_path = _dir.path.join(working_dir, Analysis)
    results = open(result_path, "w")
    results.write(p)
    results.close()

#--------------------------------------------------------------------------------------------------
# The (show_results) function takes in all variables from (process_csv) function
# in order to build out Analysis print out. Below shows all the variables and what the represent. 
# Variables: 
# (x) = Total Months | (t) = Sum of Profit/Losses column
# (a) = Result of Average Change | (inc),(inc_date) = Represents Greatest increase number and corresponding Date
# (dec),(dec_date) =  Represents Greatest decrease number and corresponding Date
#---------------------------------------------------------------------------------------------------
def show_results(x, t, a, inc_date, inc, dec_date, dec):
# This portion of the code uses sys.stdout and io.StringIO in order to store all prints in-memory then uses
# the (p) variable to spit out to terminal while passing to the output function.
    sys_output = sys.stdout
    io_string = io.StringIO()
    sys.stdout = io_string

    print("Financial Analysis")
    print("---------------------------------")    
    print(f'Total Months: {x}')
    print(f'Total: ${t}')
    print(f'Average Change: ${a}')
    print(f'Greatest Increase in Profits:{inc_date} (${inc})')
    print(f'Greatest Increase in Profits:{dec_date} (${dec})')
    p = io_string.getvalue()   
    sys.stdout = sys_output

    print(p)# Prints out results to terminal
    output_file(p)# Passes the (p) variable to the (output_file) function to perform a new file creation of results

#----------------------------------------------------------------------
# The (process_csv) func takes in a csv file with param (csv) passed 
# from (getCsvFile). Pandas is used to read the csv file and process
# financial data and store them in their respected variable and is then passed
# to the (show_results) function for terminal output and file creation.
#----------------------------------------------------------------------
def process_csv(csv):
    rdr = pandas.read_csv(csv)
    csv_header = rdr.columns.values # Stores Header
    head = rdr["Profit/Losses"].head()[0]
    tail = rdr["Profit/Losses"].tail()[85]

    x = rdr["Date"].count()
    val = rdr["Profit/Losses"].values
    t = val.sum() # Sum of profits and losses during the financial time period
    a = round((tail - head) / x, 2)
    inc = val.max()
    inc_date = rdr.loc[rdr["Profit/Losses"] == inc, "Date"].values[0] # Uses the (inc) variable to match column "Profit/Losses" to the corresponding "Date" field 
    dec = val.min()
    dec_date = rdr.loc[rdr["Profit/Losses"] == dec, "Date"].values[0] # Uses the (dec) variable to match column "Profit/Losses" to the corresponding "Date" field 
    
    show_results(x, t, a, inc_date, inc, dec_date, dec) # Passes all populated variables to func (show_results)

#----------------------------------------------------------------------
# The (getCsvFile) func uses the "working_dir" variable to identify 
# the directory in which the main.py belongs to, then uses the os library
# to walk through all levels from the root in order to find the specified 
# file stored in the "csv_file" variable.
#----------------------------------------------------------------------
def getCsvFile():
    for root, dirs, files in _dir.walk(working_dir):
        if csv_file in files:
            p = (_dir.path.join(root, csv_file))
    process_csv(p) #Calls up function(process_csv) and passes the "p" variable to process csv data
    
#Script Execution
getCsvFile()