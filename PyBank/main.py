import os as _dir
import pandas

working_dir = _dir.getcwd() 
csv_file = "budget_data.csv"

def show_results(x, t, a, inc_date, inc, dec_date, dec):
    print("Financial Analysis")
    print("---------------------------------")    
    print(f'Total Months: {x}')
    print(f'Total: ${t}')
    print(f'Average Change: ${a}')
    print(f'Greatest Increase in Profits:{inc_date} (${inc})')
    print(f'Greatest Increase in Profits:{dec_date} (${dec})')

def process_csv(csv):
    rdr = pandas.read_csv(csv)
    x = 0
    for d in rdr.Date:
        x += 1
    val = rdr["Profit/Losses"].values
    t = val.sum()
    a = round((int(rdr.iloc[-1]["Profit/Losses"]) - int(rdr.iloc[0]["Profit/Losses"])) / x, 2)
    inc = val.max()
    inc_date = rdr.loc[rdr["Profit/Losses"] == inc, "Date"].values
    dec = val.min()
    dec_date = rdr.loc[rdr["Profit/Losses"] == dec, "Date"].values
    show_results(x, t, a, inc_date, inc, dec_date, dec)

def getCsvFile():
    for root, dirs, files in _dir.walk(working_dir):
        if csv_file in files:
            p = (_dir.path.join(root, csv_file))
    process_csv(p)
    


getCsvFile()