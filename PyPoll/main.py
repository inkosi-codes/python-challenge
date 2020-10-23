#---------------------------------------------------------------------------------------
# An analysis of polling data to determine total ballots casted and outcome of election
#
# Author: Niguel K. Williams
# Create Date: 2020-10-19
#---------------------------------------------------------------------------------------

import os as _dir
import pandas
import sys
import io

working_dir = _dir.getcwd()# Used to get working directory of the main.py script for pulling data and saving output
csv_file = "election_data.csv"# File to be used for analysis of polling data

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

#---------------------------------------------
# The (show_results) function takes in all variables from (process_csv) function
# in order to build out Analysis print out. Below shows all the variables and what the represent. 
# Variables: 
# (x) = Total Votes | (k) = Number of votes for Khan | (kp) = Percentage of votes for Khan
# (c) = Number of votes for Correy | (cp) = Percentage of votes for Correy
# (l) =  Number of votes for Li | (lp) = Percentage of votes for Li
# (o) = Number of votes for O'Tooley | (op) = Percentage of votes for O'Tooley | (w) = Represents the election Winner
#---------------------------------------------
def show_results(x, k, kp, c, cp, l, lp, o, op, w):
    sys_output = sys.stdout
    io_string = io.StringIO()
    sys.stdout = io_string

    print("Election Results")
    print("---------------------------------")
    print(f"Total Votes: {x}")
    print("---------------------------------")
    print(f'Khan: {"{:.2%}".format(kp)} ({k})')
    print(f'Correy: {"{:.2%}".format(cp)} ({c})')
    print(f'Li: {"{:.2%}".format(lp)} ({l})')
    print(f'O\'Tooley: {"{:.2%}".format(op)} ({o})')
    print("--------------------------------")
    print(f"Winner: {w}")
    print("-------------------------------")
    p = io_string.getvalue()
    sys.stdout = sys_output

    print(p)
    output_file(p)

#----------------------------------------------------------------------
# The (process_csv) func takes in a csv file with param (csv) passed 
# from (getCsvFile). Pandas is used to read the csv file and process
# polling data and store them in their respected variable and is then passed
# to the (show_results) function for terminal output and file creation.
#----------------------------------------------------------------------
def process_csv(csv):
    rdr = pandas.read_csv(csv)
    csv_header = rdr.columns.values
    x = rdr["Voter ID"].count()
    k = len(rdr.loc[rdr["Candidate"] == "Khan", "Voter ID"].values)
    kp = k / x
    c = len(rdr.loc[rdr["Candidate"] == "Correy", "Voter ID"].values)
    cp = c / x
    l = len(rdr.loc[rdr["Candidate"] == "Li", "Voter ID"].values)
    lp = l / x
    o = len(rdr.loc[rdr["Candidate"] == "O'Tooley", "Voter ID"].values)
    op = o / x
    ws = {"Khan": k, "Correy": c, "Li": l, "O'Tooley": o}
    w = max(ws, key=ws.get)
    show_results(x, k, kp, c, cp, l, lp, o, op, w)

#----------------------------------------------------------------------
# The (getCsvFile) func uses the "working_dir" variable to identify 
# the directory in which the main.py belongs to, then uses the os library
# to walk through all levels from the root in order to find the specified 
# file stored in the "csv_file" variable.
#----------------------------------------------------------------------
def getCsvFile():
    for root, dirs, files in _dir.walk(working_dir):
        if csv_file in files:
            p = _dir.path.join(root, csv_file)
    process_csv(p)

#Script Execution
getCsvFile()