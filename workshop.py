#!python3
import csv
import itertools
from pprint import pprint


with open("listeners.csv", newline="") as f:
    reader = csv.DictReader(f)
    listeners = list(reader)

pprint(listeners)

#
# Make sure numbers are numbers
#
for listener in listeners:
    listener['Hours'] = float(listener['Hours'])
    listener['Sessions'] = float(listener['Sessions'])

pprint(listeners)

## https://docs.python.org/3/library/itertools.html#itertools.groupby

#~ station_hours = []
#~ for listener in listeners:
    #~ station_info = listener['Station'], float(listener['Hours'])
    #~ station_hours.append(station_info)
#~ station_hours.sort()

#~ pprint(station_hours)

#~ def key_on_station(l):
    #~ return l['Station']

#~ = sorted(listeners, key=key_on_station)
#~ for station, info in itertools.groupby(station_info, key_on_station):
    #~ total_hours = sum(float(i['Hours']) for i in info)
    #~ print(station, "=>", total_hours)
    #~ average_hours_per_session = sum(float(i['Hours']) for i in info) / sum(float(i['Sessions']) for i in info)
    #~ print("Average", station, "=>", average_hours_per_session)
