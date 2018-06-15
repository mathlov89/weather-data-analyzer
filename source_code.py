# first try
"""
data model: Convert all excel sheets into csv files
find the important 'columns'
make the pécz and front number columns for the events
find min and max dates of events
make the following table:

date || number of events 1 || weather numbers 2 || additional features 3

1: (in that combination of fetures)
2: Péczely/Front numbers to +-n days
3: unique combination of  gender, event type, ...

check if the given distribution is coming from noise, or it's something deeper (chi^2 probe)
export: histograms, p values, raw data in csv

there is a master class, with functions, for each tasks -- this should be modified, if needed
"""

from datamanipulator import DataManipulator

dm = DataManipulator("test.csv")
