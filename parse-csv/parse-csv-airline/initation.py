import os
import csv
import collections

data = []

Record = collections.namedtuple('Record', 'airline, avail_seat_km_per_week, incidents_85_99,fatal_accidents_85_99, fatalities_85_99, incidents_00_14,fatal_accidents_00_14, fatalities_00_14')

def init():
    main_path = os.path.dirname('parse-csv-airline')
    directory = os.path.join(main_path, 'data', 'airline-safety.csv')
    with open(directory, 'r') as fin:
        data.clear()
        for line in csv.DictReader(fin):
            line = edit_row(line)
            data.append(line)

def edit_row(row):
    row['incidents_85_99'] = int(row['incidents_85_99'])
    row['avail_seat_km_per_week'] = int(row['avail_seat_km_per_week'])
    row['fatalities_85_99'] = int(row['fatalities_85_99'])
    row['incidents_00_14'] = int(row['incidents_00_14'])
    row['fatal_accidents_00_14'] = int(row['fatal_accidents_00_14'])
    row['fatal_accidents_85_99'] = int(row['fatal_accidents_85_99'])
    row['fatalities_00_14'] = int(row['fatalities_00_14'])

    r = Record(**row)
    return r

init()

def max_fatal_accidents_14():
    return sorted(data, key = lambda x : -x.fatal_accidents_00_14)

for i in max_fatal_accidents_14()[:5]:
    print(i.fatal_accidents_00_14)
