import os as _dir
import pandas
import sys
import io

working_dir = _dir.getcwd()
csv_file = "election_data.csv"


def output_file(p):
    results = open("results.txt", "w")
    results.write(p)
    results.close()


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


def process_csv(csv):
    rdr = pandas.read_csv(csv)
    x = 0
    for v in rdr["Voter ID"]:
        x += 1
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


def getCsvFile():
    for root, dirs, files in _dir.walk(working_dir):
        if csv_file in files:
            p = _dir.path.join(root, csv_file)
    process_csv(p)


getCsvFile()