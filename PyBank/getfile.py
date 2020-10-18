import os as _dir

working_dir = _dir.getcwd() 
csv_file = "budget_data.csv"

for root, dirs, files in _dir.walk(working_dir):
    if csv_file in files:
        print(_dir.path.join(root, csv_file))

        g_inc = rdr.query(f'{sec} == {inc}')['Date']