import os
import csv
import collections

Record = collections.namedtuple('Record', 'date,actual_mean_temp,actual_min_temp,actual_max_temp,average_min_temp,average_max_temp,record_min_temp,record_max_temp,record_min_temp_year,record_max_temp_year,actual_precipitation,average_precipitation,record_precipitation')


sate = []

def init():
    base_folder = os.path.dirname('parse-csv-practice')
    filename = os.path.join(base_folder, 'data', 'seattle.csv')
    with open(filename) as fin:
        for line in csv.DictReader(fin):
            data = parse_row(line)
            sate.append(data)

def parse_row(row):
    row['actual_mean_temp']= int(row['actual_mean_temp'])
    r = Record(**row)
    return r



def hottest_day():
    return sorted(sate ,key = lambda x: -x.actual_mean_temp)

init()


for line in hottest_day()[:5]:
    print(line.actual_mean_temp)
