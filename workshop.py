#!python3
import csv
from collections import defaultdict
import operator
from pprint import pprint

with open("listeners.csv", newline="") as f:
    reader = csv.DictReader(f)
    listeners = list(reader)

pprint(listeners)

dimension_name = "Brand"
measure_name = "Hours"

listener_data = sorted(listeners, key=operator.itemgetter(dimension_name))
summary_data = defaultdict(int)
for listener in listener_data:

    dimension_value = listener[dimension_name]
    measure_value = float(listener[measure_name])

    summary_data[dimension_value] += measure_value

pprint(summary_data)

for station, hours in summary_data.items():
    print(station, "=>", hours)
