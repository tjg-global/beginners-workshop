#!python3
import csv
from collections import defaultdict
from pprint import pprint

#
# Read listener data into a list of dictionaries
# Each dictionary in the list represents one row in the file
# Each item in the dictionary represents one named column in that row
#

with open("listeners.csv", newline="", encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    listeners = list(reader)

pprint(listeners[0])

dimension_name = "BRAND"
measure_name = "ACTIVE_SESSIONS"

summary_data = defaultdict(int)
for listener in listeners:
    dimension_value = listener[dimension_name]
    measure_value = float(listener[measure_name])
    summary_data[dimension_value] += measure_value

pprint(summary_data)

summary_data_sort = sorted(summary_data.items(), key=lambda v:v[-1], reverse=True)

for station, hours in summary_data_sort:
    print(station, "=>", hours)

#import os
import matplotlib
matplotlib.use('TkAgg')

#
# Show the same summary on a horizontal bar chart
#
import matplotlib.pyplot as plt

labels = list(summary_data.keys())
values = list(summary_data.values())
bar_chart = plt.barh(labels, values)
plt.ylabel(dimension_name)
plt.xlabel(measure_name)
plt.show()