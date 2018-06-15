import csv

"""
TODO: date input column, 
"""


class DataManipulator:
    def __init__(self, filename):
        print("DataManipulator created")
        self.file = open(filename, "r")
        self.assign(filename)

    def __del__(self):
        print("DataManipulator destroyed")
        self.file.close()
        print("file closed")

    def assign(self, filename):
        # print(self.file.read(100))
        csvreader = csv.reader(self.file, delimiter=';',lineterminator="\r\n")
        print("DataManipulator has been connected to: " + filename)
        rownumber = 0
        for row in csvreader:
            if rownumber == 0:
                header = row
            else:
                colnumber = 0
                for col in row:
                    print('% -8s: % s' % (header[colnumber], col))
                    colnumber += 1

            rownumber += 1
