#!python3
import csv
from collections import defaultdict
from pprint import pprint

#
# Read listener data into a list of dictionaries
# Each dictionary in the list represents one row in the file
# Each item in the dictionary represents one named column in that row
#

with open("listeners.csv", newline="") as f:
    reader = csv.DictReader(f)
    listeners = list(reader)

pprint(listeners)

#
# For a selected dimension (Brand, Station etc.) add up all
# of a selected value (Hours, Sessions etc.)
# The result is a dictionary where each key represents
# one item in the dimension; and each value represents
# the sum of all the corresponding values
#

dimension_name = "Brand"
measure_name = "Sessions"

summary_data = defaultdict(int)
for listener in listeners:
    dimension_value = listener[dimension_name]
    measure_value = float(listener[measure_name])
    summary_data[dimension_value] += measure_value

pprint(summary_data)

#
# Show, in text form, the summary just created
#

for station, hours in summary_data.items():
    print(station, "=>", hours)

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
