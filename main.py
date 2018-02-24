import csv

plate_map= dict();  #key is plate number, value is a list object of MyValue.

class MyValue:
    def __init__(self, enter_time, enter_rid, enter_sid, exit_time, exit_rid, exit_sid):
        self.enter_time = enter_time
        self.enter_rid = enter_rid
        self.enter_sid = enter_sid
        self.exit_time = exit_time
        self.exit_rid = exit_rid
        self.exit_sid = exit_sid

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        # print "eq called"

        if not type(other) is MyValue:
            return False
        if self.enter_rid == other.enter_rid and self.enter_sid == other.enter_rid and self.exit_rid == other.exit_rid and self.exit_sid == other.exit_sid:
            return True
        else:
            return False



real_file = "./one_week.csv"
test_file = "./test.csv"

with open(test_file, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        # print row[6], row[6] == ""
        if not row[6] == "":
            plate = row[6]
            # print plate

            newValue = MyValue(row[2], row[0], row[1], row[5], row[3], row[4])
            if not plate_map.has_key(plate):
                plate_map[plate] = [newValue]
            else:
                plate_map[plate].append(newValue)

# print plate_map

pair_map = dict() #key is how many pairs, value is int showing how many cars have the same amount of pairs.
pair_count = 0
min_count = 1000000000000000
max_count = -1

for key in plate_map.keys():

    pair_count += 1

    val_count = plate_map[key].__len__()
    # print key, val_count
    if not pair_map.has_key(val_count):
        pair_map[val_count] = 1
    else:
        pair_map[val_count] += 1

    if pair_map[val_count]> max_count:
        max_count = pair_map[val_count]

    if pair_map[val_count]< min_count:
        min_count = pair_map[val_count]

pair_map[3]=0
pair_map[4]=0

# print max_count, min_count
# print pair_map
# print pair_count



pair_percent=dict()
running_total= 0.0
for x in range(0,5):
    pair_percent[x]= 0

# print pair_count
for key in pair_map.keys():
    val= pair_map[key]
    val_percent= float(val)/float(pair_count)
    running_total += float(val_percent)
    pair_percent[key] = running_total

# print pair_percent


import numpy as np
from scipy.interpolate import spline
from scipy.interpolate import interp1d

import matplotlib.pyplot as plt
from matplotlib import mlab

def drawPlot1():
    x = np.array(pair_percent.keys())
    y = np.array(pair_percent.values())
    x_smooth = np.linspace(x.min(), x.max(), 300)
    y_smooth = spline(x, y, x_smooth)
    f = interp1d(x, y)
    f2 = interp1d(x, y, kind='cubic')

    plt.xticks(np.arange(min_count, max_count, 1.0))
    plt.xlabel('number of pairs (enter stations, exit stations)')
    plt.ylabel('percent')
    plt.title("CDF")
    # plt.margins(0.02)

    # plt.plot(x, y) # orignial version
    # plt.plot(x_smooth, y_smooth) # same as the f2
    plt.plot(x_smooth, f(x_smooth))  # same with original version
    # plt.plot(x_smooth, f2(x_smooth))

    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.xticks(np.arange(0, max(pair_percent.keys()) + 0.1, 1.0))
    plt.show()

drawPlot1()

# --------------------------------------------------------------------
# here is for plot 2.

class Node:
    def __init__(self, val,next_node= None):
        self.val=val
        self.next = next_node

    def get_val(self):
        return self.val

    def get_next(self):
        return self.next
    def __repr__(self):
        return str(self.__dict__)




cars_pair_list_1=[] # a list of heads from different cars for 1 pairs
# every car has value.len of heads.

# for car in plate_map.keys():
#     # all_pairs=
#
#     heads_list=[]
#     i=0;
#     prev_head=null;
#     for pair in plate_map[car]:
#         if pair not in heads_list:
#             heads_list.append(Node(pair));
#         else:
#             head
#     print heads_list
#
#     cars_pair_list_1.append(heads_list)
#     break