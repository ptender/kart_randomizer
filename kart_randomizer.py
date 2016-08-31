# -*- coding: utf-8 -*-
import os
import time
from random import shuffle, random

FILE_PATH = '/tmp/names_list.txt'
names_list = []
is_even = False

names_file = open(FILE_PATH, 'r')
for name in names_file.readlines():
    names_list.append(name)
#print "names in file list:" + str(names_list)

shuffle(names_list, random)
#print "randomized names:" + str(names_list)

n_players = len(names_list)
if n_players % 2 == 0:
    is_even = True
first_batch = second_batch = n_players // 2
if not is_even:
    first_batch += 1
print "first group racers number:" + str(first_batch)
print "second group racers number:" + str(second_batch)
group_number = 1 
racer_id = 1
for name in names_list:
    if racer_id > first_batch:
        group_number = 2
        racer_id = 1
        print "\n"
    print "Race %d, pilot %d: %s" % (group_number, racer_id, name.strip())
    racer_id += 1
    time.sleep(2)
